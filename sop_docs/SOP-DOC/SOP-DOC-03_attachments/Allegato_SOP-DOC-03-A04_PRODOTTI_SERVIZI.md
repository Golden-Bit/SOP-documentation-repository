# Allegato SOP-DOC-03-A04 – PRODOTTI_SERVIZI (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A04  
- **Titolo:** PRODOTTI_SERVIZI – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `04_PRODOTTI_SERVIZI` è il **catalogo operativo** di prodotti/servizi/soluzioni dell’organizzazione.

Serve a:

- mantenere un **punto unico** dove reperire materiali **riusabili** (tecnici e/o di offerta standard) legati all’offerta;
- garantire **coerenza** tra ciò che viene venduto (Commerciale), ciò che viene consegnato (Progetti) e ciò che viene documentato (eventualmente anche su GitHub Pages);
- ridurre duplicazioni (es. “schede prodotto” sparse in progetti/opportunità);
- creare una struttura “agganciabile” a Odoo: **una cartella per ciascun prodotto/servizio** con riferimento al relativo record Odoo.

**Principio chiave:** in `04_PRODOTTI_SERVIZI` vivono i contenuti **standard e riusabili** dell’offerta (master operativi).  
I contenuti **specifici per cliente/opportunità** vivono in `02_COMMERCIALE`; i deliverable **specifici di delivery** vivono in `03_PROGETTI`.

---

