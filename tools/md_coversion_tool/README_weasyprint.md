# md2pdf_weasyprint — Markdown → HTML → PDF con WeasyPrint (Open Source)

Questo tool converte **Markdown** in **PDF** passando per **HTML**:
1) Markdown → HTML (con `markdown-it-py`)
2) HTML/CSS → PDF (con **WeasyPrint**)

È ideale se:
- vuoi controllare l’aspetto con **CSS**
- vuoi un PDF “web-like” (layout simile a stampa da browser)
- preferisci evitare LaTeX

> Nota: WeasyPrint **non esegue JavaScript**. Se usi MathJax o rendering JS, devi pre-renderizzare oppure usare Pandoc+LaTeX.

---

## Requisiti (riassunto)
### Python
- Python 3.10+ consigliato

### Pacchetti Python
- `weasyprint`
- `markdown-it-py`

### Dipendenze di sistema
WeasyPrint richiede librerie native:
- **Cairo**
- **Pango**
- **GDK-Pixbuf**
- **GLib/GObject**
- (più altre dipendenze minori come `libffi`, `shared-mime-info`, `fontconfig`)

Su Linux: si installano con package manager.  
Su Windows: bisogna fornire DLL (approccio consigliato: **MSYS2**).

---

## Installazione Python (Windows/Linux)

### 1) Crea e attiva venv
**Windows (PowerShell)**
```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
```

**Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

### 2) Installa dipendenze Python
```bash
pip install weasyprint markdown-it-py
```

### 3) Verifica
```bash
python -m weasyprint --info
```
Se `--info` fallisce, mancano librerie native (vedi sezioni OS).

---

# Setup OS — LINUX

## Debian/Ubuntu (consigliato)
```bash
sudo apt-get update
sudo apt-get install -y   libcairo2   libpango-1.0-0   libpangocairo-1.0-0   libgdk-pixbuf-2.0-0   libffi8   shared-mime-info   fontconfig   fonts-dejavu-core
```

Poi:
```bash
python -m weasyprint --info
```

## Fedora (indicativo)
```bash
sudo dnf install -y cairo pango gdk-pixbuf2 libffi shared-mime-info fontconfig dejavu-sans-fonts
```

## Arch (indicativo)
```bash
sudo pacman -S --needed cairo pango gdk-pixbuf2 libffi shared-mime-info fontconfig ttf-dejavu
```

> Se lavori in container/minimal image, ricordati anche i font: senza font, alcuni caratteri possono risultare “quadrati”/mancanti.

---

# Setup OS — WINDOWS (fix completo per errori DLL tipo `libgobject-2.0-0` / 0x7e)

Se vedi errori come:
- `OSError: cannot load library 'libgobject-2.0-0': error 0x7e`
- `WeasyPrint could not import some external libraries`

significa che WeasyPrint **non trova le DLL** di GLib/Pango/GTK stack.

## Step 0 — Controlla 64-bit vs 32-bit (fondamentale)
Nel tuo venv:
```powershell
python -c "import platform; print(platform.architecture())"
```
Se è `64bit`, usa MSYS2 x86_64 e `mingw64`.  
Se è `32bit`, servono pacchetti i686 e path `mingw32` (sconsigliato, meglio migrare a 64-bit).

---

## Metodo consigliato: MSYS2 (raccomandato dagli autori)

### Step 1 — Installa MSYS2
- Installa MSYS2 (x86_64) in un path semplice (es. `C:\msys64`).

### Step 2 — Aggiorna MSYS2
Apri **MSYS2 UCRT64** o **MSYS2 MSYS** (dipende dalla tua installazione) e fai:
```bash
pacman -Syuu
```
Chiudi e riapri la shell, poi:
```bash
pacman -Su
```
Ripeti finché non ci sono più aggiornamenti.

### Step 3 — Installa Pango (porta anche GLib/GObject, Cairo, ecc.)
Nella shell MSYS2:
```bash
pacman -S mingw-w64-x86_64-pango
```

> In molti casi basta questo pacchetto perché trascina dipendenze necessarie.

---

## Step 4 — Rendi visibili le DLL a WeasyPrint

### Opzione A (consigliata): `WEASYPRINT_DLL_DIRECTORIES`
**CMD**
```bat
set WEASYPRINT_DLL_DIRECTORIES=C:\msys64\mingw64\bin
python -m weasyprint --info
```

