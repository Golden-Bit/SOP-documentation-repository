# `concat_texts.py`

Strumento da riga di comando in Python per:

* scandire una **root** (directory) con uno o più **pattern glob**
* filtrare i file per **estensione**
* limitare la scansione a una **lista di file/cartelle specifica** (`--only`)
* concatenare in **un unico file di testo** i contenuti di tutti i file trovati
* separare ogni documento con un **header di metadati** (path, nome file, estensione, dimensioni, numero di righe, ecc.)

Pensato per creare rapidamente un *corpus testuale* a partire da un albero di directory (es. per analisi NLP, indicizzazione, addestramento LLM, ecc.).

---

## Requisiti

* **Python 3.8+** (qualunque versione recente va bene)
* Sistema operativo: Linux, macOS, Windows (su Windows i comandi `chmod`/esecuzione diretta cambiano leggermente)

---

## Installazione

1. Copia lo script in una cartella a tua scelta, ad esempio:

   ```bash
   cp concat_texts.py ~/bin/concat_texts.py
   ```

2. (Opzionale, ma comodo su Linux/macOS) Rendi lo script eseguibile:

   ```bash
   chmod +x ~/bin/concat_texts.py
   ```

3. Assicurati che la cartella sia nel tuo `PATH` (oppure esegui lo script tramite `python`):

   * Esecuzione diretta (se eseguibile e nel PATH):

     ```bash
     concat_texts.py ...
     ```

   * Esecuzione con Python esplicito:

     ```bash
     python concat_texts.py ...
     ```

     oppure

     ```bash
     python3 concat_texts.py ...
     ```

---

## Utilizzo di base

Sintassi generale:

```bash
concat_texts.py [ROOT] [OPZIONI]
```

Se non specifichi `ROOT`, viene usata la **directory corrente** (`.`).

Esempio minimale:

```bash
# Analizza la directory corrente con il glob di default ("**/*")
# e crea all_texts.txt nella root
concat_texts.py
```

---

## Opzioni disponibili

### Positional: `ROOT`

```bash
concat_texts.py ROOT [opzioni]
```

* `ROOT` (opzionale, default: `.`)
  Directory da cui partire per la scansione.
  Se omessa, è la directory corrente.

---

### `-g`, `--glob PATTERN [PATTERN ...]`

```bash
-g "**/*.txt"
-g "**/*.txt" "**/*.md"
```

* Uno o più **pattern glob** relativi alla `ROOT` (o alle cartelle indicate in `--only`).
* Default: `**/*` → tutti i file sotto la root (in modo ricorsivo).
* Puoi usare un **singolo glob** o una **lista di globs**; i risultati vengono **uniti senza duplicazioni**.

Esempi:

```bash
# Solo file .txt
concat_texts.py . -g "**/*.txt"

# File .txt e .md (merge senza duplicati)
concat_texts.py . -g "**/*.txt" "**/*.md"
```

---

### `-e`, `--ext EXT [EXT ...]`

```bash
-e .txt .md .py
```

* Filtra per estensione (es. `.txt`, `.md`, `.py`).
* Se omesso, **tutti i file** corrispondenti ai glob vengono considerati.
* L’estensione è case-insensitive; puoi scrivere `.TXT`, `.txt`, ecc.

Esempi:

```bash
# Solo .txt e .md trovati tramite i glob specificati
concat_texts.py . -g "**/*" -e .txt .md
```

---

### `--only PATH [PATH ...]`

```bash
--only src docs README.md
```

* Limita la scansione a una **lista esplicita di file/cartelle**.
* Ogni elemento può essere:

  * una **cartella** → viene scansionata con i pattern `--glob` al suo interno
  * un **file** → viene aggiunto direttamente all’elenco dei file da concatenare
* I **path relativi** sono interpretati rispetto alla `ROOT`.
* I risultati (da tutte le `--only`) vengono mergiati e deduplicati.

Esempi:

```bash
# Analizza solo "src" e "docs" (e i loro sottoalberi)
concat_texts.py . --only src docs -g "**/*.py" "**/*.md"

# Analizza alcune cartelle + alcuni file specifici
concat_texts.py . --only src tests README.md -g "**/*.py" "**/*.md"
```

---

### `-o`, `--output OUTPUT_FILE`

```bash
-o all_texts.txt
-o /percorso/assoluto/tutto.txt
-o risultati.txt
```

Determina **nome e/o percorso** del file di output.

Logica:

1. Se `--output` è un **percorso completo o contiene una directory** (es. `/tmp/tutto.txt`, `out/all.txt`):

   * Viene usato **esattamente** quel percorso; `--output-dir` viene ignorato.

2. Se `--output` è **solo un nome file** (es. `all_texts.txt`):

   * Viene combinato con:

     * `--output-dir` (se fornita), oppure
     * la `ROOT` (se `--output-dir` non è specificata).