## 2. Struttura interna (standard)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
04_PRODOTTI_SERVIZI
├── 00_README_E_LINEE_GUIDA
├── PRD-<CODICE_ODOO>_<NOME_PRODOTTO>/
├── SRV-<CODICE_ODOO>_<NOME_SERVIZIO>/
├── ...
└── 99_ARCHIVIO
```

### 2.1 Regola base: 1 cartella = 1 prodotto/servizio (Odoo)

- Per **ogni** prodotto/servizio presente in Odoo e “attivo” (o in fase di lancio) deve esistere una cartella dedicata in `04_PRODOTTI_SERVIZI`.
- Il **riferimento Odoo** è parte del naming della cartella (vedi §5.1).

### 2.2 Struttura interna della singola cartella prodotto/servizio

La **struttura interna** dentro `PRD-.../` e `SRV-.../` è **arbitraria** e può essere definita liberamente dai responsabili dell’offerta/prodotto, in funzione delle esigenze operative.

Vincoli minimi consigliati (non strutturali):
- mantenere **ordine** e **reperibilità** (evitare file “random” non spiegati);
- evitare duplicazioni di “master” in altre macro-cartelle (vedi §7).

---

## 3. Cosa deve stare in PRODOTTI_SERVIZI (e cosa no)

### 3.1 Deve stare in `04_PRODOTTI_SERVIZI` (ammesso)

Esempi di contenuti ammessi (standard/riusabili):

- descrizione e posizionamento del prodotto/servizio (overview, value proposition, FAQ interne);
- documentazione tecnica riusabile (architetture standard, componenti, specifiche generali, guide di configurazione standard, manuali interni di delivery **non cliente-specifici**);
- schede/one-pager e materiali “base” riutilizzabili (non campagne), utili anche a Commerciale;
- listini/rate card **standard** (non personalizzati per singolo cliente), se non gestiti integralmente in Odoo;
- benchmark, comparativi, note di roadmap **non confidenziali** o comunque gestite con permessi adeguati;
- materiali di onboarding interno sul prodotto/servizio (in alternativa o in link a `05_FORMATIVO_LINEE_GUIDA`).

> Nota: se una documentazione diventa “ufficiale/stabile” e deve essere pubblicata/versionata, la **fonte di verità** può essere GitHub/GitHub Pages (SOP-DOC-02), mantenendo in Drive link e/o asset operativi.

### 3.2 Non deve stare in `04_PRODOTTI_SERVIZI` (vietato / da evitare)

- documentazione **specifica per cliente/opportunità** (proposte, offerte, presentazioni cliente personalizzate) → `02_COMMERCIALE`;
- deliverable e documenti **di progetto** (piani progetto, verbali delivery, report cliente, materiali di commessa) → `03_PROGETTI`;
- contratti, NDA, DPA firmati e documentazione legale “di pratica” → `08_LEGALE_COMPLIANCE`;
- campagne, piani editoriali, creatività operative marketing → `06_MARKETING_COMUNICAZIONE`;
- template “master” (presentazioni standard, template offerta, modelli documenti) → `12_TEMPLATE_E_BRAND`;
- procedure, policy e audit di sicurezza/compliance security → `11_SICUREZZA`.

**Regola anti-duplicazione:** `04_PRODOTTI_SERVIZI` è un catalogo “master operativo”. Altrove si creano documenti derivati o si usano **link**.

---

## 4. Regole operative (sintetiche)

### 4.1 Creazione cartella prodotto/servizio
- La cartella viene creata quando il prodotto/servizio:
  - esiste come record in Odoo (anche in bozza ma con codice assegnato), **oppure**
  - è approvato come “in avvio” (Go/No-Go) e si vuole impostare il catalogo.
- La creazione è responsabilità dell’**Owner di prodotto/servizio** (o responsabile offerta), in coordinamento con Qualità/Documentazione se richiesto.

### 4.2 Coerenza con Odoo (minimo indispensabile)
Ogni cartella prodotto/servizio dovrebbe consentire un aggancio chiaro al record Odoo:
- il **codice Odoo** è nel nome cartella (vedi §5.1);
- dentro la cartella è raccomandato un file `INDEX.md` (o equivalente) con:
  - link al record Odoo,
  - breve descrizione e “cosa cercare qui”,
  - eventuali link a documentazione ufficiale (GitHub Pages) se presente.

> Se l’azienda adotta un collegamento automatico Odoo↔Drive (SOP-DOC-01), il link/ID Odoo diventa requisito operativo.

### 4.3 Versioning (principio)
- Evitare “final_v7_definitivo2”.
- Usare versioni esplicite (es. `v1.0`, `v1.1`) e/o date nel naming dei file (vedi §5.2).
- Quando un documento viene sostituito, spostare la versione superata in una posizione coerente (a discrezione dell’owner) oppure usare `99_ARCHIVIO` se non più attuale.

### 4.4 Ciclo di vita e dismissione
- Prodotti/servizi dismessi, superati o non più venduti:
  - spostare la cartella in `99_ARCHIVIO` mantenendo naming e riferimenti Odoo;
  - non eliminare senza valutazione congiunta (Owner + Direzione/Qualità, se applicabile).

---

## 5. Naming convention (cartelle e file)

### 5.1 Naming cartelle prodotto/servizio (obbligatorio)

Formato:

`PRD-<CODICE_ODOO>_<NOME_PRODOTTO>`  
`SRV-<CODICE_ODOO>_<NOME_SERVIZIO>`

Dove:
- `PRD` = Prodotto (deliverable “packaged”, piattaforma, modulo, ecc.)
- `SRV` = Servizio (consulenza, managed service, supporto, progetto standardizzato, ecc.)
- `CODICE_ODOO` = **riferimento Odoo** preferibile:
  - *Internal Reference / Default Code* del prodotto/servizio (raccomandato), **oppure**
  - un codice definito dal processo interno (es. `ODOO-PRD-000123`) se si preferisce non usare il default code.
- `NOME_*` = nome normalizzato (MAIUSCOLO, underscore `_`, senza caratteri speciali)

Esempi:
- `PRD-GEOSAT24_FLEET_TRACKING_PLATFORM`
- `SRV-SRV-001_FLEET_TRACKING_MANAGED_SERVICE`
- `PRD-ODOO-PRD-000123_DIGITAL_TWIN_SUITE`

> Se `CODICE_ODOO` non è disponibile: usare temporaneamente `NA` e sostituire appena assegnato (`PRD-NA_...`).

### 5.2 Naming file (consigliato)

Formato consigliato:

`YYYY-MM-DD__TIPODOC__PRD|SRV-<CODICE_ODOO>__TITOLO__vX.Y.ext`

Esempi:
- `2025-12-01__SPEC__PRD-GEOSAT24__Architettura_generale__v1.2.pdf`
- `2025-11-20__ONEPAGER__SRV-SRV-001__Descrizione_servizio__v1.0.pptx`
- `2025-10-05__GUIDA__PRD-ODOO-PRD-000123__Installazione__v2.0.md`

### 5.3 TIPODOC (valori suggeriti)
- `OVERVIEW`
- `ONEPAGER`
- `SPEC`
- `ARCH`
- `GUIDA`
- `FAQ`
- `PRICELIST`
- `RATESCARD`
- `CHANGELOG`
- `ROADMAP`

---

## 6. Dove archiviare i file “cliente-specifici” (regola pratica)

- Se un documento è **personalizzato per un cliente/opportunità** (es. presentazione con logo cliente, offerta economica dedicata, SOW in bozza):
  - → `02_COMMERCIALE/<OPP-...>/...`
- Se un documento è un **deliverable di progetto** (report, verbali delivery, piani, documentazione consegnata al cliente):
  - → `03_PROGETTI/<NomeProgettoOdoo>/...`
- Se un documento è **standard e riusabile** (base comune dell’offerta):
  - → `04_PRODOTTI_SERVIZI/<PRD|SRV-...>/...`

---

## 7. Link e riferimenti (anti-duplicazione)

### 7.1 Regola
- Un contenuto “master operativo” sta in `04_PRODOTTI_SERVIZI`.
- Altrove (Commerciale/Progetti) si usano:
  - link Drive (“Aggiungi collegamento”), **oppure**
  - file `LINKS_*.md` con URL e riferimenti.

### 7.2 Esempi di link consigliati
- In `02_COMMERCIALE/<OPP-...>/`:
  - `LINKS_PRODOTTO_SERVIZIO.md` con link ai materiali master in `04_PRODOTTI_SERVIZI`
- In `03_PROGETTI/<NomeProgettoOdoo>/`:
  - `LINKS_PRODOTTO_SERVIZIO.md` con link a guide/spec standard utili al delivery

---

## 8. Permessi (linea guida)

- Di default `04_PRODOTTI_SERVIZI` dovrebbe essere visibile a:
  - Commerciale, PM, Delivery (per riuso e coerenza), con capacità di lettura e contribuzione secondo ruoli.
- Alcuni contenuti possono richiedere accesso ristretto (es. roadmap sensibile, pricing interno):
  - gestire permessi a livello di cartella prodotto/servizio o singoli file (need-to-know).

---

## 9. Collegamenti e coerenza con altri allegati

- `02_COMMERCIALE` → Allegato SOP-DOC-03-A02 (materiali cliente-specifici, offerte, opportunità)
- `03_PROGETTI` → Allegato SOP-DOC-03-A03 (deliverable e documentazione di commessa)
- `05_FORMATIVO_LINEE_GUIDA` → Allegato SOP-DOC-03-A05 (formazione trasversale, linee guida generali)
- `06_MARKETING_COMUNICAZIONE` → Allegato SOP-DOC-03-A06 (campagne e contenuti marketing operativi)
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12 (template master, asset e brand)

---
