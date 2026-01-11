# Allegato 5 — Template ufficiale “Descrizione Progetto standardizzata” (Odoo > Progetto > Campo “Descrizione”)

## Scopo
Questo template standardizza la **Descrizione del Progetto** in Odoo per:
- rendere immediatamente comprensibili **contesto, obiettivi, scope**;
- definire chiaramente **setup Scrum**, governance e regole di qualità (DoD);
- centralizzare **link** a Drive, repository documentale, KB e documenti chiave;
- supportare onboarding rapido e audit/controlli.

## Utilizzo (come si usa)
1. **Copia/incolla** il template nel campo **Descrizione** del Progetto Odoo.
2. Compila i campi `{{...}}` con le informazioni reali del progetto.
3. Mantieni la struttura: puoi estendere, ma **non rimuovere** le sezioni minime.
4. Se viene usata la colonna **BLOCKED** nella board:
   - sposta in **BLOCKED** le card ferme per dipendenze/impedimenti;
   - traccia il motivo in: **Dipendenze** e/o **Note / rischi** nelle card;
   - nel progetto, tieni aggiornate le dipendenze critiche in §4.

---

## TEMPLATE (da clonare/incollare in Odoo)

~~~text
# Descrizione Progetto

## 1. Descrizione generale

- **Codice progetto:** {{CODICE_PROGETTO}}
- **Titolo progetto:** {{TITOLO_PROGETTO}}
- **Tipo progetto:** {{Esterno (Cliente) / Interno}}
- **Cliente / Sponsor interno:** {{NOME_CLIENTE_O_SPONSOR}}
- **Stato attuale:** {{Iniziato / In corso / In attesa / Chiuso}}

### 1.1 Contesto

{{Descrizione sintetica del contesto del cliente o dell’esigenza interna: problema/opportunità, scenario di partenza, sistemi/processi coinvolti.}}

### 1.2 Obiettivi di alto livello

- {{Obiettivo 1 (es. automatizzare il processo X)}}
- {{Obiettivo 2 (es. ridurre tempi di Y del 20%)}}
- {{Obiettivo 3 (es. introdurre nuova piattaforma / modulo)}}

### 1.3 Perimetro (Scope) ad alto livello

- **In scope:**  
  - {{Elemento / funzionalità / processo 1}}  
  - {{Elemento / funzionalità / processo 2}}  

- **Out of scope:**  
  - {{Elemento esplicitamente escluso 1}}  
  - {{Elemento esplicitamente escluso 2}}

---

## 2. Setup Scrum del progetto

> Informazioni **minime obbligatorie** per capire come è organizzato il lavoro.

- **Durata Sprint:** {{es. 2 settimane (lun–ven)}}
- **Periodo previsto progetto:** {{es. 2025-02 → 2025-07 (stimato)}}
- **Project Manager / Product Owner:** {{NOME_PM_PO}}
- **Scrum Master:** {{NOME_SCRUM_MASTER (se presente)}}
- **Team di sviluppo (core):** {{Lista sintetica nomi/ruoli principali}}

### 2.1 Cerimonie Scrum

- **Daily Scrum:**  
  - Frequenza: {{es. ogni giorno lavorativo}}  
  - Orario: {{es. 9:30–9:45}}  
  - Canale/Strumento: {{es. meet/link ricorrente, sala riunioni, ecc.}}

- **Sprint Planning:**  
  - Cadenza: {{es. all’inizio di ogni Sprint}}  
  - Durata indicativa: {{es. 1,5–2 ore}}  
  - Partecipanti: {{PM/PO, Dev Team, Scrum Master, eventuali stakeholder}}

- **Sprint Review:**  
  - Cadenza: {{es. a fine Sprint}}  
  - Modalità: {{demo al cliente / demo interna}}  
  - Output: {{verbale, checklist, decisioni su prossimi Sprint}}

- **Sprint Retrospective:**  
  - Cadenza: {{es. a fine Sprint, dopo la Review}}  
  - Focus: {{cosa è andato bene / cosa migliorare / esperimenti da provare}}

> Eventuali cerimonie aggiuntive (es. refinement dedicati) possono essere annotate qui:  
> **Altro:** {{eventuali meeting di refinement, allineamenti extra, cerimonie custom}}

### 2.2 Board Odoo: fasi e significato (OBBLIGATORIO)

- **BACKLOG**
  - Significato: elementi noti ma non ancora pronti/assegnati.
  - Regola ingresso: descrizione compilata; se tecnico indicare prossimo step (analisi/ticket/spike).

- **ASSIGNED**
  - Significato: pronto e assegnato (owner/team definito).
  - Prerequisiti: requisiti chiari, dipendenze note, priorità definita; se tecnico issue GitLab creata o da creare subito.

- **IN PROGRESS**
  - Significato: lavoro attivo in corso.
  - Regola: aggiornare note/blocchi; se tecnico tracciamento su GitLab (issue/MR/CI).

