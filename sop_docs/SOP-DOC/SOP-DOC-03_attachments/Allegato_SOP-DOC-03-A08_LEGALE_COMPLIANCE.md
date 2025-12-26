# Allegato SOP-DOC-03-A08 – LEGALE_COMPLIANCE (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A08  
- **Titolo:** LEGALE_COMPLIANCE – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `08_LEGALE_COMPLIANCE` contiene la documentazione **legale e di compliance “di pratica”** dell’organizzazione, ovvero documenti **vincolanti**, **firmati**, **ufficiali** o **di evidenza** (audit/adempimenti), e serve a:

- garantire **conservazione ordinata**, reperibilità e tracciabilità della documentazione legale;
- ridurre dispersione e duplicazioni (es. contratti sparsi in Commerciale/Progetti);
- supportare audit interni/esterni (es. evidenze GDPR contrattuali, procure, deleghe, accordi quadro);
- applicare controlli di **riservatezza** e permessi coerenti (need-to-know).

**Principio chiave:** in `08_LEGALE_COMPLIANCE` si archiviano **documenti reali e/o firmati** e relative evidenze.  
I **template master** (NDA/contratti/DPA in bianco, fac-simile, modelli) **non** risiedono qui ma in `12_TEMPLATE_E_BRAND`.

---

