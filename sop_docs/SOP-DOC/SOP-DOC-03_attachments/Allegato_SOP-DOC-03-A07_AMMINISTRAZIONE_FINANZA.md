# Allegato SOP-DOC-03-A07 – AMMINISTRAZIONE_FINANZA (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A07  
- **Titolo:** AMMINISTRAZIONE_FINANZA – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `07_AMMINISTRAZIONE_FINANZA` contiene la documentazione amministrativa e finanziaria **operativa e di supporto**, utile alla gestione corrente dell’organizzazione e serve a:

- garantire ordine e reperibilità dei documenti amministrativi/finanziari **non gestiti interamente in Odoo** (o che richiedono lavorazioni operative fuori dal gestionale);
- conservare prospetti di lavoro, report, riconciliazioni e documenti di supporto a decisioni economico-finanziarie;
- separare correttamente la documentazione amministrativa/finanziaria da:
  - documenti legali “di pratica” (**08_LEGALE_COMPLIANCE**),
  - documentazione HR/personale (**09_PEOPLE_HR**),
  - documenti commerciali di presales (**02_COMMERCIALE**),
  - documentazione di delivery (**03_PROGETTI**).

**Principio:** la **fonte di verità** dei dati contabili e delle transazioni (fatture registrate, scadenze, pagamenti, registrazioni) è il sistema gestionale (**Odoo** o altro sistema contabile adottato).  
Drive ospita documentazione **di supporto**, working files e materiali necessari alla gestione operativa.

---