3. Se `--output` è **omesso**:

   * Nome di default: `all_texts.txt`.
   * Directory: quella indicata da `--output-dir` (se presente), altrimenti la `ROOT`.

Esempi:

```bash
# Output in ROOT/all_texts.txt
concat_texts.py .

# Output in ROOT/risultati.txt
concat_texts.py . -o risultati.txt

# Output in ./out/merged.txt (directory ./out creata se non esiste)
concat_texts.py . --output-dir ./out -o merged.txt

# Output in ./out/all_texts.txt (nome di default)
concat_texts.py . --output-dir ./out

# Output assoluto in /tmp/tutto.txt (ignora --output-dir)
concat_texts.py . -o /tmp/tutto.txt --output-dir ./out
```

---

### `--output-dir OUTPUT_DIR`

```bash
--output-dir ./out
```

* Specifica la **cartella** in cui scrivere il file di output (quando `--output` non è un percorso completo).
* Se **non fornita**, la cartella di output è la **root**.

---

### `--encoding ENCODING`

```bash
--encoding utf-8
--encoding latin-1
```

* Encoding usato per leggere i file testuali e scrivere l’output.
* Default: `utf-8`.
* Gli errori di decodifica vengono **ignorati** (`errors="ignore"`), per evitare crash se qualche file ha caratteri “strani”.

---

## Comportamento dettagliato

### 1. Selezione dei file

1. Si parte da `ROOT` (o dalle cartelle indicate in `--only`).
2. Si applicano i pattern `--glob` (uno o più).
3. I risultati vengono uniti in un **set** per eliminare duplicati.
4. Se è stata fornita `--ext`, si filtrano solo i file con estensioni ammesse.
5. Il file di output (se ricadrebbe nei glob) viene **escluso** per evitare autoriferimenti.

---

### 2. Struttura del file di output

All’inizio del file viene scritto un header generale, ad esempio:

```text
# CONCATENATED TEXT DOCUMENT
# ROOT        : /percorso/alla/root
# OUTPUT FILE : /percorso/di/output/all_texts.txt
# FILES       : 42 (prima di eventuali errori di lettura)
# ONLY PATHS  : src, docs          # (solo se usi --only)
# NOTE        : Ogni doc è preceduto da '========== DOC START =========='
```

Poi, per **ogni file** concatenato, viene aggiunto un blocco del tipo:

```text
========== DOC START ==========
PATH      : /percorso/completo/al/file.txt
DIRNAME   : /percorso/completo/al
FILENAME  : file.txt
EXTENSION : .txt
SIZE BYTES: 1234
SIZE CHARS: 1200
LINES     : 42
---------- DOC CONTENT ---------

<contenuto del file...>
=========== DOC END ===========

```

Alla fine del file, un riepilogo:

```text
# SUMMARY
# DOCUMENTS CONCATENATED : 42
# TOTAL CHARS            : 123456
```

---

## Esempi pratici

### 1. Concatenare tutti i .txt sotto la directory corrente

```bash
concat_texts.py . -g "**/*.txt"
```

Risultato: `all_texts.txt` nella directory corrente, contenente tutti i `.txt`.

---

### 2. Concatenare `.txt` e `.md` da alcune cartelle specifiche

```bash
concat_texts.py . \
  --only src docs \
  -g "**/*.txt" "**/*.md"
```

Risultato:

* Vengono scansionate solo `src` e `docs` (rispetto alla `ROOT`).
* In ognuna si cercano file che matchano `**/*.txt` e `**/*.md`.
* L’output è `all_texts.txt` nella root.

---

### 3. Usare una cartella di output dedicata

```bash
concat_texts.py . \
  -g "**/*.py" \
  -e .py \
  --output-dir ./out \
  -o codice_concatenato.txt
```

Risultato: `./out/codice_concatenato.txt` contenente tutti i `.py` sotto la root.

---

### 4. Solo alcuni file e cartelle mischiati

```bash
concat_texts.py . \
  --only src tests README.md \
  -g "**/*.py" "**/*.md"
```

* `src` e `tests` vengono scansionate con i glob.
* `README.md` viene aggiunto direttamente.
* Duplicati (stessi path) vengono rimossi automaticamente.

---

## Note e consigli

* Se hai alberi molto grandi, può essere utile specificare da subito glob mirati (es. `**/*.txt`) e/o `--ext` per evitare di aprire file non testuali.
* Se alcuni file hanno encoding diversi (es. latin-1, cp1252), valuta se:

  * usare un encoding più generoso (`latin-1`), oppure
  * fare una pre-pulizia / conversione dei file.
* L’output è pensato per essere facilmente:

  * indicizzato,
  * passato a strumenti NLP,
  * “chunkato” da altri script.