# Allegato SOP-DOC-03-A02 – COMMERCIALE (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A02  
- **Titolo:** COMMERCIALE – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `02_COMMERCIALE` contiene la documentazione **presales/sales** associata a:

- **opportunità** (CRM), trattative e pipeline;
- **offerte** (tecniche/economiche), proposte e presentazioni dedicate;
- analisi preliminari, raccolta requisiti, scambi e materiali di supporto **prima** dell’avvio della commessa.

Serve a:

- garantire **ordine** e reperibilità dei materiali commerciali per opportunità;
- mantenere coerenza e tracciabilità con le **opportunità** gestite in **Odoo** (CRM);
- ridurre dispersione e duplicazioni tra aree (Commerciale, Progetti, Legale, Amministrazione).

**Principio:** `02_COMMERCIALE` ospita documenti **di opportunità** (pre-commessa).  
I documenti **di delivery** vivono in `03_PROGETTI`, i documenti **firmati** in `08_LEGALE_COMPLIANCE`, e i documenti **amministrativi operativi** in `07_AMMINISTRAZIONE_FINANZA`.

---

## 2. Struttura interna (standard)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
02_COMMERCIALE
├── <OPP-01_NomeOpportunitaOdoo>/
├── <OPP-02_NomeOpportunitaOdoo>/
├── ...
└── 99_ARCHIVIO
```

**Regola fondamentale:** si crea **una sottocartella per ciascuna opportunità**.

- La cartella opportunità usa **lo stesso nome dell’opportunità in Odoo** (vedi §5).  
- Le opportunità **chiuse** (Lost/Cancelled) o **storiche** vengono spostate in `99_ARCHIVIO` mantenendo naming e contenuto.

> Nota: se un’opportunità genera più SOW/ordini nel tempo, è possibile mantenere la stessa cartella opportunità e gestire le “fasi” al suo interno (vedi §6).

---

## 3. Cosa deve stare in COMMERCIALE (e cosa no)

### 3.1 Deve stare in `02_COMMERCIALE` (ammesso)

Esempi di contenuti ammessi:

- presentazioni **dedicate al cliente** e materiali presales;
- raccolta requisiti, note discovery, workshop pre-sales, questionari, RFI/RFP (se ricevuti);
- bozze e versioni di lavoro di:
  - offerta tecnica,
  - offerta economica,
  - proposta progettuale (non delivery),
  - statement of work **in bozza**;
- preventivi, stime, calcoli economici, pricing, business case (se non “contabilità operativa”);
- corrispondenza commerciale e minute rilevanti (email esportate, verbali incontri presales);
- documentazione richiesta dal cliente per qualificazione (es. vendor qualification) **se non è “anagrafica generale”**.

### 3.2 Non deve stare in `02_COMMERCIALE` (non ammesso)

- documentazione operativa di **progetto/commessa** (piani, verbali delivery, deliverable, report avanzamento) → `03_PROGETTI`;
- **contratti/NDA/DPA firmati** e documenti legali definitivi → `08_LEGALE_COMPLIANCE`;
- template “master” (offerte, contratti in bianco, deck istituzionali, loghi) → `12_TEMPLATE_E_BRAND`;
- fatture, estratti, riconciliazioni e contabilità operativa → `07_AMMINISTRAZIONE_FINANZA`;
- evidenze e documentazione di sicurezza/compliance security → `11_SICUREZZA`;
- documenti “di identità/relazione” della controparte (visure, profili istituzionali generici, anagrafica base) → `01_ANAGRAFICHE`.

**Regola anti-duplicazione:** se un documento “vive” in un’altra macro-cartella, in `02_COMMERCIALE` si inserisce al massimo un **link/riferimento** (vedi §7.3).

---

## 4. Regole operative (sintetiche)

### 4.1 Creazione cartella opportunità
Si crea una cartella opportunità quando:
- l’opportunità viene creata/attivata in **Odoo CRM** e sono previsti scambi/documenti;
- oppure esiste la necessità di archiviare materiale presales strutturato.

**Responsabile primario:** Owner dell’opportunità (Commerciale/BD o referente assegnato).  
**Responsabile di controllo:** Owner Area Commerciale (o PMO se definito).

### 4.2 Unicità e coerenza con Odoo
- Per ogni opportunità deve esistere **una sola** cartella in `02_COMMERCIALE`.
- Vietata la creazione di duplicati con nomi diversi: si usa il **nome Odoo** (vedi §5).

### 4.3 Passaggio Opportunità → Progetto (handover)
Quando un’opportunità viene vinta e in Odoo viene creato un **progetto/commessa**:

- la documentazione di **delivery** da quel momento in poi va in `03_PROGETTI/<NomeProgettoOdoo>/...`;
- in `02_COMMERCIALE/<NomeOpportunitaOdoo>/` si mantiene lo storico presales (offerte, negoziazione, materiale di supporto);
- si crea un file di **handover** e collegamenti incrociati (vedi §7.2).

### 4.4 Chiusura e archiviazione
- Opportunità perse/annullate: spostare la cartella in `02_COMMERCIALE/99_ARCHIVIO/`.
- Opportunità vinte: la cartella può restare in `02_COMMERCIALE` (per storico) oppure essere spostata in `99_ARCHIVIO` dopo un periodo definito internamente; in ogni caso, i link verso progetto/legale devono rimanere validi.

---

## 5. Naming convention delle cartelle opportunità

### 5.1 Naming cartella opportunità (obbligatorio)
**Regola base:** il nome della cartella deve essere **identico** al nome dell’opportunità in Odoo.

Formato consigliato (se in Odoo è disponibile un codice/ID opportunità):
- `CRM-<ID>__<NOME_OPPORTUNITA_ODOO>`

Se non si vuole usare l’ID (o non è disponibile):
- `<NOME_OPPORTUNITA_ODOO>`

**Raccomandazioni di normalizzazione (se necessario):**
- evitare caratteri che creano problemi in path/link (es. `/`, `\`, `:`); sostituire con `-` o `_`;
- mantenere il naming leggibile e stabile nel tempo.

Esempi:
- `CRM-001245__ACME_SRL__Fleet_Tracking_2026`
- `BETA_TECH__Digital_Twin_Impianto_Pilota`

### 5.2 Regola di rinomina
- Se il nome opportunità cambia in Odoo in modo sostanziale, la cartella può essere rinominata **una sola volta**, preferibilmente quando l’opportunità è ancora in fase iniziale, per non rompere link e riferimenti.
- Dopo avvio commessa, evitare rinomine: usare file `NOTE__RINOMINA.md` o un file indice per spiegare eventuali discrepanze.

---

## 6. Struttura interna della singola opportunità (standard)

All’interno di ogni cartella opportunità (es. `CRM-001245__ACME_SRL__Fleet_Tracking_2026`) la struttura consigliata è:

```
<OPPORTUNITA>
├── 01_CONTESTO_E_REQUISITI
├── 02_SCAMBI_E_MEETING_PRESALES
├── 03_OFFERTA_TECNICA
├── 04_OFFERTA_ECONOMICA
├── 05_PRESENTAZIONI_E_MATERIALI
├── 06_NEGOZIAZIONE_E_BOZZE
├── 07_HANDOVER_E_LINK
└── 99_ARCHIVIO
```

Descrizione sintetica:
- **01_CONTESTO_E_REQUISITI:** contesto, requisiti, RFI/RFP, note discovery, questionari.
- **02_SCAMBI_E_MEETING_PRESALES:** verbali presales, note call, export email rilevanti, minutes.
- **03_OFFERTA_TECNICA:** proposta tecnica, architetture di massima, scope, assunzioni, versioni.
- **04_OFFERTA_ECONOMICA:** preventivi, pricing, stime, BOM/BoQ commerciali, calcoli economici.
- **05_PRESENTAZIONI_E_MATERIALI:** deck cliente, demo, one-pager, materiali preparati ad hoc.
- **06_NEGOZIAZIONE_E_BOZZE:** bozze SOW/ordini/appendici **non firmate**, commenti, redline.
- **07_HANDOVER_E_LINK:** file indice e link verso Progetti/Legale/Anagrafiche (anti-duplicazione).
- **99_ARCHIVIO:** materiale superato/obsoleto (vecchie versioni).

> Nota: i documenti **firmati** (SOW/contratti/NDA/DPA) non vanno in `06_NEGOZIAZIONE_E_BOZZE` ma in `08_LEGALE_COMPLIANCE` (vedi §7).

---

## 7. Link e collegamenti (anti-duplicazione)

### 7.1 Principio
Per evitare copie multiple di documenti che hanno “fonte di verità” altrove:
- in `02_COMMERCIALE` si mantiene **lo storico presales**;
- per documenti definitivi/firmati o di delivery si usano **link** (Google Drive “Aggiungi collegamento”) o file `.md/.txt` con URL.

### 7.2 Dove mettere i link (consigliato)
Dentro l’opportunità, in `07_HANDOVER_E_LINK/` creare:

- `LINKS__PROGETTO.md`  
  Link alla cartella progetto in `03_PROGETTI/<NomeProgettoOdoo>/` (se esiste).

- `LINKS__LEGALE.md`  
  Link ai documenti firmati in `08_LEGALE_COMPLIANCE/.../<CONTROPARTE>/`.

- `LINKS__ANAGRAFICA.md`  
  Link alla cartella controparte in `01_ANAGRAFICHE/...`.

- `HANDOVER__<Opportunita>.md`  
  Sintesi handover: contesto, scope venduto, assunzioni, vincoli, timeline, riferimenti.

### 7.3 Contenuto minimo dei file link
- titolo documento/cartella
- breve descrizione (1 riga)
- link Google Drive
- eventuale ID Odoo (CRM/PRJ) e data

---

## 8. Naming convention dei file (consigliata)

### 8.1 Regola generale
Formato consigliato:

`YYYY-MM-DD__TIPODOC__DESCRIZIONE.ext`

Esempi:
- `2025-12-10__RFP__ACME_SRL__Richiesta_Offerta.pdf`
- `2025-12-12__Note__Discovery_Call_ACME.md`
- `2025-12-20__Offerta_Tecnica__v03.docx`
- `2025-12-20__Offerta_Economica__v03.xlsx`
- `2026-01-05__Presentazione__Demo_Soluzione.pptx`

### 8.2 TIPODOC (valori suggeriti)
`RFP`, `RFI`, `Note`, `Verbale`, `Offerta_Tecnica`, `Offerta_Economica`, `Presentazione`, `Preventivo`, `Stima`, `Redline`, `Email_Export`, `Altro`

### 8.3 Versioning (quando utile)
Per documenti iterativi (offerte, proposte) usare:
- `v01`, `v02`, `v03` nel nome file, oppure
- versioning nativo Google (se Google Docs/Sheets/Slides).

---

## 9. Collegamenti e coerenza con altri allegati

- `01_ANAGRAFICHE` → Allegato SOP-DOC-03-A01 (dati di controparte e repository trasversale soggetto)
- `03_PROGETTI` → Allegato SOP-DOC-03-A03 (documentazione di delivery)
- `07_AMMINISTRAZIONE_FINANZA` → Allegato SOP-DOC-03-A07 (fatturazione e amministrazione operativa)
- `08_LEGALE_COMPLIANCE` → Allegato SOP-DOC-03-A08 (contratti firmati, NDA, DPA, evidenze legali)
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12 (template master offerte, documenti e brand)

---