## 2. Struttura interna (standard)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
07_AMMINISTRAZIONE_FINANZA
├── 00_POLICY_E_GUIDE
├── 01_FATTURAZIONE_E_PAGAMENTI
├── 02_CICLO_PASSIVO_FORNITORI
├── 03_BANCHE_E_RICONCILIAZIONI
├── 04_BUDGET_CONTROLLO_GESTIONE
├── 05_REPORTING_E_KPI
├── 06_TASSE_E_ADEMPIMENTI
├── 07_DOCUMENTI_SOCIETARI_FIN
├── 09_LINK_RIFERIMENTI
└── 99_ARCHIVIO
```

Regole generali:

- dove utile, si organizzano i contenuti **per anno** con sottocartelle `YYYY` (es. `2026`) dentro le sezioni principali (01–06).  
- `99_ARCHIVIO` contiene materiale storico/obsoleto o esercizi chiusi trasferiti in blocco.

---

## 3. Cosa deve stare in AMMINISTRAZIONE_FINANZA (e cosa no)

### 3.1 Deve stare in `07_AMMINISTRAZIONE_FINANZA`
Esempi (non esaustivi):

- prospetti e fogli di lavoro (cashflow, scadenziari operativi, forecast, analisi costi);
- riconciliazioni bancarie, estratti conto, quadrature (se non già gestite integralmente nel gestionale);
- documenti di pagamento (distinte, report bonifici, esiti pagamento) **senza credenziali/segreti**;
- report economico-finanziari interni, KPI, rendicontazioni;
- documentazione per adempimenti fiscali/amministrativi (modelli, ricevute, dichiarazioni, comunicazioni) secondo policy;
- documenti societari di ambito amministrativo-finanziario (es. bilanci approvati, verbali relativi a bilancio, delibere economiche), se non classificati come “legali di pratica”.

### 3.2 Non deve stare in `07_AMMINISTRAZIONE_FINANZA`
- contratti firmati, NDA, DPA, documenti legali vincolanti come fonte di verità → `08_LEGALE_COMPLIANCE`;
- documentazione presales (offerte, proposte, preventivi) → `02_COMMERCIALE`;
- documentazione operativa di progetto (deliverable, piani di progetto, meeting) → `03_PROGETTI`;
- documentazione HR personale (buste paga, documentazione individuale, valutazioni) → `09_PEOPLE_HR`;
- template “master” (modelli di fatture/offerte/report) → `12_TEMPLATE_E_BRAND`;
- evidenze security/compliance security → `11_SICUREZZA`.

**Regola anti-duplicazione:** se un documento ha fonte di verità in un’altra macro-cartella o in Odoo, in `07_AMMINISTRAZIONE_FINANZA` si conserva al massimo un **link/riferimento** (vedi §7.3), salvo necessità operative motivate.

---

## 4. Descrizione sintetica delle sottocartelle (cosa metterci)

### 4.1 00_POLICY_E_GUIDE
- procedure operative di amministrazione (checklist mese/anno, istruzioni interne);
- guide all’uso strumenti amministrativi (senza credenziali);
- note di processo interne (non template).

### 4.2 01_FATTURAZIONE_E_PAGAMENTI
Scopo: gestione operativa del **ciclo attivo** e pagamenti in uscita (lato amministrazione), quando non completamente in Odoo.

Struttura consigliata:
```
01_FATTURAZIONE_E_PAGAMENTI
├── 2025
├── 2026
└── ...
```

Dentro l’anno, consigliato (opzionale) per mese:
- `01_GEN`, `02_FEB`, … `12_DIC` **oppure** `2026-01`, `2026-02`, …

Contenuti tipici:
- copie operative di fatture emesse (se non gestite/archiviate in Odoo o se richiesto per workflow esterno);
- scadenziari operativi, solleciti (contenuti operativi, non CRM);
- conferme pagamento, esiti, distinte.

> Nota: se Odoo è fonte di verità per fatture emesse, preferire link/estrazione report piuttosto che duplicare.

### 4.3 02_CICLO_PASSIVO_FORNITORI
Scopo: gestione operativa del **ciclo passivo** (fornitori), quando non completamente in Odoo.

Struttura consigliata:
```
02_CICLO_PASSIVO_FORNITORI
├── 2025
├── 2026
└── ...
```

Contenuti tipici:
- fatture fornitori e note di credito (se necessario);
- documenti di acquisto: ordini, conferme, DDT (se non gestiti in altro sistema);
- scadenziario fornitori, verifiche e quadrature operative.

> Nota: documenti contrattuali firmati con fornitori restano in `08_LEGALE_COMPLIANCE`.

### 4.4 03_BANCHE_E_RICONCILIAZIONI
Scopo: materiali operativi legati a banche e riconciliazioni.

Struttura consigliata:
```
03_BANCHE_E_RICONCILIAZIONI
├── 2025
├── 2026
└── ...
```

Contenuti tipici:
- estratti conto, report transazioni, riconciliazioni (file Excel/CSV/PDF);
- quadrature e note di riconciliazione;
- documentazione operativa su IBAN/coordinate (senza dati sensibili non necessari).

### 4.5 04_BUDGET_CONTROLLO_GESTIONE
Scopo: budget, forecast, controllo di gestione.

Struttura consigliata:
```
04_BUDGET_CONTROLLO_GESTIONE
├── 2025
├── 2026
└── ...
```

Contenuti tipici:
- budget annuale, forecast trimestrali/mensili;
- analisi scostamenti, costing, marginalità;
- piani economici per iniziative (se non sono documenti di progetto).

### 4.6 05_REPORTING_E_KPI
Scopo: reporting periodico e indicatori economico-finanziari.

Struttura consigliata:
```
05_REPORTING_E_KPI
├── 2025
├── 2026
└── ...
```

Contenuti tipici:
- report mensili/quarterly, dashboard export, KPI pack;
- presentazioni/report interni di sintesi.

### 4.7 06_TASSE_E_ADEMPIMENTI
Scopo: documentazione per adempimenti fiscali/amministrativi (nel perimetro autorizzato).

Struttura consigliata:
```
06_TASSE_E_ADEMPIMENTI
├── 2025
├── 2026
└── ...
```

Contenuti tipici:
- dichiarazioni, ricevute invii, F24, comunicazioni, prospetti preparatori;
- corrispondenza operativa con consulenti (se non contiene dati “legali di pratica” o personali).

> Nota: documenti particolarmente sensibili possono richiedere permessi dedicati (vedi §8).

### 4.8 07_DOCUMENTI_SOCIETARI_FIN
Scopo: documentazione societaria di natura economico-finanziaria.

Contenuti tipici:
- bilanci approvati, note integrative, relazioni, verbali e delibere economiche (ove classificato come amministrativo-finanziario);
- documenti istituzionali economico-finanziari (es. rating, banche, linee di credito – se applicabile).

> Se un documento è prevalentemente “legale/contrattuale” o vincolante, collocarlo in `08_LEGALE_COMPLIANCE`.

### 4.9 09_LINK_RIFERIMENTI
File `.md`/`.txt` con link a:
- record Odoo (fatture, pagamenti, contabilità, scadenze) quando possibile;
- cartelle di progetto (solo se serve collegamento economico, senza duplicare);
- cartelle legali (contratti firmati);
- cartelle anagrafiche (fornitori/clienti) per documenti trasversali.

### 4.10 99_ARCHIVIO
Materiale storico, esercizi chiusi, versioni obsolete o documenti da conservare ma non “operativi”.

---

## 5. Naming convention delle sottocartelle (consigliata)

### 5.1 Anno
Cartella anno: `YYYY`  
Esempio: `2026`

### 5.2 Mese (se utilizzato)
Due alternative ammesse (scegliere una e mantenerla coerente per tutta l’organizzazione):

- **Opzione A (testuale):** `01_GEN`, `02_FEB`, … `12_DIC`  
- **Opzione B (ISO):** `YYYY-MM` (es. `2026-01`)

---

## 6. Naming convention dei file (consigliata)

### 6.1 Regola generale
`YYYY-MM-DD__AMMFIN__TIPODOC__DESCRIZIONE__vX.ext`

Esempi:
- `2026-01-31__AMMFIN__Report_Mensile__Gennaio__v1.0.pdf`
- `2026-02-10__AMMFIN__Riconciliazione_Banca__Febbraio__v2.xlsx`
- `2026-03-05__AMMFIN__Scadenziario__Clienti__v1.xlsx`

### 6.2 Fatture (se archiviate in Drive)
> Preferire Odoo come fonte di verità. Se serve copia operativa in Drive:

**Fatture emesse (ciclo attivo):**  
`INV-OUT__<NumeroFattura>__<Cliente>__YYYY-MM-DD.pdf`

Esempio:
- `INV-OUT__2026-0012__ACME_SRL__2026-02-28.pdf`

**Fatture fornitori (ciclo passivo):**  
`INV-IN__<NumeroFattura>__<Fornitore>__YYYY-MM-DD.pdf`

Esempio:
- `INV-IN__FT-4589__BETA_TECH_SPA__2026-03-10.pdf`

### 6.3 Pagamenti / distinte (se archiviati)
`PAY__<Metodo>__<Riferimento>__YYYY-MM-DD.ext`

Esempi:
- `PAY__BONIFICO__DISTINTA_2026-03-15__2026-03-15.pdf`
- `PAY__SEPA__ESITO_2026-03__2026-03-20.xlsx`

---

## 7. Regole operative (sintetiche)

### 7.1 Responsabilità
- **Responsabile primario:** Amministrazione/Finance (o figura delegata).  
- **Responsabile di controllo:** Direzione/Responsabile Amministrativo (se presente) + IT per aspetti permessi.

### 7.2 Versioning e documenti “finali”
- i file di lavoro (Excel, bozze) possono essere versionati con `vX`;  
- i documenti “finali” vanno marcati `FINAL` nel nome se utile:
  - `...__FINAL__v1.0.pdf`

### 7.3 Link e riferimenti (anti-duplicazione)
Quando la fonte di verità è altrove (Odoo o altra macro-cartella):
- creare un file in `09_LINK_RIFERIMENTI` (es. `LINKS__AMMFIN__2026.md`) contenente:
  - link a record Odoo,
  - link a cartelle legali,
  - link a cartelle progetto/anagrafiche se pertinenti.

### 7.4 Archiviazione
- a chiusura esercizio o periodo, consolidare in cartelle anno e spostare materiale non operativo in `99_ARCHIVIO`;
- evitare cancellazioni non tracciate: in caso di rimozione, seguire policy IT/Qualità.

---

## 8. Permessi e sicurezza (obbligatori)

- Applicare principio di **least privilege**: accesso solo a chi ha necessità operativa.
- **Dati personali** (es. documenti contenenti dati individuali) devono essere minimizzati e, se necessari, trattati con permessi restrittivi; in molti casi la collocazione corretta è `09_PEOPLE_HR`.
- **Credenziali, token, chiavi, password**: non devono mai essere salvati in Drive.
- Attenzione a documenti fiscali/finanziari sensibili: applicare policy interne e GDPR dove applicabile.

---

## 9. Collegamenti e coerenza con altri allegati

- `01_ANAGRAFICHE` → Allegato SOP-DOC-03-A01 (documenti trasversali per soggetto, link)
- `02_COMMERCIALE` → Allegato SOP-DOC-03-A02 (offerte, presales)
- `03_PROGETTI` → Allegato SOP-DOC-03-A03 (documentazione delivery; evitare duplicazioni economiche)
- `08_LEGALE_COMPLIANCE` → Allegato SOP-DOC-03-A08 (contratti firmati e documenti legali)
- `09_PEOPLE_HR` → Allegato SOP-DOC-03-A09 (documentazione HR/personale)
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12 (template e asset master)

---

## 10. Note finali

- `07_AMMINISTRAZIONE_FINANZA` è una cartella **operativa**: deve rimanere ordinata, coerente e facilmente auditabile.
- Se una tipologia di documento genera dubbi (finanza vs legale vs HR), prevale il criterio:
  - **vincolante/contrattuale** → `08_LEGALE_COMPLIANCE`
  - **personale/HR individuale** → `09_PEOPLE_HR`
  - **contabile/finanziario operativo** → `07_AMMINISTRAZIONE_FINANZA`
