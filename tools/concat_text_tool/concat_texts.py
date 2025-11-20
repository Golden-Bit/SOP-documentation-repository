#!/usr/bin/env python3
"""
concat_texts.py

Strumento da riga di comando che:
- scandisce, usando glob, i file testuali sotto una root (corrente o specificata)
- permette di filtrare per:
    * pattern glob (uno o più)
    * estensioni
    * lista di file/cartelle (--only)
- concatena in un unico file di testo i contenuti dei file trovati
- separa ogni documento con un header contenente metadati (path, nome, tipo, size, ecc.)
"""

import argparse
import glob
import os
from typing import Iterable, List, Optional, Set


# ---------- UTILS PER RICERCA FILE ----------

def resolve_to_root(root: str, path: str) -> str:
    """Se path è relativo, lo interpreta rispetto a root; se è assoluto lo lascia così."""
    if os.path.isabs(path):
        return path
    return os.path.join(root, path)


def collect_files_with_globs(root: str, patterns: List[str]) -> Set[str]:
    """Raccoglie file da root in base a una lista di pattern glob (senza duplicati)."""
    files = set()
    for pattern in patterns:
        full_pattern = os.path.join(root, pattern)
        for path in glob.iglob(full_pattern, recursive=True):
            if os.path.isfile(path):
                files.add(os.path.abspath(path))
    return files


def collect_files(
    root: str,
    patterns: List[str],
    only_paths: Optional[List[str]] = None,
) -> List[str]:
    """
    Raccoglie i file da considerare:
    - se only_paths è None: usa root + patterns
    - se only_paths è valorizzato:
        * se elemento è cartella: scandisce quella cartella con i patterns
        * se elemento è file: lo aggiunge direttamente
    In tutti i casi rimuove duplicati.
    """
    root = os.path.abspath(root)
    files: Set[str] = set()

    if only_paths:
        for p in only_paths:
            ap = os.path.abspath(resolve_to_root(root, p))
            if os.path.isdir(ap):
                files.update(collect_files_with_globs(ap, patterns))
            elif os.path.isfile(ap):
                files.add(ap)
            else:
                # path inesistente -> lo ignoriamo (potresti loggarlo se vuoi)
                continue
    else:
        files.update(collect_files_with_globs(root, patterns))

    return sorted(files)


def filter_by_extensions(files: Iterable[str], extensions: Optional[List[str]]) -> List[str]:
    """Filtra i file per estensione (se extensions non è None)."""
    if not extensions:
        return list(files)
    exts = {e.lower() if e.startswith(".") else "." + e.lower() for e in extensions}
    result = []
    for f in files:
        _, ext = os.path.splitext(f)
        if ext.lower() in exts:
            result.append(f)
    return result


# ---------- UTILS PER OUTPUT ----------

def resolve_output_path(root: str, output: Optional[str], output_dir: Optional[str]) -> str:
    """
    Determina il percorso finale del file di output.

    Logica:
    - se --output contiene un path (assoluto o con directory) -> usalo così com'è
    - altrimenti:
        * nome_file = output se fornito, altrimenti "all_texts.txt"
        * base_dir = output_dir se fornita, altrimenti root
        * output_path = base_dir / nome_file
    """
    if output and (os.path.isabs(output) or os.path.dirname(output)):
        # percorso completo esplicito
        return os.path.abspath(output)

    name = output if output else "all_texts.txt"
    base_dir = os.path.abspath(output_dir) if output_dir else os.path.abspath(root)
    return os.path.join(base_dir, name)


def read_file_text(path: str, encoding: str = "utf-8") -> str:
    """Legge un file come testo, ignorando gli errori di decodifica."""
    with open(path, "r", encoding=encoding, errors="ignore") as f:
        return f.read()


def make_doc_separator(path: str, content: str) -> str:
    """Crea il blocco di metadati che precede il contenuto del file."""
    dirname, filename = os.path.split(path)
    _, ext = os.path.splitext(filename)
    size_bytes = os.path.getsize(path)
    size_chars = len(content)
    lines = content.count("\n") + (1 if content and not content.endswith("\n") else 0)

    header = [
        "========== DOC START ==========",
        f"PATH      : {path}",
        f"DIRNAME   : {dirname}",
        f"FILENAME  : {filename}",
        f"EXTENSION : {ext or '<no_ext>'}",
        f"SIZE BYTES: {size_bytes}",
        f"SIZE CHARS: {size_chars}",
        f"LINES     : {lines}",
        "---------- DOC CONTENT ---------",
        "",
    ]
    return "\n".join(header)


