from __future__ import annotations
import subprocess
from pathlib import Path

def md_to_pdf(
    md_path: str | Path,
    pdf_path: str | Path,
    *,
    pdf_engine: str = "xelatex",
    toc: bool = False,
    margin: str = "2.5cm",
    mainfont: str | None = "DejaVu Serif",
) -> None:
    md_path = Path(md_path)
    pdf_path = Path(pdf_path)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(md_path),
        "-o", str(pdf_path),
        f"--pdf-engine={pdf_engine}",
        "-V", f"geometry:margin={margin}",
    ]

    if toc:
        cmd.append("--toc")

    if mainfont:
        cmd += ["-V", f"mainfont={mainfont}"]

    # Esegui e mostra errori “umani”
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            "Conversione fallita.\n"
            f"Comando: {' '.join(cmd)}\n\n"
            f"STDOUT:\n{e.stdout}\n\nSTDERR:\n{e.stderr}"
        ) from e

# esempio
md_to_pdf("C:\\Users\\info\\Desktop\\work_space\\repositories\\SOP-documentation-repository\\sop_docs\\SOP-DOC\\SOP-DOC-03_attachments\\Allegato_SOP-DOC-03-A00_INBOX.md",
          "C:\\Users\\info\\Desktop\\work_space\\repositories\\SOP-documentation-repository\\sop_docs\\SOP-DOC\\SOP-DOC-03_attachments\\Allegato_SOP-DOC-03-A00_INBOX.pdf", toc=True)