- **BLOCKED** (se presente nel board)
  - Significato: card **ferma** per impedimenti esterni o dipendenze.
  - Regola: indicare chiaramente **cosa blocca** e **azione/owner per sbloccare** in “Dipendenze” e/o “Note / rischi”.
  - Uscita: rimuovere impedimento → tornare in ASSIGNED o IN PROGRESS.

- **DONE**
  - Significato: completato e verificato.
  - Regola uscita: DoD rispettata; se tecnico issue chiusa + link MR/commit + doc/Drive aggiornati se necessario.

### 2.3 Definition of Done (DoD) di progetto (OBBLIGATORIO)

- [ ] Criteri di accettazione soddisfatti / validazione eseguita
- [ ] Evidenze presenti (note, screenshot, link, verbale, output)
- [ ] Documentazione aggiornata se impatta utenti/operatività
- [ ] (Se tecnico) Ticket GitLab chiuso + MR/commit collegati
- [ ] (Se tecnico) Test/CI OK oppure motivazione documentata

---

## 3. Riferimenti documentali e sistemi

> Qui vanno inseriti i link principali per trovare **subito** la documentazione di progetto.

### 3.1 Riferimenti su Odoo

- **Progetto Odoo (questo record):** {{LINK_A_QUESTO_PROGETTO_SE_UTILIZZATO_ALTROVE}}
- **Opportunità CRM correlata (se presente):** {{LINK_OPPORTUNITÀ_CRM}}

### 3.2 Cartelle e file

- **Cartella principale Google Drive (standard):**  
  - `{{NOME_CARTELLA_DRIVE}}`  
    - Esempio standard: `{{PRJ-EXT-2025-001 - Piattaforma Ordini B2B}}`  
  - Link: {{LINK_CARTELLA_DRIVE}}

- **Documenti chiave:**
  - Documento di Progetto (Esterno/Interno): {{LINK_DOC_PROGETTO}}
  - Eventuali specifiche principali (funzionali/tecniche): {{LINK_SPECIFICHE_PRINCIPALI}}
  - Verbali riunioni importanti (se raccolti in un unico file/cartella): {{LINK_VERBALI}}

### 3.3 Repository documentale e codice

- **Repository documentale di progetto (repo principale):**  
  - Nome repo (standard): `{{codice_progetto_minuscolo}}-docs`  
    - Esempio: `prj-ext-2025-001-docs`  
  - Link: {{LINK_REPO_DOCS}}

- **Repository di codice (se presenti):**
  - Backend / API: {{LINK_REPO_BACKEND (es. prj-ext-2025-001-api)}}  
  - Frontend / UI: {{LINK_REPO_FRONTEND}}  
  - Altri componenti: {{ALTRI_REPO_RILEVANTI}}

> Nota: la struttura interna dei repo di **codice** segue i SOP di sviluppo (SOP-DEV-01 / SOP-DEV-02);  
> la struttura del repo **documentale** seguirà il SOP dedicato (SOP-DOC-03).

### 3.4 Documentazione pubblicata

- **GitHub Pages – Documentazione di progetto:** {{LINK_GITHUB_PAGES_PROGETTO}}  
  (se esistente; può essere generata dal repo `*-docs`)

- **Articolo Knowledge Base Odoo:** {{LINK_ARTICOLO_KB}}  
  (es. articolo riassuntivo con overview del progetto e link rapidi)

- **Altri riferimenti:**  
  - {{Link ad eventuali tool esterni, board ausiliari, fogli condivisi, ecc.}}

---

## 4. Dipendenze e collegamenti con altri progetti

- **Progetti correlati in Odoo (card [PROJECT]):**
  - {{CODICE_PROGETTO_1 – breve descrizione relazione / dipendenza}}  
  - {{CODICE_PROGETTO_2 – breve descrizione relazione / dipendenza}}

- **Dipendenze critiche:**
  - Tecniche: {{es. dipendenza da rilascio ambiente X, modulo Y, API di terzi}}  
  - Organizzative: {{es. approvazione cliente, decisioni direzionali}}  
  - Altre: {{altre dipendenze rilevanti}}

---

## 5. Note operative e regole specifiche

- **Regole di comunicazione con il cliente / stakeholder interni:**
  - {{es. canale ufficiale per richieste, tempi di risposta attesi, referenti principali}}

- **Vincoli particolari:**
  - {{es. finestre di deploy, vincoli normativi, SLA, ecc.}}

- **Eccezioni rispetto al processo standard:**
  - {{Es. “per questo progetto non si applica la Review con il cliente ad ogni Sprint ma solo ogni N Sprint”}}

---

## 6. Storico aggiornamenti descrizione progetto (facoltativo ma consigliato)

> Breve log degli aggiornamenti alla **descrizione** (non del progetto in sé).

- **{{yyyy-mm-dd}} – {{NOME}} –** {{Aggiornamento iniziale descrizione progetto}}  
- **{{yyyy-mm-dd}} – {{NOME}} –** {{Aggiornata sezione Setup Scrum (durata Sprint, Daily, ecc.)}}  
- **{{yyyy-mm-dd}} – {{NOME}} –** {{Aggiornati link a Drive / repo / GitHub Pages / KB}}
~~~