# ---------- LOGICA PRINCIPALE ----------

def concat_texts(
    root: str,
    output: Optional[str],
    output_dir: Optional[str],
    patterns: List[str],
    extensions: Optional[List[str]],
    encoding: str = "utf-8",
    only_paths: Optional[List[str]] = None,
) -> None:
    """Esegue la scansione e crea il file di output."""
    root = os.path.abspath(root)
    output_path = resolve_output_path(root, output, output_dir)

    files = collect_files(root, patterns, only_paths)
    # escludi il file di output se si trova tra i candidati
    files = [f for f in files if os.path.abspath(f) != output_path]
    files = filter_by_extensions(files, extensions)

    total_docs = 0
    total_chars = 0

    out_dir = os.path.dirname(output_path) or "."
    os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding=encoding, errors="ignore") as out:
        out.write("# CONCATENATED TEXT DOCUMENT\n")
        out.write(f"# ROOT        : {root}\n")
        out.write(f"# OUTPUT FILE : {output_path}\n")
        out.write(f"# FILES       : {len(files)} (prima di eventuali errori di lettura)\n")
        if only_paths:
            out.write(f"# ONLY PATHS  : {', '.join(only_paths)}\n")
        out.write("# NOTE        : Ogni doc è preceduto da '========== DOC START =========='\n\n")

        for path in files:
            try:
                content = read_file_text(path, encoding=encoding)
            except Exception as e:
                out.write(
                    f"\n========== DOC START ==========\n"
                    f"PATH      : {path}\n"
                    f"ERROR     : Impossibile leggere il file ({e})\n"
                    f"---------- DOC CONTENT ---------\n\n"
                )
                continue

            header = make_doc_separator(path, content)
            out.write(header)
            out.write(content)
            if not content.endswith("\n"):
                out.write("\n")
            out.write("=========== DOC END ===========\n\n")

            total_docs += 1
            total_chars += len(content)

        # riepilogo finale
        out.write("\n# SUMMARY\n")
        out.write(f"# DOCUMENTS CONCATENATED : {total_docs}\n")
        out.write(f"# TOTAL CHARS            : {total_chars}\n")


# ---------- CLI ----------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scansiona una root con glob e concatena i contenuti testuali "
            "in un unico file con separatori e metadati."
        )
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Root da cui partire (default: directory corrente).",
    )
    parser.add_argument(
        "-g",
        "--glob",
        dest="patterns",
        nargs="+",
        default=["**/*"],
        help=(
            "Pattern glob (uno o più). "
            "Esempi: -g '**/*.txt' oppure -g '**/*.txt' '**/*.md'. "
            "Default: '**/*'."
        ),
    )
    parser.add_argument(
        "-e",
        "--ext",
        dest="extensions",
        nargs="+",
        help="Limita per estensioni (es: -e .txt .md .py). Se omesso, considera tutti i file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help=(
            "Percorso del file di output. "
            "Se contiene una directory (o è assoluto) viene usato così com'è. "
            "Se è solo un nome file, viene combinato con --output-dir (o con la root). "
            "Se omesso, verrà usato 'all_texts.txt' nella cartella di output."
        ),
    )
    parser.add_argument(
        "--output-dir",
        help=(
            "Cartella di output. Se non fornita, viene usata la root. "
            "Ignorata se --output è un percorso completo."
        ),
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Encoding per la lettura/scrittura dei file testuali (default: utf-8).",
    )
    parser.add_argument(
        "--only",
        dest="only_paths",
        nargs="+",
        help=(
            "Analizza SOLO questi path (file o cartelle). "
            "Se è una cartella, vengono applicati i pattern glob dentro di essa. "
            "I path relativi sono interpretati rispetto alla root."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    concat_texts(
        root=args.root,
        output=args.output,
        output_dir=args.output_dir,
        patterns=args.patterns,
        extensions=args.extensions,
        encoding=args.encoding,
        only_paths=args.only_paths,
    )


if __name__ == "__main__":
    main()
