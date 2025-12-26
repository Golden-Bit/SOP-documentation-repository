# Allegato SOP-DOC-03-A01 – ANAGRAFICHE (utilizzo, struttura interna e naming) – **senza cartelle per tipologia**

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A01  
- **Titolo:** ANAGRAFICHE – Regole di utilizzo, struttura interna e naming (senza cartelle per tipologia)  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `01_ANAGRAFICHE` contiene la documentazione associata ai **soggetti anagrafici** dell’organizzazione (aziende e persone) e serve a:

- mantenere un punto unico e coerente per **documenti “di identità/relazione”** (profilo, visure, dati amministrativi, referenti, comunicazioni base);
- garantire **allineamento** con le anagrafiche gestite in **Odoo** (contatti, aziende, indirizzi, referenti);
- evitare dispersione e duplicazioni tra aree (Commerciale, Progetti, Amministrazione, Legale).

**Principio:** `01_ANAGRAFICHE` ospita documenti “trasversali” legati al soggetto.  
I documenti **di opportunità**, **di progetto**, **amministrativi ricorrenti** e **legali firmati** risiedono nelle rispettive macro-cartelle (vedi §3.2).

---

## 2. Struttura interna (standard)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
01_ANAGRAFICHE
├── <CARTELLE_ANAGRAFICHE...>
└── 99_ARCHIVIO
```

Regole fondamentali:

- In `01_ANAGRAFICHE` si crea **una cartella per ciascuna anagrafica**, **tutte allo stesso livello** (nessuna suddivisione per tipologia tramite sottocartelle).
- La **tipologia** (cliente/fornitore/partner/ente) è indicata **nel nome della cartella anagrafica** tramite prefisso (vedi §5).
- `99_ARCHIVIO` contiene anagrafiche non più attive (es. clienti cessati, fornitori dismessi) mantenendo naming e contenuto.

> Nota: non si cancellano cartelle anagrafiche senza valutazione congiunta (Owner Area + IT/Qualità).

---

## 3. Cosa deve stare in ANAGRAFICHE (e cosa no)

### 3.1 Deve stare in `01_ANAGRAFICHE`
Esempi di contenuti ammessi (a livello di anagrafica):

- profilo anagrafico azienda/persona (dati generali, schede, presentazioni istituzionali ricevute);
- visure e documenti societari di base (ove pertinenti e autorizzati);
- documenti di onboarding del fornitore/partner (es. modulistica generale, certificazioni generiche);
- elenco referenti e contatti (o export/contatti condivisi), organigrammi del soggetto se forniti;
- comunicazioni “di relazione” non legate a una specifica offerta o a un progetto (es. lettere generiche, informative);
- documenti utili trasversali (es. coordinate logistiche generali, sedi, informazioni di accesso “non IT/security”).

### 3.2 Non deve stare in `01_ANAGRAFICHE`
- documenti di **opportunità/presales** (bozze offerta, presentazioni dedicate, proposte) → `02_COMMERCIALE`;
- documenti di **progetto/commessa** (deliverable, piani, verbali di progetto, meeting di delivery) → `03_PROGETTI`;
- documenti di **fatturazione/contabilità operativa** (fatture, estratti, riconciliazioni) → `07_AMMINISTRAZIONE_FINANZA`;
- documenti **legali firmati** e “di pratica” (contratti firmati, NDA firmati, DPA, audit legali) → `08_LEGALE_COMPLIANCE`;
- template “master” (contratti, offerte, loghi, brand) → `12_TEMPLATE_E_BRAND`;
- evidenze di sicurezza/compliance security → `11_SICUREZZA`.

**Regola anti-duplicazione:** se un documento vive in un’altra macro-cartella, in `01_ANAGRAFICHE` si inserisce al massimo un **link/riferimento** (vedi §7.3).

---

## 4. Regole operative (sintetiche)

### 4.1 Creazione cartella anagrafica
Si crea una cartella anagrafica quando:
- l’anagrafica viene creata/attivata in Odoo **e** esiste la necessità di archiviare documenti associati, **oppure**
- è richiesto un repository condiviso per referenti/documenti di base.

**Responsabile primario:** chi crea/gestisce l’anagrafica in Odoo (o referente assegnato).  
**Responsabile di controllo:** Owner Area (Commerciale/Procurement/PMO a seconda del caso).

### 4.2 Unicità
- Per ogni soggetto deve esistere **una sola** cartella anagrafica per organizzazione.
- Vietata la creazione di duplicati per varianti del nome (es. “ACME”, “ACME SRL”, “ACME S.r.l.”): si usa il naming standard (§5).

### 4.3 Spostamento in archivio
Quando un soggetto non è più attivo:
- la cartella viene spostata in `01_ANAGRAFICHE/99_ARCHIVIO`;
- naming e contenuto restano invariati;
- eventuali link da Commerciale/Progetti restano validi.

---

## 5. Naming convention delle cartelle anagrafiche

### 5.1 Naming cartella anagrafica (obbligatorio)
Formato standard:

`<TIPO>-<CODICE>_<NOME_ANAGRAFICA>`

Dove:
- **TIPO** ∈ `{CLI, FOR, PAR, ENT}` (Cliente, Fornitore, Partner, Ente/Istituzione)  
- **CODICE** = codice univoco (preferibilmente **Codice/ID Odoo** o codice interno); se non disponibile usare `NA` temporaneo e aggiornare appena possibile  
- **NOME_ANAGRAFICA** = nome normalizzato (MAIUSCOLO, underscore `_`, senza caratteri speciali)

Esempi:
- `CLI-000123_ACME_SRL`
- `FOR-000045_BETA_TECH_SPA`
- `PAR-000077_GAMMA_PARTNERS`
- `ENT-NA_COMUNE_DI_ROMA`

### 5.2 Regole di normalizzazione nome
- usare solo lettere/numeri/underscore (`_`);
- evitare punti, virgole, slash, parentesi, accenti;
- persone fisiche: `COLOMBO_MARIO` (Cognome_Nome).

### 5.3 Collocazione (senza cartelle per tipologia)
- Tutte le cartelle anagrafiche (CLI/FOR/PAR/ENT) risiedono **direttamente** in `01_ANAGRAFICHE`.
- Quando non attive, vengono spostate in `01_ANAGRAFICHE/99_ARCHIVIO` mantenendo il prefisso TIPO.

---

## 6. Struttura interna della singola anagrafica (standard)

All’interno di ogni cartella anagrafica (es. `CLI-000123_ACME_SRL`) la struttura consigliata è:

```
<ANAGRAFICA>
├── 01_PROFILO_E_DATI
├── 02_REFERENTI_E_CONTATTI
├── 03_DOCUMENTI_EVIDENZE
├── 04_LINK_RIFERIMENTI
└── 99_ARCHIVIO
```

Descrizione sintetica:
- **01_PROFILO_E_DATI:** schede azienda/persona, presentazioni istituzionali, visure/documenti societari generali (se pertinenti).
- **02_REFERENTI_E_CONTATTI:** file con contatti/referenti, organigrammi forniti, rubriche condivise, note di contatto.
- **03_DOCUMENTI_EVIDENZE:** certificazioni generiche, modulistica generale, documentazione “base” non legata a una singola opportunità/progetto.
- **04_LINK_RIFERIMENTI:** file `.md` o `.txt` con link a opportunità, progetti, contratti firmati, documentazione amministrativa (se applicabile).
- **99_ARCHIVIO:** materiale superato o versioni obsolete.

---

## 7. Naming convention dei file dentro ANAGRAFICHE

### 7.1 Regola generale (consigliata)
`YYYY-MM-DD__TIPODOC__DESCRIZIONE.ext`

Esempi:
- `2025-12-10__Visura__ACME_SRL.pdf`
- `2025-11-03__Company_Profile__ACME_SRL.pdf`
- `2025-12-01__Contatti__Referenti_Principali.xlsx`

### 7.2 Tipodoc (valori suggeriti)
`Visura`, `Company_Profile`, `Certificazione`, `Contatti`, `Organigramma`, `Modulo`, `Note`, `Altro`

### 7.3 Link e riferimenti (anti-duplicazione)
Per evitare duplicazioni, quando serve “puntare” a documenti che vivono altrove:
- creare un file in `04_LINK_RIFERIMENTI` (es. `LINKS__ACME_SRL.md`) con:
  - link alle cartelle opportunità (`02_COMMERCIALE`) e progetti (`03_PROGETTI`),
  - link ai contratti firmati (`08_LEGALE_COMPLIANCE`),
  - link a documenti amministrativi (`07_AMMINISTRAZIONE_FINANZA`) se necessario.

---

## 8. Collegamenti e coerenza con altri allegati

- `02_COMMERCIALE` → Allegato SOP-DOC-03-A02 (documenti di opportunità/offerte)
- `03_PROGETTI` → Allegato SOP-DOC-03-A03 (documenti di delivery/progetto)
- `07_AMMINISTRAZIONE_FINANZA` → Allegato SOP-DOC-03-A07 (fatturazione e amministrazione operativa)
- `08_LEGALE_COMPLIANCE` → Allegato SOP-DOC-03-A08 (contratti firmati e documenti legali)
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12 (template e asset master)
