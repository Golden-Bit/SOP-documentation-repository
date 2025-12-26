# Allegato SOP-DOC-03-A00 – INBOX (regole, utilizzo, struttura e naming) – **senza sottocartelle**

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A00  
- **Titolo:** INBOX – Regole di utilizzo, struttura e naming (senza sottocartelle)  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `00_INBOX` è un’area **temporanea** di ingresso per documenti/file:

- ricevuti via email/chat o da terzi (clienti/fornitori/partner),
- creati rapidamente durante call/meeting,
- scaricati da portali, export, screenshot, registrazioni,
- che **non sono ancora stati classificati** nella macro-cartella corretta.

**Principio:** `00_INBOX` **non** è un archivio e **non** è una cartella di lavoro permanente.

---

## 2. Struttura interna (standard)

La cartella `00_INBOX` **non prevede sottocartelle**.

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
00_INBOX
```

Tutti i file “da smistare” vengono inseriti direttamente in `00_INBOX`.

---

## 3. Cosa deve stare in INBOX (e cosa no)

### 3.1 Deve stare in `00_INBOX`
- File “da smistare” per i quali non è chiara la destinazione finale.
- File che richiedono una verifica rapida prima di essere collocati (es. “è una bozza commerciale o un deliverable di progetto?”).
- Materiale grezzo di breve vita (export, note, screenshot) **finché** non viene associato a una destinazione certa, ad esempio:
  - anagrafica → `01_ANAGRAFICHE`
  - opportunità/presales → `02_COMMERCIALE`
  - progetto/commessa → `03_PROGETTI`
  - contenuti marketing operativi → `06_MARKETING_COMUNICAZIONE`
  - documenti admin/finanza → `07_AMMINISTRAZIONE_FINANZA`
  - documenti legali reali/firmati → `08_LEGALE_COMPLIANCE`
  - documentazione HR → `09_PEOPLE_HR`
  - runbook/procedure IT → `10_IT_OPERATIONS`
  - sicurezza/audit/policy security → `11_SICUREZZA`
  - template/asset master → `12_TEMPLATE_E_BRAND`

### 3.2 Non deve stare in `00_INBOX`
- Documenti definitivi o in uso ricorrente (devono stare nella macro-cartella corretta).
- Template e asset master (devono stare in `12_TEMPLATE_E_BRAND`).
- Contratti/NDA/DPA **firmati** o documenti legali “di pratica” (devono stare in `08_LEGALE_COMPLIANCE`).
- Documentazione di progetto in corso (deve stare in `03_PROGETTI`).
- Documenti amministrativi correnti (devono stare in `07_AMMINISTRAZIONE_FINANZA`).

---

## 4. Regole operative (sintetiche)

### 4.1 Tempo massimo di permanenza
- Un file può rimanere in `00_INBOX` per un massimo di **7 giorni**.
- Eccezioni fino a **14 giorni** solo se motivate (es. in attesa di informazioni minime per assegnazione corretta).

### 4.2 Responsabilità dello smistamento
- **Responsabile primario:** chi carica/crea il file in `00_INBOX` è responsabile di:
  - rinominare correttamente (vedi §5),
  - spostare nella cartella corretta entro i tempi.
- **Responsabile di controllo:** Responsabile di Area (o referente operativo) verifica periodicamente che `00_INBOX` non accumuli arretrato.

### 4.3 Svuotamento (cadenzamento minimo)
- `00_INBOX` va revisionata **almeno 1 volta a settimana**.
- Obiettivo: `00_INBOX` deve rimanere **quasi vuota** (solo flusso di ingresso, non deposito).

---

## 5. Naming convention dei file in INBOX

### 5.1 Regola generale
Finché un file è in `00_INBOX`, il nome deve permettere di capire **al volo**:
- *cosa è*, *chi/che cosa riguarda*, *quando è stato generato*, *qual è lo stato*.

**Formato consigliato:**
`YYYY-MM-DD__OGGETTO__RIFERIMENTO__STATO.ext`

Esempi:
- `2025-12-23__Call_note__Cliente-Rossi__TO-SORT.docx`
- `2025-12-23__Offerta_draft__Lead-Acme__WAITING-INFO.pptx`
- `2025-12-22__Screenshot__Bug-Login__TO-SORT.png`

### 5.2 RIFERIMENTO (se noto)
Usare uno dei seguenti, se applicabile:
- `Cliente-<Nome>` / `Fornitore-<Nome>` / `Partner-<Nome>`
- `Lead-<Nome>` / `Opp-<CodiceOdoo>` (se disponibile)
- `Progetto-<CodiceOdoo>` (se disponibile)
- `Interno-<Tema>`

### 5.3 STATO (valori standard)
Valori ammessi:
- `TO-SORT`
- `WAITING-INFO`
- `DUPLICATE` (da eliminare dopo verifica)
- `OBSOLETE` (superato/non più utile)

---

## 6. Regole di uscita da INBOX (criteri di smistamento)

Ogni file deve uscire da `00_INBOX` con **una** delle seguenti azioni:

1. **Spostamento** nella macro-cartella corretta (`01…12`) in base allo scopo e al contenuto.
2. **Eliminazione** se duplicato o non pertinente, dopo verifica minima.
3. **Rinominare e spostare** non appena si ottengono le informazioni mancanti (es. codice progetto/cliente/opportunità).

---

## 7. Collegamenti e coerenza con gli altri allegati

La struttura interna e le regole operative di destinazione finale sono definite negli allegati:
- `01_ANAGRAFICHE` → Allegato SOP-DOC-03-A01  
- `02_COMMERCIALE` → Allegato SOP-DOC-03-A02  
- `03_PROGETTI` → Allegato SOP-DOC-03-A03  
- `04_PRODOTTI_SERVIZI` → Allegato SOP-DOC-03-A04  
- `05_FORMATIVO_LINEE_GUIDA` → Allegato SOP-DOC-03-A05  
- `06_MARKETING_COMUNICAZIONE` → Allegato SOP-DOC-03-A06  
- `07_AMMINISTRAZIONE_FINANZA` → Allegato SOP-DOC-03-A07  
- `08_LEGALE_COMPLIANCE` → Allegato SOP-DOC-03-A08  
- `09_PEOPLE_HR` → Allegato SOP-DOC-03-A09  
- `10_IT_OPERATIONS` → Allegato SOP-DOC-03-A10  
- `11_SICUREZZA` → Allegato SOP-DOC-03-A11  
- `12_TEMPLATE_E_BRAND` → Allegato SOP-DOC-03-A12
