# Documento di Progetto – Progetto Interno

---

## 0. Metadati di progetto

- **Codice progetto:** {{CODICE_PROGETTO}}
- **Titolo progetto:** {{TITOLO_PROGETTO}}
- **Tipo progetto:** Interno
- **Sponsor interno:** {{SPONSOR_INTERNO}}
- **Priorità strategica:** {{Alta / Media / Bassa}}
- **Stato progetto:** {{Iniziato / In corso / Chiuso / In attesa}}
- **Project Manager / Product Owner:** {{NOME_PM_PO}}
- **Scrum Master:** {{NOME_SCRUM_MASTER}}
- **Versione documento:** {{VERSIONE_DOC}}
- **Data:** {{DATA}}
- **Confidenzialità:** {{Uso interno}}

> **Esempio di compilazione**  
> - Codice progetto: PRJ-INT-2025-LOG-OPT  
> - Titolo progetto: Ottimizzazione processo di deployment interno  
> - Sponsor interno: CTO  
> - Priorità strategica: Alta

---

## 1. Contesto, motivazioni e obiettivi

### 1.1 Contesto e motivazione

_Descrivere il problema/opportunità interna che il progetto intende affrontare._

**Esempi di contenuti:**

- Problemi attuali (es. tempi lunghi di deploy, errori frequenti, attività manuali).
- Contesto organizzativo (es. crescita del numero di progetti, nuovi requisiti interni).
- Motivazioni strategiche (es. riduzione dei tempi di go-live, aumento qualità, riduzione costi operativi).

### 1.2 Obiettivi di alto livello

_Elencare gli obiettivi principali del progetto interno e i benefici attesi._

**Esempi:**

- Ridurre il tempo medio di deployment del 50%.
- Automatizzare il 70% delle attività manuali di rilascio.
- Standardizzare il processo di deploy su tutti i progetti.
- Migliorare la visibilità dello stato di release per il team.

---

## 2. Ambito (Scope) del progetto

### 2.1 In scope

_Elencare ciò che è incluso (processi, sistemi, moduli, team coinvolti)._

**Esempi:**

- Processo di deployment per progetti Python/NodeJS su infrastruttura esistente.
- Introduzione di pipeline CI/CD standard (GitLab CI).
- Definizione di linee guida di tagging/release.

### 2.2 Out of scope

_Elencare ciò che non è compreso nel progetto._

**Esempi:**

- Re-ingegnerizzazione completa dell’infrastruttura cloud.
- Migrazione di tutti i progetti legacy a nuove tecnologie.
- Cambiamenti radicali nei processi amministrativi/contabili.

---

## 3. Stakeholder e ruoli interni

- **Sponsor interno:** {{SPONSOR_INTERNO}}  
  _Esempio: CTO / Direzione Operativa._
- **Project Manager / Product Owner:** {{NOME_PM_PO}}
- **Scrum Master:** {{NOME_SCRUM_MASTER}}
- **Team di progetto:** {{NOMI_RISORSE}}  
  _Esempio: devops engineer, sviluppatori senior, referente QA._
- **Altre funzioni coinvolte:** {{ELENCO}}  
  _Esempio: Amministrazione (per impatti di processo), HR (per formazione), Marketing (se impatta su processi di release lato cliente)._

---

## 4. Setup Scrum e modalità di lavoro

### 4.1 Durata e calendario degli Sprint

- **Durata Sprint:** {{Durata Sprint, es. 2 settimane}}
- **Periodo previsto progetto:** {{Data inizio – Data fine (stimate)}}

**Esempio:**

- Durata Sprint: 2 settimane.
- Periodo previsto: 2025-02-01 → 2025-04-30.

### 4.2 Cerimonie Scrum

- **Daily:** {{frequenza e orario}}  
  _Esempio: 10 minuti ogni giorno h 10:00._
- **Sprint Planning:** {{modalità e durata}}  
  _Esempio: 1,5 ore con team completo._
- **Sprint Review:** {{modalità e durata}}  
  _Esempio: 1 ora con sponsor interno e team impattati._
- **Retrospective:** {{modalità e durata}}  
  _Esempio: 45 minuti, focus su cosa mantenere/migliorare._

### 4.3 Modalità di comunicazione interna

_Specificare canali e modalità operative._

**Esempi:**

- Canali: riunioni periodiche, strumenti di chat interni, ticket Odoo/GitLab.
- Documentazione delle decisioni su KB Odoo o note nella cartella di progetto su Drive.
- Sintesi di avanzamento condivisa periodicamente in una riunione di allineamento cross-team (se necessario).

---

## 5. Descrizione dell’intervento e backlog di alto livello

_Descrivere le principali EPIC / macro-user story interne._

**Esempi di EPIC:**

- EPIC-INT-01 – Definizione pipeline CI/CD standard.
- EPIC-INT-02 – Automazione dei test di regressione.
- EPIC-INT-03 – Introduzione sistema di monitoraggio post-deploy.
- EPIC-INT-04 – Formazione interna sui nuovi processi di release.

