# Allegato SOP-DOC-03-A06 – MARKETING_COMUNICAZIONE (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A06  
- **Titolo:** MARKETING_COMUNICAZIONE – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `06_MARKETING_COMUNICAZIONE` contiene materiali **operativi** di marketing e comunicazione (piani, campagne, contenuti, bozze, report), con l’obiettivo di:

- organizzare e tracciare attività e asset marketing in lavorazione;
- mantenere separati i contenuti “operativi” dagli asset “master” (che risiedono in `12_TEMPLATE_E_BRAND`);
- garantire reperibilità e storicizzazione di campagne e materiali pubblicati.

**Principio chiave:** qui vive il “lavoro marketing” (work-in-progress e output), non la libreria ufficiale dei template/brand.

---

## 2. Struttura interna (al momento arbitraria)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
06_MARKETING_COMUNICAZIONE
├── (struttura interna al momento ARBITRARIA: da definire in una revisione futura)
└── 99_ARCHIVIO
```

- La tassonomia (campagne, canali, periodi, brand/linee, ecc.) è **temporaneamente lasciata arbitraria**.
- **Obbligatorio** mantenere `99_ARCHIVIO` per campagne concluse, versioni precedenti, materiali non più attivi.

---

## 3. Cosa deve stare qui (e cosa no)

### 3.1 Deve stare in `06_MARKETING_COMUNICAZIONE`
Esempi:
- piani editoriali, calendari contenuti, backlog e brief creativi;
- copy, creatività, grafiche in lavorazione, storyboard, script;
- report performance (social, ADV, SEO, newsletter, eventi), analisi e insight;
- materiali per eventi (inviti, landing, presentazioni evento, comunicati) quando non “master”;
- kit comunicazione specifici (press kit di campagna, materiali per una specifica iniziativa).

### 3.2 Non deve stare in `06_MARKETING_COMUNICAZIONE`
- loghi ufficiali, brand identity, template master (presentazioni, documenti, grafiche master) → `12_TEMPLATE_E_BRAND`;
- documenti commerciali di opportunità (offerte, proposte cliente) → `02_COMMERCIALE`;
- documentazione legale/privacy di campagne (consensi, DPA, contratti ADV) → `08_LEGALE_COMPLIANCE` e/o `11_SICUREZZA` per aspetti security;
- documentazione HR/personale → `09_PEOPLE_HR`.

---

## 4. Regole operative (sintetiche)

### 4.1 Versioning e “master”
- Per gli asset **master/ufficiali** (template grafici, loghi, guideline): usare `12_TEMPLATE_E_BRAND`.
- In questa cartella mantenere versioni operative e consegne; evitare duplicazioni di master.

### 4.2 Pubblicazione e storicizzazione
- A fine campagna/progetto marketing: spostare materiali “chiusi” in `99_ARCHIVIO` (senza cancellare).
- Conservare report e post-mortem per confronto storico.

### 4.3 Link e tracciabilità
- Quando un contenuto è collegato a un progetto o a un’opportunità, mantenere collegamenti (link) verso:
  - `02_COMMERCIALE` (opportunità) e/o
  - `03_PROGETTI` (delivery),
  evitando copie multiple.

---

## 5. Naming convention (consigliata)

### 5.1 Asset e contenuti
Formato consigliato:

`YYYY-MM-DD__MKT__CAMPAGNA_O_TEMA__ASSET__CANALE__vX.Y.ext`

Esempi:
- `2025-09-01__MKT__Prodotto_X__Landing_Copy__WEB__v0.3.docx`
- `2025-09-10__MKT__Evento_Y__Creativita__SOCIAL__v1.0.png`

### 5.2 Report
Formato consigliato:

`YYYY-MM__REPORT__CANALE_O_CAMPAGNA__KPI__vX.Y.ext`

Esempi:
- `2025-11__REPORT__LinkedIn__KPI__v1.0.pdf`

---

## 6. Collegamenti e coerenza con altri allegati

- `12_TEMPLATE_E_BRAND` → fonte per template e asset ufficiali (brand master).
- `02_COMMERCIALE` → materiali presales; linkare, non duplicare.
- `03_PROGETTI` → per iniziative legate a delivery; link bidirezionali dove utile.
- `08_LEGALE_COMPLIANCE` / `11_SICUREZZA` → per documenti vincolanti e aspetti compliance/security.

---
