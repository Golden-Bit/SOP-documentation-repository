# Allegato SOP-DOC-03-A11 – SICUREZZA (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A11  
- **Titolo:** SICUREZZA – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `11_SICUREZZA` contiene documentazione di **security, privacy e compliance security** (policy, controlli, audit, incident, evidenze), con l’obiettivo di:

- garantire tracciabilità di policy e controlli;
- conservare evidenze utili per audit e certificazioni;
- gestire incident e lesson learned in modo controllato;
- mantenere separati contenuti di sicurezza dall’operatività IT (che vive in `10_IT_OPERATIONS`).

**Principio chiave:** contenuti sensibili, accesso strettamente **need-to-know**.

---

## 2. Struttura interna (al momento arbitraria)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
11_SICUREZZA
├── (struttura interna al momento ARBITRARIA: da definire in una revisione futura)
└── 99_ARCHIVIO
```

- La struttura interna (policy, audit, risk, incident, evidenze, ecc.) è **temporaneamente lasciata arbitraria**.
- **Obbligatorio** mantenere `99_ARCHIVIO` per versioni superate, audit chiusi, incident storicizzati.

---

## 3. Cosa deve stare qui (e cosa no)

### 3.1 Deve stare in `11_SICUREZZA`
Esempi:
- policy sicurezza e privacy, standard interni, linee guida security;
- audit e report security, piani di remediation, evidenze di controllo;
- incident report, post-mortem, registri eventi (ove previsti);
- risk assessment e documenti di gestione rischio (se adottati).

### 3.2 Non deve stare in `11_SICUREZZA`
- runbook operativi IT, procedure tecniche, inventari → `10_IT_OPERATIONS`;
- contratti, DPA, SCC firmate (documentazione legale vincolante) → `08_LEGALE_COMPLIANCE`;
- documentazione commerciale/progetto → `02_COMMERCIALE` / `03_PROGETTI`;
- template “master” (modelli di policy, modelli documentali) se intesi come libreria ufficiale → `12_TEMPLATE_E_BRAND` (salvo casi in cui la policy “master” sia qui per riservatezza).

---

## 4. Regole operative (sintetiche)

### 4.1 Permessi (obbligatori)
- Accesso minimo consigliato:
  - **Owner Security/Privacy**: pieno controllo;
  - **Direzione**: accesso secondo necessità;
  - **IT**: accesso ai contenuti necessari (es. remediation), preferibilmente in lettura dove opportuno;
  - altri ruoli: solo accessi puntuali e temporanei, se necessario.

### 4.2 Controllo versioni e “stato”
- Ogni policy/report dovrebbe indicare:
  - versione,
  - data emissione/ultima revisione,
  - owner,
  - stato (BOZZA/APPROVATA/DEPRECATA).
- Versioni precedenti vanno in `99_ARCHIVIO`.

### 4.3 Incident e riservatezza
- Gli incident report devono essere trattati come documenti ad alta sensibilità.
- Evitare di condividere copie: usare link con permessi controllati.

---

## 5. Naming convention (consigliata)

Formato consigliato:

`YYYY-MM-DD__SEC__TIPO__OGGETTO__vX.Y__STATO.ext`

Esempi:
- `2025-11-30__SEC__POLICY__Access_Control__v1.0__APPROVATA.pdf`
- `2025-10-12__SEC__INCIDENT__Phishing__v1.0__FINAL.pdf`
- `2025-09-05__SEC__AUDIT__Cloud_Security__v2.1__FINAL.pdf`

---

## 6. Collegamenti e coerenza con altri allegati

- `10_IT_OPERATIONS` → procedure operative correlate a remediation (link, non duplicazione).
- `08_LEGALE_COMPLIANCE` → contrattualistica e documenti vincolanti (DPA/SCC/contratti).
- `09_PEOPLE_HR` → formazione obbligatoria e aspetti HR, con link a policy security quando serve.
- `SOP-DOC-02` → se alcune policy devono essere pubblicate/controllate in Git, definire la fonte di verità.

---
