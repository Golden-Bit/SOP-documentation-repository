# Allegato SOP-DOC-03-A09 – PEOPLE_HR (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A09  
- **Titolo:** PEOPLE_HR – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `09_PEOPLE_HR` contiene documentazione **People/HR** necessaria alla gestione del personale e dei processi HR, con particolare attenzione a:

- **privacy** e riservatezza (dati personali, documenti sensibili);
- tracciabilità di onboarding/offboarding e formazione obbligatoria;
- reperibilità di policy HR, procedure interne, job description (ove applicabile).

**Principio chiave:** accesso rigorosamente **need-to-know** e gestione coerente con GDPR e policy interne.

---

## 2. Struttura interna (al momento arbitraria)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
09_PEOPLE_HR
├── (struttura interna al momento ARBITRARIA: da definire in una revisione futura)
└── 99_ARCHIVIO
```

- La struttura interna è **temporaneamente lasciata arbitraria** (es. per ruoli, processi, persone, periodi).
- **Obbligatorio** mantenere `99_ARCHIVIO` per documenti non più attivi (es. ex-dipendenti, procedure superate), nel rispetto delle policy di conservazione.

---

## 3. Cosa deve stare qui (e cosa no)

### 3.1 Deve stare in `09_PEOPLE_HR`
Esempi:
- onboarding/offboarding (checklist, consegne, asset consegnati/rientrati, account);
- policy e procedure HR interne (ferie, note spese, smart working, ecc.) se non pubblicate come SOP;
- documentazione su ruoli e organizzazione HR (job description, skill matrix) dove applicabile;
- formazione obbligatoria e attestazioni (ove previste);
- documentazione del personale **solo se prevista** e gestita con permessi adeguati (es. contratti di lavoro: valutare se qui o in area legale/archivio societario secondo policy).

### 3.2 Non deve stare in `09_PEOPLE_HR`
- contratti con clienti/fornitori, NDA, DPA e documentazione legale “di pratica” → `08_LEGALE_COMPLIANCE`;
- documentazione amministrativa contabile → `07_AMMINISTRAZIONE_FINANZA`;
- policy e audit security/privacy (incident, controlli) → `11_SICUREZZA`;
- template “master” (lettere standard, modelli) → `12_TEMPLATE_E_BRAND`;
- documentazione tecnica IT (runbook, configurazioni) → `10_IT_OPERATIONS`.

---

## 4. Regole operative (sintetiche)

### 4.1 Permessi (obbligatori)
- Accesso minimo consigliato:
  - **Owner HR/People**: pieno controllo;
  - **Direzione**: accesso secondo necessità;
  - **Amministrazione**: accesso solo se necessario e preferibilmente in sola lettura;
  - **Team/Line manager**: accesso limitato alle sole informazioni necessarie (es. onboarding checklist, non documenti personali).
- Evitare cartelle “aperte a tutti” se contengono dati personali.

### 4.2 Dati personali e minimizzazione
- Archiviare solo ciò che è necessario al processo e in linea con le policy.
- Evitare duplicazioni di documenti personali in altre aree: usare link controllati o riferimenti, se appropriato.

### 4.3 Ciclo di vita
- Alla cessazione del rapporto: spostare la documentazione non più attiva in `99_ARCHIVIO` (senza cancellare), seguendo regole di conservazione e accesso.

---

## 5. Naming convention (consigliata)

Formato consigliato:

`YYYY-MM-DD__HR__PROCESSO_O_TEMA__RIF__vX.Y.ext`

Esempi:
- `2025-08-01__HR__Onboarding__CHECKLIST__v1.0.xlsx`
- `2025-07-15__HR__Policy_SmartWorking__v2.0.pdf`

> Nota: se si includono file collegati a persone, evitare dati superflui nel nome file (privacy by design).

---

## 6. Collegamenti e coerenza con altri allegati

- `11_SICUREZZA` → privacy/security policy e controlli (non duplicare).
- `10_IT_OPERATIONS` → procedure IT operative (account, device) con link incrociati in onboarding.
- `12_TEMPLATE_E_BRAND` → template ufficiali (lettere, modelli) usati in HR.
- `08_LEGALE_COMPLIANCE` → documentazione legale vincolante (separazione e permessi).

---