> I dettagli (Story e Task) sono gestiti nel backlog operativo su **Odoo Progetti** e **GitLab**.

---

## 6. Impatti attesi e metriche interne

_Descrivere gli impatti attesi e le metriche (KPI) che si intende monitorare._

**Esempi di impatti:**

- Riduzione dei tempi di rilascio.
- Diminuzione dei bug in produzione dopo il deploy.
- Maggiore standardizzazione dei processi tra i progetti.

**Esempi di KPI:**

- Tempo medio di deploy prima/dopo il progetto.
- Numero di rollback per release.
- Numero di passaggi manuali nel processo di distribuzione.
- Percentuale di progetti che adottano la nuova pipeline standard.

---

## 7. Piano di lavoro e milestone

### 7.1 Roadmap interna

_Elencare le fasi e le principali milestone._

**Esempio di tabella:**

| Milestone                            | Data stimata   | Descrizione                                           | Deliverable principale                        |
|--------------------------------------|----------------|-------------------------------------------------------|----------------------------------------------|
| M1 – Analisi stato attuale           | 2025-02-15     | Raccolta info sui processi di deploy esistenti       | Documento analisi AS-IS                      |
| M2 – Definizione pipeline standard   | 2025-03-01     | Definizione pipeline CI/CD target                    | Documento TO-BE + configurazione iniziale    |
| M3 – Pilot su 1–2 progetti           | 2025-03-31     | Applicazione pipeline standard a pochi progetti      | Pipeline operative su progetti pilota        |
| M4 – Estensione ad altri progetti    | 2025-04-30     | Roll-out graduale e formazione                       | Lista progetti migrati + materiale formativo |

### 7.2 Dipendenze e vincoli

_Elencare dipendenze interne e vincoli._

**Esempi:**

- Disponibilità team devops per la configurazione iniziale.
- Finestra di manutenzione condivisa con i team di sviluppo.
- Eventuale necessità di coordinamento con fornitori/partner esterni.

---

## 8. Rischi, assunzioni e mitigazioni

### 8.1 Rischi principali

**Esempi:**

- Rischio: resistenza al cambiamento da parte dei team.  
  - Impatto: Medio/Alto.  
  - Probabilità: Media.
- Rischio: sovraccarico del team devops durante la fase di rollout.  
  - Impatto: Alto.  
  - Probabilità: Media.

### 8.2 Assunzioni

**Esempi:**

- I team di sviluppo sono disponibili a collaborare alla definizione dei processi.
- Le attuali infrastrutture supportano le pipeline definite senza upgrade immediati.

### 8.3 Strategie di mitigazione

**Esempi:**

- Sessioni di formazione e comunicazione interna prima del rollout.
- Pianificazione del rollout in ondate, evitando di migrare troppi progetti in parallelo.
- Identificazione di “champion” interni per supportare l’adozione.

---

## 9. Riferimenti a sistemi, documenti e SOP

- Riferimento progetto Odoo: {{LINK_PROGETTO_ODOO}}
- Repository GitLab (se presente): {{LINK_GITLAB}}
- Repository GitHub (se presente): {{LINK_GITHUB}}
- Cartella Google Drive del progetto: {{LINK_CARTELLA_DRIVE}}
- Documentazione su GitHub Pages: {{LINK_GITHUB_PAGES}}
- Articolo Knowledge Base Odoo (se presente): {{LINK_KB_ODOO}}
- SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo
- SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)
- SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages
- SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo

> **Esempio:**  
> - Cartella Drive: `/Progetti_Interni/PRJ-INT-2025-LOG-OPT`  
> - Doc GitHub Pages: `/internal-projects/prj-int-2025-log-opt/`  

---

## 10. Allegati

_Elencare gli allegati effettivi e il loro contenuto._

**Esempi di allegati:**

- **Allegato A – Mappa processi AS-IS del deployment**  
  Contenuto: diagrammi di flusso dei processi di deploy attuali, con attori e strumenti utilizzati.
- **Allegato B – Disegno TO-BE pipeline CI/CD**  
  Contenuto: diagrammi delle pipeline target, step automatici, tool e responsabilità.
- **Allegato C – Linee guida operative per i team di sviluppo**  
  Contenuto: istruzioni per utilizzare la nuova pipeline, naming convenzioni, politiche di branch, regole per le merge request.
- **Allegato D – Piano di formazione interna**  
  Contenuto: calendario delle sessioni, materiali formativi (slide, link a video), destinatari.
- **Allegato E – Report di misurazione KPI pre/post progetto**  
  Contenuto: tabella comparativa dei KPI (tempi di deploy, rollback, errori) prima e dopo l’intervento.

> Indicare per ogni allegato il percorso su Drive o il link alla pagina GitHub Pages/KB in cui è archiviato.
