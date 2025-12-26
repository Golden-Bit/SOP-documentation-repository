# md2pdf_pandoc — Markdown → PDF con Pandoc (Open Source)

Questo tool converte documenti **Markdown (.md)** in **PDF** usando:
- **Pandoc** (converter universale)
- un **motore PDF** (di solito **LaTeX**: `xelatex`/`lualatex`; in alternativa `tectonic`)

> Importante: **Pandoc non “crea PDF da solo”**. Per generare un PDF serve un motore esterno (LaTeX/ConTeXt/HTML→PDF, ecc.). Il default è LaTeX.  
> (Vedi manuale Pandoc: sezione “Creating a PDF”.)

---

## Quando scegliere questa soluzione
Scegli Pandoc se ti serve:
- PDF “da stampa” con tipografia molto buona
- TOC (indice), note, citazioni/bibliografia, tabelle complesse
- Math LaTeX (formula inline/block)
- template LaTeX personalizzati

---

## Requisiti (riassunto)
### Runtime (obbligatorio)
1. **pandoc** nel `PATH`
2. **un PDF engine**
   - consigliato: `xelatex` (incluso in MiKTeX/TeX Live)
   - alternativa: `tectonic` (molto comodo in CI/ambienti puliti)

### Python
- Python 3.10+ consigliato
- Nessuna dipendenza Python obbligatoria se lo script usa `subprocess` per chiamare `pandoc`.

---

## Installazione e setup — WINDOWS

### A) Installa Pandoc (scegli UN solo metodo)
**Metodo 1 — Installer ufficiale (MSI)**
- Installa Pandoc dal sito ufficiale (installer).
- L’installer **aggiunge pandoc al PATH** automaticamente.

**Metodo 2 — winget**
```powershell
winget install --source winget --exact --id JohnMacFarlane.Pandoc
```

**Metodo 3 — Chocolatey**
```powershell
choco install pandoc
```

> Nota importante: evitare installazioni multiple (MSI + winget + choco) per non ritrovarti due `pandoc.exe` diversi.

**Verifica**
```powershell
pandoc --version
where pandoc
```

---

### B) Installa un motore PDF (LaTeX)

#### Opzione consigliata su Windows: MiKTeX (con xelatex)
1. Installa **MiKTeX** (64-bit se il tuo Python è 64-bit).
2. Apri **MiKTeX Console** e fai:
   - **Updates** → *Check for updates* → *Update now*
3. Impostazione utile: abilita l’installazione automatica dei pacchetti mancanti (on-the-fly) nella console MiKTeX
   - Questo riduce gli errori “file .sty not found” al primo build.

**Verifica**
```powershell
xelatex --version
where xelatex
```

> Se vedi messaggi tipo “So far, no MiKTeX administrator has checked for updates”, spesso è perché MiKTeX è installato “for all users” e serve fare update anche in **Admin mode** (MiKTeX Console → modalità amministratore → update).

#### Alternativa: TeX Live (più pesante)
- Va benissimo ma su Windows occupa molto spazio disco.

#### Alternativa: Tectonic (senza installare TeX Live/MiKTeX)
- Installazione tipica via Chocolatey:
```powershell
choco install tectonic
tectonic --version
```
- Poi userai `--pdf-engine=tectonic`.

---

### C) Setup Python (Windows)
Dal root del repo:
```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
```

Se il tuo script non ha dipendenze Python, sei pronto.

---

## Installazione e setup — LINUX (Debian/Ubuntu)

### A) Pandoc
Puoi installare da package manager (può essere “indietro” rispetto all’ultima release):
```bash
sudo apt-get update
sudo apt-get install -y pandoc
pandoc --version
```

Se ti serve **l’ultima versione**, spesso conviene usare il pacchetto `.deb` ufficiale Pandoc.

---

### B) Motore PDF (LaTeX) — opzioni

#### Opzione “facile” (molto completa)
```bash
sudo apt-get install -y texlive
```
Pro: funziona quasi sempre out-of-the-box  
Contro: è grande.

