# Allegato SOP-DOC-03-A05 – FORMATIVO_LINEE_GUIDA (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A05  
- **Titolo:** FORMATIVO_LINEE_GUIDA – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `05_FORMATIVO_LINEE_GUIDA` raccoglie materiali **formativi** e **linee guida operative** utili al lavoro quotidiano (how-to, manuali interni, checklist, note operative, playbook), con l’obiettivo di:

- ridurre dipendenza da conoscenza “tribale” e facilitare onboarding;
- standardizzare procedure operative (anche quando non sono ancora formalizzate come SOP);
- mantenere un punto unico di riferimento per guide di utilizzo strumenti/processi.

**Principio chiave:** questa cartella contiene contenuti “operativi” e “didattici”.  
Quando un contenuto diventa **ufficiale, stabile e pubblicabile**, può essere candidato a pubblicazione secondo **SOP-DOC-02** (fonte di verità su GitHub Pages), lasciando in Drive eventuali materiali di lavoro.

---

## 2. Struttura interna (al momento arbitraria)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
05_FORMATIVO_LINEE_GUIDA
├── (struttura interna al momento ARBITRARIA: da definire in una revisione futura)
└── 99_ARCHIVIO
```

- La struttura interna (sottocartelle, tassonomia, eventuali categorie) **non è ancora standardizzata**.
- **Obbligatorio** mantenere `99_ARCHIVIO` per contenuti superati/deprecati, mantenuti per tracciabilità.

---

## 3. Cosa deve stare qui (e cosa no)

### 3.1 Deve stare in `05_FORMATIVO_LINEE_GUIDA`
Esempi:
- guide “how-to” su strumenti (Odoo, Drive, GitHub, strumenti interni);
- checklist operative (chiusura progetto, handover, kick-off, delivery);
- linee guida operative non ancora formalizzate in SOP (best practice, standard minimi);
- tutorial interni (slide, note, video-link, esempi);
- FAQ interne, vademecum, note di onboarding tecnico/operativo (non HR).

### 3.2 Non deve stare in `05_FORMATIVO_LINEE_GUIDA`
- SOP ufficiali “fonte di verità” e versionate → GitHub (SOP-DOC-02);
- documenti commerciali per opportunità/cliente → `02_COMMERCIALE`;
- documenti di progetto (deliverable, piani, verbali delivery) → `03_PROGETTI`;
- policy e contenuti security/compliance security → `11_SICUREZZA`;
- template “master” e asset ufficiali → `12_TEMPLATE_E_BRAND`;
- documentazione HR/personale o sensibile → `09_PEOPLE_HR`.

---

## 4. Regole operative (sintetiche)

### 4.1 Versioni e aggiornamenti
- Preferire file con **versione esplicita** e data (vedi §5).
- Quando un documento viene sostituito, spostare la versione precedente in `99_ARCHIVIO` (non cancellare).

### 4.2 Qualità minima del contenuto
Ogni guida dovrebbe includere:
- scopo e destinatari (chi deve usarla);
- prerequisiti (accessi, strumenti, ruoli);
- procedura “step-by-step” o checklist;
- riferimenti (link a record Odoo, SOP, template).

### 4.3 Link (anti-duplicazione)
Se una guida deve puntare a risorse “di verità” (SOP su GitHub, template master, documenti progetto), usare **link** e non copie.

---

## 5. Naming convention (consigliata)

### 5.1 File di guida / how-to
Formato consigliato:

`YYYY-MM-DD__GUIDA__ARGOMENTO__AUDIENCE__vX.Y.ext`

Esempi:
- `2025-12-01__GUIDA__Odoo_CRM_Pipeline__Commerciale__v1.0.md`
- `2025-11-20__GUIDA__Gestione_Drive_Link__Tutti__v0.9.pdf`

### 5.2 Checklist
Formato consigliato:

`YYYY-MM-DD__CHECKLIST__PROCESSO__vX.Y.ext`

Esempi:
- `2025-10-05__CHECKLIST__Chiusura_Progetto__v1.2.docx`

---

## 6. Collegamenti e coerenza con altri allegati

- `SOP-DOC-02` → pubblicazione documentazione ufficiale su GitHub Pages (fonte di verità).
- `12_TEMPLATE_E_BRAND` → template e asset ufficiali (da linkare, non duplicare).
- `03_PROGETTI` → per guide/procedure specifiche di progetto, usare link dal progetto alla guida e viceversa.
- `11_SICUREZZA` → separazione netta tra contenuti formativi generici e policy/incident/audit security.

---
