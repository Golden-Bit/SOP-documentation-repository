# Allegato SOP-DOC-03-A03 – PROGETTI (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A03  
- **Titolo:** PROGETTI – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `03_PROGETTI` contiene la documentazione relativa a **progetti/commesse** (interni o verso clienti) e serve a:

- centralizzare tutti i file necessari alla **delivery** e alla **gestione operativa** del progetto;
- garantire tracciabilità e reperibilità nel tempo (audit, passaggi di consegne, chiusura progetto);
- assicurare coerenza con la gestione progetto in **Odoo** (progetti, task, commesse, timesheet), secondo **SOP-DOC-01**.

**Principio:** per ogni progetto esiste **una sola cartella progetto** dentro `03_PROGETTI`, e il suo nome è **lo stesso** usato in **Odoo**.

---

## 2. Struttura interna (standard)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
03_PROGETTI
├── <CARTELLE_PROGETTO...>
└── 99_ARCHIVIO
```

Regole fondamentali:

- In `03_PROGETTI` si crea **una cartella per ciascun progetto**, tutte allo stesso livello.  
- Il **nome della cartella progetto** deve coincidere con il **nome del progetto in Odoo** (vedi §5).  
- `99_ARCHIVIO` contiene progetti chiusi/non attivi (spostati mantenendo nome e contenuto).

> Nota: non si eliminano cartelle progetto senza valutazione congiunta (Owner Progetto/PM + IT/Qualità).

---

## 3. Dove archiviare i file relativi a un progetto (regola generale)

### 3.1 Regola base
Tutti i documenti **operativi di delivery** (analisi, piani, meeting, deliverable, materiali tecnici di progetto, evidenze di collaudo, ecc.) devono essere archiviati **nella cartella del progetto** in:

`ORG-XXX_NomeOrganizzazione/03_PROGETTI/<NOME_PROGETTO_ODOO>/...`

### 3.2 Eccezioni (documenti che NON vivono in 03_PROGETTI)
Per evitare duplicazioni e conflitti di “fonte di verità”:

- **Offerte / presales / proposte commerciali** → `02_COMMERCIALE`  
  (in `03_PROGETTI` si può mettere un link in `09_LINK_RIFERIMENTI`, vedi §6.10)

- **Contratti firmati, NDA, DPA e documentazione legale “di pratica”** → `08_LEGALE_COMPLIANCE`  
  (in `03_PROGETTI` si mantiene copia solo se autorizzato e necessario operativamente; preferire link)

- **Fatture, riconciliazioni, documenti amministrativi/finanziari** → `07_AMMINISTRAZIONE_FINANZA`  
  (in `03_PROGETTI` al massimo link o estratto operativo non contabile)

- **Template e asset “master”** → `12_TEMPLATE_E_BRAND`  
  (nel progetto si salvano solo gli output derivati)

- **Policy/incident/audit security e evidenze di sicurezza** → `11_SICUREZZA`  
  (nel progetto solo ciò che è strettamente “delivery” e consentito)

---

## 4. Cosa deve stare in PROGETTI (e cosa no)

### 4.1 Deve stare in `03_PROGETTI`
Esempi (non esaustivi):

- documenti di avvio: kickoff, scope operativo, charter, stakeholder map (se usati);
- pianificazione: WBS, Gantt, roadmap, piani di rilascio, risk log operativo;
- requisiti e analisi: raccolta requisiti, specifiche funzionali/tecniche di progetto, verbali analisi;
- meeting e comunicazioni operative: minute, report avanzamento, decision log;
- materiali di delivery: deliverable, report, manuali specifici di progetto, presentazioni di progetto;
- collaudi/QA: test plan, UAT, evidenze, report bug (se non gestiti in tool dedicati);
- dati/asset di progetto: export, dataset consegnati, materiali cliente, allegati tecnici;
- operazioni di rilascio: checklist deployment, note di rilascio, configurazioni operative specifiche (se non IT runbook generali).

### 4.2 Non deve stare in `03_PROGETTI`
- documentazione “master” non specifica del progetto (template, brand, asset istituzionali) → `12_TEMPLATE_E_BRAND`;
- procedure IT generali (runbook infrastruttura, policy operative IT non specifiche) → `10_IT_OPERATIONS`;
- documentazione commerciale di opportunità (prima della firma/avvio) → `02_COMMERCIALE`;
- contratti firmati/NDA/DPA come fonte di verità → `08_LEGALE_COMPLIANCE`;
- fatture/documenti contabili come fonte di verità → `07_AMMINISTRAZIONE_FINANZA`.

---

## 5. Naming convention cartelle progetto (obbligatorio)

### 5.1 Regola obbligatoria
La cartella progetto in `03_PROGETTI` deve avere **esattamente** il **nome del progetto in Odoo**:

`03_PROGETTI/<NOME_PROGETTO_ODOO>`

Esempi:
- `03_PROGETTI/ACME - Fleet Tracking 2026`
- `03_PROGETTI/Versalis - Digital Twin Pilot`
- `03_PROGETTI/Interno - Knowledge Base Revamp`

### 5.2 Unicità e stabilità del nome
- Il nome deve essere **univoco** (se in Odoo esistono omonimie, va risolto in Odoo, es. aggiungendo anno/codice).  
- Evitare rinomine manuali in Drive: la rinomina si fa **prima in Odoo** e poi si allinea il Drive secondo processo concordato (IT/Owner).

---

## 6. Struttura interna della singola cartella progetto (standard)

All’interno di ogni cartella progetto (es. `03_PROGETTI/Versalis - Digital Twin Pilot`) la struttura consigliata è:

```
<NOME_PROGETTO_ODOO>
├── 00_ADMIN_E_GOVERNANCE
├── 01_PIANIFICAZIONE_E_CONTROLLO
├── 02_ANALISI_E_REQUISITI
├── 03_TECNICO_E_SVILUPPO
├── 04_DELIVERABLE_E_CONSEGNE
├── 05_MEETING_E_COMUNICAZIONI
├── 06_TEST_COLLAUDI_EVIDENZE
├── 07_DATI_E_ALLEGATI
├── 08_RILASCI_E_DEPLOYMENT
├── 09_LINK_RIFERIMENTI
└── 99_ARCHIVIO
```

### 6.1 00_ADMIN_E_GOVERNANCE
Contenuti tipici:
- kickoff pack, charter, scope operativo, stakeholder;
- decision log alto livello, registro rischi (se non in tool dedicati);
- documenti di “governo” del progetto.

### 6.2 01_PIANIFICAZIONE_E_CONTROLLO
Contenuti tipici:
- piani di lavoro, roadmap, WBS, Gantt, baseline;
- report avanzamento, SAL, timesheet export (se usato operativamente);
- planning sprint (se non nel tool di gestione).

### 6.3 02_ANALISI_E_REQUISITI
Contenuti tipici:
- requisiti, workshop notes, verbali analisi;
- specifiche funzionali di progetto;
- backlog export (se serve per consegna/archivio).

### 6.4 03_TECNICO_E_SVILUPPO
Contenuti tipici:
- architetture di progetto, specifiche tecniche;
- documenti di integrazione, configurazioni specifiche di progetto (non IT generali);
- note tecniche e manuali “interni” di progetto.

> Nota: codice sorgente e documentazione “as-code” rimangono nei repo (GitHub/GitLab). Qui si archivia solo ciò che è necessario come documentazione di progetto o consegna.

### 6.5 04_DELIVERABLE_E_CONSEGNE
Contenuti tipici:
- deliverable ufficiali (report, documenti, presentazioni, manuali consegnati);
- pacchetti consegna, versioni finali;
- materiale cliente “finale”.

### 6.6 05_MEETING_E_COMUNICAZIONI
Contenuti tipici:
- verbali, minute, note meeting;
- comunicazioni operative rilevanti (estratti email se necessario, preferire link);
- decision log operativo.

### 6.7 06_TEST_COLLAUDI_EVIDENZE
Contenuti tipici:
- piani di test, UAT, evidenze collaudo, report bug (export);
- checklist qualità/done criteria specifici.

### 6.8 07_DATI_E_ALLEGATI
Contenuti tipici:
- export, dataset, allegati ricevuti dal cliente, file di lavoro;
- immagini, tracciati, materiali tecnici non strutturati.

> Attenzione: dati personali o sensibili vanno gestiti secondo GDPR/policy e con permessi adeguati.

### 6.9 08_RILASCI_E_DEPLOYMENT
Contenuti tipici:
- note di rilascio, checklist deployment, piani di migrazione specifici;
- configurazioni di rilascio (solo se autorizzato; segreti/credenziali non vanno mai in Drive).

### 6.10 09_LINK_RIFERIMENTI
File `.md`/`.txt` con link a:
- cartella opportunità/offerta in `02_COMMERCIALE` (se esiste);
- contratti firmati in `08_LEGALE_COMPLIANCE` (fonte di verità);
- documenti amministrativi in `07_AMMINISTRAZIONE_FINANZA` (se pertinenti);
- repository GitHub/GitLab, board, ticketing, ambienti, KB Odoo.

### 6.11 99_ARCHIVIO
Materiale superato/obsoleto, versioni non più valide, o contenuti da conservare ma non “operativi”.

---

## 7. Naming convention dei file di progetto

### 7.1 Regola generale (consigliata)
`YYYY-MM-DD__AREA__OGGETTO__STATO__vX.ext`

Dove:
- **AREA**: es. `PLAN`, `REQ`, `TECH`, `MEET`, `DELIV`, `TEST`, `REL`, `DATA`
- **STATO**: `DRAFT`, `FINAL`, `IN-REVIEW` (o vuoto se non serve)
- **vX**: versione (`v1`, `v2`, `v1.0`, …) quando utile

Esempi:
- `2025-12-23__MEET__Kickoff__FINAL__v1.docx`
- `2026-01-10__REQ__Requisiti_Funzionali__IN-REVIEW__v2.docx`
- `2026-02-05__DELIV__Report_Avanzamento_SAL1__FINAL__v1.0.pdf`
- `2026-02-20__REL__Release_Notes_R1__FINAL__v1.md`

### 7.2 Deliverable ufficiali (consigliato)
Per i deliverable consegnati al cliente, formato suggerito:

`DELIV__<NomeDeliverable>__<Versione>__YYYY-MM-DD.ext`

Esempi:
- `DELIV__Manuale_Utente__v1.0__2026-03-01.pdf`
- `DELIV__Report_Test_UAT__v1.1__2026-03-15.pdf`

### 7.3 Verbali meeting (consigliato)
`YYYY-MM-DD__MEET__<Titolo>__vX.ext`

Esempi:
- `2026-02-12__MEET__Allineamento_Tecnico__v1.docx`

---

## 8. Regole operative (sintetiche)

### 8.1 Creazione cartella progetto
Si crea quando il progetto è:
- creato/attivato in Odoo **e** passa in fase operativa (kickoff o avvio delivery).

**Responsabile primario:** PM/Owner progetto (o chi è assegnato in Odoo).  
**Responsabile di controllo:** Responsabile Area/PMO (ove presente) + IT per permessi.

### 8.2 Permessi (principi)
- Accesso al progetto solo a chi è coinvolto (principio di “least privilege”).
- Contenuti sensibili (dati personali, documenti riservati) richiedono permessi dedicati secondo policy.

### 8.3 Chiusura e archiviazione
Alla chiusura progetto:
- consolidare deliverable finali in `04_DELIVERABLE_E_CONSEGNE`;
- spostare la cartella progetto in `03_PROGETTI/99_ARCHIVIO` mantenendo il nome;
- garantire che i link in `09_LINK_RIFERIMENTI` restino validi.

---

## 9. Collegamenti e coerenza con altri allegati

- `01_ANAGRAFICHE` → Allegato SOP-DOC-03-A01 (cartelle soggetti e riferimenti)
- `02_COMMERCIALE` → Allegato SOP-DOC-03-A02 (offerte/opportunità/presales)
- `07_AMMINISTRAZIONE_FINANZA` → Allegato SOP-DOC-03-A07 (documenti admin/finanza)
- `08_LEGALE_COMPLIANCE` → Allegato SOP-DOC-03-A08 (contratti firmati e documenti legali)
- `10_IT_OPERATIONS` → Allegato SOP-DOC-03-A10 (runbook e procedure IT generali)
- `11_SICUREZZA` → Allegato SOP-DOC-03-A11 (policy, audit, incident security)
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12 (template e asset master)

---

## 10. Note di sicurezza (obbligatorie)

- **Credenziali, token, chiavi, segreti**: non devono mai essere salvati in Drive.  
- Dati personali/sensibili: gestire secondo GDPR e policy interne; usare permessi restrittivi e minimizzazione.  
- Documenti contrattuali firmati: fonte di verità in `08_LEGALE_COMPLIANCE`, non duplicare senza necessità.