#### Opzione “ragionevole” per xelatex (più leggera)
```bash
sudo apt-get install -y   texlive-xetex   texlive-latex-recommended   texlive-latex-extra   texlive-fonts-recommended   texlive-lang-italian   fonts-dejavu
```

**Verifica**
```bash
pandoc --version
xelatex --version
```

> Pandoc richiede vari pacchetti LaTeX (amsmath, geometry, graphicx, booktabs, longtable, ecc.). Con TeX Live in genere ci sei.

---

## Come usare lo script (Python)

### 1) Conversione base
```python
from md_to_pdf_pandoc import md_to_pdf

md_to_pdf("input.md", "output.pdf")
```

### 2) Con TOC (indice) + margini
```python
md_to_pdf(
    "input.md",
    "dist/output.pdf",
    toc=True,
    margin="2.5cm",
    pdf_engine="xelatex",
    mainfont="DejaVu Serif",
)
```

### 3) Usare Tectonic
```python
md_to_pdf("input.md", "output.pdf", pdf_engine="tectonic")
```

---

## Esempi CLI (utile per debug)

### PDF con xelatex
```bash
pandoc input.md -o output.pdf --pdf-engine=xelatex --toc -V geometry:margin=2.5cm
```

### Debug: genera il .tex intermedio
Se vuoi capire cosa sta succedendo:
```bash
pandoc input.md -s -o debug.tex
```
Poi compila il `.tex` col tuo engine per vedere l’errore reale:
```bash
xelatex debug.tex
```

---

## Gestione immagini e risorse

### Percorsi relativi
- Metti immagini in cartelle relative (es. `docs/img/logo.png`) e referenziale in Markdown:
  `![Logo](docs/img/logo.png)`
- Esegui lo script dalla root del progetto, così i path “tornano”.

### Path risorse custom (quando lavori da directory diverse)
Pandoc supporta `--resource-path` (puoi aggiungerlo allo script se serve) per dire dove cercare immagini/allegati.

---

## Personalizzazione PDF (LaTeX variables)
Esempi utili:
- Margini:
  `-V geometry:margin=2.5cm`
- Font (con xelatex/lualatex):
  `-V mainfont="DejaVu Serif"`
- Lingua:
  `-V lang=it-IT`

---

## Troubleshooting (comune)

### 1) `pandoc: command not found` / `where pandoc` vuoto
- Pandoc non è installato o non è nel PATH.
- Su Windows: reinstallare via MSI/winget/choco e riaprire il terminale.

### 2) `xelatex not found`
- Il motore non è installato, o PATH non aggiornato.
- Installa MiKTeX/TeX Live oppure usa `tectonic`.

### 3) Errori LaTeX tipo `File 'xxx.sty' not found`
- Mancano pacchetti LaTeX.
- MiKTeX: abilita installazione automatica pacchetti + fai update (anche in admin mode).
- TeX Live: installa collezioni extra (es. `texlive-latex-extra`, `texlive-fonts-recommended`).

### 4) Font non trovato (`fontspec error: The font ... cannot be found`)
- Il font indicato non è installato.
- Cambia `mainfont` o installa un font disponibile (DejaVu/Noto).

### 5) Immagini non trovate
- Controlla working directory.
- Usa percorsi relativi corretti o `--resource-path`.

### 6) Caratteri “strani” / encoding
- Pandoc lavora in UTF-8; assicurati che i tuoi `.md` siano salvati in UTF-8.

---

## Struttura repo consigliata

```
tools/md_conversion_tool/
├── md_to_pdf_pandoc.py
├── README_pandoc.md
├── examples/
│   ├── input.md
│   └── convert_pandoc.py
└── dist/
```

---

## Consigli pratici (progetto/team)
- Per documentazione interna, spesso conviene standardizzare:
  - `--pdf-engine=xelatex`
  - un set di font disponibili su tutte le macchine (DejaVu/Noto)
  - margini/TOC coerenti
- In CI/CD puoi valutare:
  - container `pandoc/latex` (se non vuoi installare TeX sulle macchine)

---

## Licenza
Pandoc è software libero (GPL). Il tuo script wrapper può avere una licenza open-source a tua scelta (MIT/Apache-2.0/GPL, ecc.).
