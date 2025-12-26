# Allegato SOP-DOC-03-A12 – TEMPLATE_E_BRAND (utilizzo, struttura interna e naming)

---

## 0. Metadati allegato

- **Codice allegato:** SOP-DOC-03-A12  
- **Titolo:** TEMPLATE_E_BRAND – Regole di utilizzo, struttura interna e naming  
- **Riferimento:** SOP-DOC-03 (Struttura generale Google Drive multi-organizzazione)  
- **Stato:** Bozza  
- **Applicabilità:** Valido per **ogni** cartella `ORG-XXX_NomeOrganizzazione`

---

## 1. Scopo

La cartella `12_TEMPLATE_E_BRAND` è la **libreria ufficiale** di:

- template documentali (offerte, report, verbali, presentazioni standard, intestazioni);
- template legali (NDA, contratti, DPA, lettere, procure) **in bianco**;
- asset grafici ufficiali (loghi, icone, immagini master, brand identity, linee guida);
- componenti “master” utili a garantire coerenza tra aree e ridurre duplicazioni.

**Principio chiave:** qui vivono solo i **master**.  
I documenti “operativi” derivati (es. una specifica offerta cliente, una creatività adattata, un contratto firmato) vivono nelle cartelle di competenza (`02_COMMERCIALE`, `06_MARKETING_COMUNICAZIONE`, `08_LEGALE_COMPLIANCE`, `03_PROGETTI`).

---

## 2. Struttura interna (al momento arbitraria)

All’interno di `ORG-XXX_NomeOrganizzazione`:

```
12_TEMPLATE_E_BRAND
├── (struttura interna al momento ARBITRARIA: da definire in una revisione futura)
└── 99_ARCHIVIO
```

- La tassonomia interna (template legali, template business, brand assets, ecc.) è **temporaneamente lasciata arbitraria**.
- **Obbligatorio** mantenere `99_ARCHIVIO` per versioni precedenti dei master (deprecati ma tracciabili).

---

## 3. Cosa deve stare qui (e cosa no)

### 3.1 Deve stare in `12_TEMPLATE_E_BRAND`
Esempi:
- template PPT/Doc “master” (corporate deck, offerta standard, report standard);
- template legali in bianco (NDA, contratti, DPA, addendum, lettere);
- linee guida di brand (tone of voice, identity, usage rules);
- loghi e asset master (formati ufficiali, vettoriali, sorgenti).

### 3.2 Non deve stare in `12_TEMPLATE_E_BRAND`
- offerte specifiche per cliente/opportunità → `02_COMMERCIALE`;
- documenti di progetto/commessa → `03_PROGETTI`;
- contratti/NDA/DPA **firmati** → `08_LEGALE_COMPLIANCE`;
- materiali marketing operativi di campagna → `06_MARKETING_COMUNICAZIONE`;
- policy e audit security sensibili → `11_SICUREZZA` (salvo modelli “master” non sensibili, se previsto).

---

## 4. Regole operative (sintetiche)

### 4.1 Governo dei master
- Ogni template/asset deve avere un **owner** (ruolo o persona) responsabile dell’aggiornamento.
- Le modifiche ai master devono essere tracciabili (versione + changelog minimo).

### 4.2 Versioning e deprecazione
- Il template “corrente” deve essere identificabile chiaramente (vedi naming).
- Versioni precedenti vanno in `99_ARCHIVIO` (non cancellare).

### 4.3 Anti-duplicazione
- È vietato creare “nuovi master” paralleli in altre cartelle.
- Le aree (Commerciale/Marketing/HR/IT/Legale) devono usare **solo** i master qui presenti, salvo eccezioni approvate.

---

## 5. Naming convention (consigliata)

### 5.1 Template documentali
Formato consigliato:

`TEMPLATE__CATEGORIA__NOME__vX.Y__STATO.ext`

Dove `STATO` ∈ `{DRAFT, APPROVATO, DEPRECATO}`.

Esempi:
- `TEMPLATE__COMMERCIALE__Offerta_Standard__v2.3__APPROVATO.pptx`
- `TEMPLATE__PMO__Verbale_Riunione__v1.1__APPROVATO.docx`

### 5.2 Template legali (in bianco)
Formato consigliato:

`TEMPLATE__LEGALE__TIPO__vX.Y__STATO.ext`

Esempi:
- `TEMPLATE__LEGALE__NDA_Mutual__v3.0__APPROVATO.docx`
- `TEMPLATE__LEGALE__DPA__v1.4__APPROVATO.docx`

### 5.3 Asset brand
Formato consigliato:

`BRAND__ASSET__NOME__vX.Y__STATO.ext`

Esempi:
- `BRAND__LOGO__Primary__v1.0__APPROVATO.svg`
- `BRAND__GUIDELINE__Brand_Identity__v2.0__APPROVATO.pdf`

---

## 6. Collegamenti e coerenza con altri allegati

- `02_COMMERCIALE` → usa i template master (offerte, deck) da qui; i deliverable per cliente restano in Commerciale.
- `06_MARKETING_COMUNICAZIONE` → usa asset master (loghi, guideline) da qui; output di campagna resta in Marketing.
- `08_LEGALE_COMPLIANCE` → separazione: qui template, lì documenti firmati.
- `05_FORMATIVO_LINEE_GUIDA` → può linkare a template e asset; non duplicare.
- `SOP-DOC-02` → se alcuni template “ufficiali” devono avere fonte di verità in Git (es. docs-as-code), va stabilito esplicitamente.

---
