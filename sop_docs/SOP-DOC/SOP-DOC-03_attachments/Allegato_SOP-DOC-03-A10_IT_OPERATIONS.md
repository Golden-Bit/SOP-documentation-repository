# Allegato SOP-DOC-03-A10 – IT_OPERATIONS (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A10  
- **Titolo:** IT_OPERATIONS – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `10_IT_OPERATIONS` raccoglie documentazione **operativa IT** (runbook, procedure tecniche, configurazioni operative, inventari, guide strumenti) per garantire:

- continuità operativa (knowledge trasferibile);
- standardizzazione e riduzione errori nelle attività ricorrenti;
- tracciabilità di cambi e configurazioni (a livello documentale, non sostitutivo del versioning del codice).

**Principio chiave:** qui vive l’operatività IT.  
Policy, audit, incident e documentazione security/privacy vivono in `11_SICUREZZA`.

---

## 2. Struttura interna (al momento arbitraria)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
10_IT_OPERATIONS
├── (struttura interna al momento ARBITRARIA: da definire in una revisione futura)
└── 99_ARCHIVIO
```

- La struttura interna (per sistemi, ambienti, piattaforme, runbook, inventario, ecc.) è **temporaneamente lasciata arbitraria**.
- **Obbligatorio** mantenere `99_ARCHIVIO` per procedure deprecate, sistemi dismessi, versioni precedenti.

---

## 3. Cosa deve stare qui (e cosa no)

### 3.1 Deve stare in `10_IT_OPERATIONS`
Esempi:
- runbook operativi (deploy, restore, routine manutentive);
- guide configurazione strumenti (workspace, account, integrazioni operative);
- inventari IT (asset, licenze, strumenti) se non gestiti altrove;
- procedure tecniche interne (backup operativi, gestione accessi operativa, provisioning).

### 3.2 Non deve stare in `10_IT_OPERATIONS`
- policy e audit security/privacy, incident report, controlli → `11_SICUREZZA`;
- documentazione ufficiale del software e codice → repository Git (SOP-DOC-02) quando applicabile;
- documenti HR (onboarding/offboarding) → `09_PEOPLE_HR` (con link verso procedure IT pertinenti);
- documenti legali (DPA, SCC, contratti IT) → `08_LEGALE_COMPLIANCE`.

---

## 4. Regole operative (sintetiche)

### 4.1 Fonte di verità e duplicazioni
- Se una procedura è parte del software/codice (README, docs-as-code), la fonte di verità è Git.
- In Drive tenere solo materiale operativo non adatto al repository (es. procedure interne non pubbliche, inventari).

### 4.2 Aggiornamenti e deprecazione
- Ogni runbook deve indicare:
  - owner (chi lo mantiene),
  - data ultima revisione,
  - pre-condizioni e rollback.
- Quando un runbook è superato: spostare in `99_ARCHIVIO` (non cancellare).

### 4.3 Permessi
- Accesso tipico: team IT (scrittura), altri ruoli (lettura) solo dove necessario.

---

## 5. Naming convention (consigliata)

Formato consigliato:

`YYYY-MM-DD__ITOPS__SISTEMA_O_AREA__OGGETTO__vX.Y.ext`

Esempi:
- `2025-11-03__ITOPS__Odoo__Backup_Restore__v1.1.md`
- `2025-10-10__ITOPS__GoogleWorkspace__Provisioning_Utente__v1.0.pdf`

---

## 6. Collegamenti e coerenza con altri allegati

- `11_SICUREZZA` → separazione tra operatività e sicurezza/compliance.
- `09_PEOPLE_HR` → onboarding/offboarding: link ai runbook e checklist IT.
- `05_FORMATIVO_LINEE_GUIDA` → guide “per tutti” (non tecniche) separate dai runbook IT.
- `SOP-DOC-02` → documentazione ufficiale/versionata in Git.

---