## 2. Struttura interna (standard)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
08_LEGALE_COMPLIANCE
├── 01_CONTRATTI_E_ORDINI_FIRMATI
│   └── <CONTROPARTE>/
├── 02_NDA_FIRMATI
│   └── <CONTROPARTE>/
├── 03_PRIVACY_GDPR_DPA
│   └── <CONTROPARTE>/
├── 04_AUDIT_E_EVIDENZE_COMPLIANCE
│   ├── 01_AUDIT
│   ├── 02_EVIDENZE
│   └── 03_CORRISPONDENZA_UFFICIALE
├── 05_PROCURE_DELEGHE_POTERI
└── 99_ARCHIVIO
```

**Regola fondamentale:** per i rami **01–03** si crea **una sottocartella per ciascuna controparte** (`<CONTROPARTE>`) usando lo **stesso naming** della cartella anagrafica in `01_ANAGRAFICHE` (vedi §5.1).

> Nota: `99_ARCHIVIO` contiene documenti non più attivi (es. contratti scaduti/risolti) o superati.  
> Non si eliminano documenti legali senza valutazione congiunta (Owner Legale/Compliance + Direzione, se applicabile).

---

## 3. Cosa deve stare in LEGALE_COMPLIANCE (e cosa no)

### 3.1 Deve stare in `08_LEGALE_COMPLIANCE`

Esempi di contenuti ammessi:

- **Contratti/accordi firmati** con clienti/fornitori/partner (accordi quadro, contratti di servizio, ordini firmati, SOW firmati);
- **NDA firmati** (mutual/unilateral) e relative versioni firmate;
- **DPA / Accordi privacy** (es. DPA, SCC, clausole GDPR firmate, addendum privacy);
- **Procure / deleghe / poteri** e documentazione societaria funzionale alla firma (limitatamente a ciò che serve operativamente);
- **Evidenze di compliance legale** (es. audit legali, evidenze di adempimenti, corrispondenza ufficiale vincolante, verbali/approvazioni formali).

### 3.2 Non deve stare in `08_LEGALE_COMPLIANCE`

- **Template master** (in bianco) di contratti, NDA, DPA, lettere → `12_TEMPLATE_E_BRAND`;
- Documenti di **opportunità/presales** (bozze offerta, proposte, presentazioni) → `02_COMMERCIALE`;
- Documentazione operativa di **progetto** (deliverable, piani, verbali delivery) → `03_PROGETTI`;
- Documentazione amministrativa **ricorrente** (fatture, riconciliazioni, estratti) → `07_AMMINISTRAZIONE_FINANZA`;
- Documentazione **security/compliance security** (policy sicurezza, controlli, incident, audit security) → `11_SICUREZZA`;
- Visure e documenti “anagrafici” di base (se non strettamente legali/firmatari) → `01_ANAGRAFICHE`.

**Regola anti-duplicazione:** se un documento vive in `08_LEGALE_COMPLIANCE`, altrove si usa al massimo **link/riferimento** (vedi §7.3), non copie multiple.

---

## 4. Regole operative (sintetiche)

### 4.1 Creazione e gestione cartelle controparte
- La cartella `<CONTROPARTE>` viene creata quando esiste almeno **un documento firmato** o una evidenza legale associata.
- La cartella `<CONTROPARTE>` deve essere coerente con l’anagrafica in Odoo e con la cartella in `01_ANAGRAFICHE`.

### 4.2 Documenti “definitivi”
- In `08_LEGALE_COMPLIANCE` si archivia **solo** la versione **finale** e, quando applicabile, **firmata**.
- Le bozze e negoziazioni (se conservate) devono avere uno spazio dedicato **fuori** da `08_LEGALE_COMPLIANCE` (es. in `02_COMMERCIALE` o in workspace di lavoro), salvo esigenze specifiche definite da Owner Legale/Compliance.

### 4.3 Permessi e riservatezza (minimo indispensabile)
- Accesso limitato secondo principio **need-to-know**.
- Permessi consigliati:
  - **Direzione**: accesso completo (ove richiesto).
  - **Owner Legale/Compliance**: pieno controllo e responsabilità di governo.
  - **Amministrazione**: accesso ai documenti necessari (es. contratti per fatturazione), preferibilmente **in sola lettura**.
  - **PM/Commerciale**: accesso ai documenti necessari al delivery/presales (preferibilmente via **link** e non tramite copia).
- Eventuali cartelle/contratti “sensibili” possono avere permessi più restrittivi.

### 4.4 Archiviazione e ciclo di vita
- Contratti scaduti/cessati: spostare in `99_ARCHIVIO` mantenendo naming e riferimenti.
- Non si cancellano documenti legali senza indicazione esplicita dell’Owner Legale/Compliance e/o policy di conservazione applicabile.

### 4.5 Indicizzazione minima (consigliata)
Per ogni controparte è consigliato mantenere un file indice:
- `INDEX__<CONTROPARTE>.md` (o `.txt`) con:
  - elenco contratti/NDA/DPA principali,
  - riferimenti a progetti Odoo correlati,
  - eventuali note su scadenze/rinnovi (senza dati sensibili non necessari).

---

## 5. Naming convention (cartelle e file)

### 5.1 Naming cartella controparte (obbligatorio)
La cartella `<CONTROPARTE>` deve utilizzare lo stesso standard dell’anagrafica (Allegato SOP-DOC-03-A01):

`<TIPO>-<CODICE>_<NOME_CONTROPARTE>`

Dove:
- **TIPO** ∈ `{CLI, FOR, PAR, ENT}` (Cliente, Fornitore, Partner, Ente/Istituzione)  
- **CODICE** = codice univoco (preferibilmente **Codice/ID Odoo**; se non disponibile usare `NA` temporaneo e aggiornare)  
- **NOME_CONTROPARTE** = nome normalizzato (MAIUSCOLO, underscore `_`, senza caratteri speciali)

Esempi:
- `CLI-000123_ACME_SRL`
- `FOR-000045_BETA_TECH_SPA`
- `PAR-000077_GAMMA_PARTNERS`
- `ENT-NA_COMUNE_DI_ROMA`

### 5.2 Naming dei file (obbligatorio per documenti firmati)
Formato standard consigliato:

`YYYY-MM-DD__TIPODOC__<CONTROPARTE>__OGGETTO__ID__STATO.ext`

Dove:
- `YYYY-MM-DD` = data firma (o data versione finale)
- `TIPODOC` = tipo documento (vedi §5.3)
- `<CONTROPARTE>` = stringa breve coerente (es. `ACME_SRL`, oppure `CLI-000123_ACME_SRL` se utile)
- `OGGETTO` = oggetto sintetico (underscore, senza caratteri speciali)
- `ID` = identificativo (es. `CNTR-2025-014`, `ODOO-PRJ-00088`, `SOW-03`) se disponibile
- `STATO` ∈ `{SIGNED, EXECUTED, COUNTERSIGNED}` (o `FINAL` se non firmato ma definitivo per evidenze)

Esempi:
- `2025-11-15__CONTRATTO__CLI-000123_ACME_SRL__Servizi_IT__CNTR-2025-014__SIGNED.pdf`
- `2025-10-02__NDA__FOR-000045_BETA_TECH_SPA__Mutual__NDA-2025-009__COUNTERSIGNED.pdf`
- `2025-09-20__DPA__CLI-000123_ACME_SRL__Data_Processing__DPA-2025-003__SIGNED.pdf`

### 5.3 TIPODOC (valori suggeriti)
- `CONTRATTO`
- `ORDINE`
- `SOW`
- `NDA`
- `DPA`
- `SCC`
- `ADDENDUM`
- `PROCURA`
- `DELEGA`
- `AUDIT`
- `EVIDENZA`
- `CORRISPONDENZA`

---

## 6. Dove archiviare i file “relativi a un progetto” (regola pratica)

- I documenti **operativi di progetto** (analisi, piani, meeting, deliverable) vanno in:
  - `03_PROGETTI/<NomeProgettoOdoo>/...` (Allegato SOP-DOC-03-A03).
- I documenti **legali firmati** legati a quel progetto (SOW firmati, addendum contrattuali, NDA di progetto, DPA del cliente) vanno in:
  - `08_LEGALE_COMPLIANCE` nella cartella della **controparte**.

**Collegamento consigliato:**
- in `03_PROGETTI/<NomeProgettoOdoo>/` creare un file link (es. `LINKS_LEGALE.md`) che punti ai documenti firmati in `08_LEGALE_COMPLIANCE`;
- in `08_LEGALE_COMPLIANCE/.../<CONTROPARTE>/` indicare (in `INDEX__...`) il progetto Odoo correlato.

---

## 7. Link e riferimenti (anti-duplicazione)

### 7.1 Regola
Invece di duplicare PDF firmati in più cartelle:
- mantenere **una sola copia** in `08_LEGALE_COMPLIANCE`;
- usare link (Google Drive “Aggiungi collegamento”) o file `.md/.txt` con URL.

### 7.2 Dove mettere i link
- Progetti → `03_PROGETTI/<NomeProgettoOdoo>/LINKS_LEGALE.md`
- Commerciale (se utile) → `02_COMMERCIALE/.../LINKS_LEGALE.md`
- Anagrafiche → `01_ANAGRAFICHE/<Controparte>/04_LINK_RIFERIMENTI/LINKS__<Controparte>.md`

### 7.3 Contenuto minimo del file link
- titolo documento, data, tipo (NDA/Contratto/DPA)
- link al file in `08_LEGALE_COMPLIANCE`
- eventuale ID (contratto, progetto Odoo) e note essenziali (senza dati sensibili superflui)

---

## 8. Collegamenti e coerenza con altri allegati

- `01_ANAGRAFICHE` → Allegato SOP-DOC-03-A01 (naming controparte e dati anagrafici)
- `02_COMMERCIALE` → Allegato SOP-DOC-03-A02 (bozze e materiali presales; non firmati)
- `03_PROGETTI` → Allegato SOP-DOC-03-A03 (documentazione operativa di delivery)
- `07_AMMINISTRAZIONE_FINANZA` → Allegato SOP-DOC-03-A07 (fatturazione/amministrazione operativa)
- `11_SICUREZZA` → Allegato SOP-DOC-03-A11 (policy e audit security)
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12 (template master legali e documentali)

---