**PowerShell**
```powershell
$env:WEASYPRINT_DLL_DIRECTORIES="C:\msys64\mingw64\bin"
python -m weasyprint --info
```

Se `--info` non dà errori, puoi lanciare lo script.

### Opzione B: aggiungi `mingw64\bin` al PATH (sessione corrente)
```bat
set PATH=C:\msys64\mingw64\bin;%PATH%
python -m weasyprint --info
```

### Opzione C: rendilo permanente
```bat
setx WEASYPRINT_DLL_DIRECTORIES "C:\msys64\mingw64\bin"
```
Poi **chiudi e riapri** terminale/IDE.

---

## Step 5 — IDE / runner che non eredita env var (fix “in codice”)
Se lanci da PyCharm/VSCode e continua a fallire, aggiungi all’inizio del tuo script (prima dell’import di WeasyPrint):

```python
import os
os.add_dll_directory(r"C:\msys64\mingw64\bin")
from weasyprint import HTML, CSS
```

---

## Alternative Windows (non consigliata, ma possibile): GTK runtime
Alcune guide usano un GTK runtime (es. “GTK3-Runtime Win64”) e poi aggiungono la cartella `bin` al PATH, ad esempio:
`C:\Program Files\GTK3-Runtime Win64\bin`

Funziona, ma MSYS2 tende a essere più riproducibile e aggiornabile.

---

## Pitfall comuni su Windows
- **Non mischiare** più “fonti di DLL” (MSYS2 + runtime GTK separato + Conda): può causare errori “entry point not found”.
- Se hai più GTK installati, imposta `WEASYPRINT_DLL_DIRECTORIES` a **una sola** cartella (quella giusta), per evitare che WeasyPrint carichi DLL incompatibili.
- Se hai Python 64-bit ma MSYS2 32-bit (o viceversa) → errore sicuro.

---

## Uso dello script (Python)

### Esempio base
```python
from md_to_pdf_weasyprint import md_to_pdf_weasyprint

with open("input.md", "r", encoding="utf-8") as f:
    md_to_pdf_weasyprint(f.read(), "output.pdf")
```

### Con CSS inline
```python
from md_to_pdf_weasyprint import md_to_pdf_weasyprint

css = """
@page { margin: 2.5cm; }
body { font-family: sans-serif; line-height: 1.5; }
h1, h2, h3 { margin-top: 1.2em; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ccc; padding: 6px; }
pre { padding: 10px; background: #f6f6f6; overflow-x: auto; }
"""

md_text = open("input.md", encoding="utf-8").read()
md_to_pdf_weasyprint(md_text, "output.pdf", css_text=css)
```

### IMPORTANT: immagini con path relativi (base_url)
Se nel Markdown hai immagini con path relativi (es. `![img](docs/img/a.png)`), WeasyPrint le risolve meglio se fornisci un `base_url` all’HTML.
Se vuoi supporto robusto alle immagini, considera di modificare lo script per usare:
```python
HTML(string=html, base_url=str(Path.cwd())).write_pdf(...)
```

---

## Troubleshooting

### 1) `python -m weasyprint --info` fallisce su Windows
- 99%: DLL non trovate.
- Controlla:
  - `WEASYPRINT_DLL_DIRECTORIES` punta a `...\msys64\mingw64\bin`
  - Python 64-bit ↔ MSYS2 x86_64
  - non ci sono altre GTK nel PATH che “sporcano” il caricamento DLL

### 2) Errore specifico: `libgobject-2.0-0` / `pango-1.0-0` / `cairo-2`
- È sempre la stessa classe: mancano DLL o non sono nel path corretto.

### 3) PDF generato ma senza font corretti
- Installa font (DejaVu/Noto) e specifica in CSS `font-family`.
- Su Linux installa pacchetti font (es. `fonts-dejavu`).

### 4) Output “vuoto”
- Stampa l’HTML intermedio per debug:
```python
from markdown_it import MarkdownIt
print(MarkdownIt("commonmark").render(md_text))
```

---

## Struttura repo consigliata
```
tools/md_conversion_tool/
├── md_to_pdf_weasyprint.py
├── README_weasyprint.md
├── examples/
│   ├── input.md
│   └── convert_weasyprint.py
└── dist/
```

---

## Licenza
WeasyPrint e markdown-it-py sono open-source; il tuo script wrapper può avere una licenza open-source a tua scelta (MIT/Apache-2.0/GPL, ecc.).
