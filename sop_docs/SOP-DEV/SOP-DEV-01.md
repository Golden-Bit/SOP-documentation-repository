# SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo

---

### 0. Metadati del documento

* **Codice SOP:** SOP-DEV-01
* **Titolo:** Utilizzo di GitLab per lo sviluppo collaborativo
* **Versione:** 0.1
* **Data di emissione:** 2025-11-16
* **Redatto da:** CTO / Responsabile Sviluppo
* **Verificato da (se applicabile):** Project Manager Progetti Interni
* **Approvato da:** CEO / Direzione Generale
* **Revisione successiva prevista:** 2026-05-16
* **Stato:** Bozza
* **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

### 1.1 Scopo

Il presente SOP definisce le **regole di utilizzo di GitLab** per lo sviluppo collaborativo del software, con particolare riferimento a:

* struttura e naming dei **repository GitLab**;
* gestione di **issue**, **branch**, **merge request (MR)** e **code review**;
* collegamento tra GitLab e **Odoo** (progetti, user story, task) per garantire **tracciabilità end-to-end**;
* impostazione e utilizzo delle **pipeline CI/CD**;
* modalità di **accesso ai repository privati** (sviluppatori e server);
* workflow di lavoro:

  * su **postazioni con interfaccia grafica** (IDE / client Git);
  * su **sistemi server/headless** (solo CLI, senza sviluppo diretto);
* regole minime di **qualità del codice** (lint, test automatici) e di **protezione dei branch principali**;
* gestione di base dei **collaboratori esterni** e della condivisione dei repository privati.

### 1.2 Campo di applicazione

Il SOP si applica a:

* tutti i **progetti di sviluppo software** gestiti dall’azienda (prodotti interni, progetti cliente, tool interni);
* tutti gli **sviluppatori, devops, tech lead, maintainer, PM/PO** che interagiscono con GitLab;
* tutti i **repository ospitati in GitLab** che:

  * sono collegati a progetti Odoo;
  * fanno parte del portafoglio prodotti o infrastruttura interna;
  * sono considerati asset di codice aziendale, privati o interni.

Sono esclusi:

* i repository pubblici e la pubblicazione su GitHub, regolati da **SOP-DEV-02**;
* gli aspetti di gestione documentale esterna (GitHub Pages), regolati da **SOP-DOC-02**;
* i dettagli di implementazione delle singole pipeline di progetto, definiti in:

  * file `.gitlab-ci.yml` dei progetti;
  * eventuali guide tecniche interne collegate.

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabile)

* *Da definire in caso di adozione di standard o policy formali (es. linee guida di sicurezza, standard di qualità, norme settoriali).*

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
  Contesto generale e integrazione tra Odoo, GitLab, GitHub, Google Drive, GitHub Pages.

* **SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo**
  Gestione di backlog, sprint, user story e task in Odoo e collegamento con le issue GitLab.

* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
  Gestione di documenti di progetto e materiale tecnico archiviato su Drive.

* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
  Pubblicazione di documentazione tecnica derivata dai repository.

* **SOP-MKT-01 – Immagine, comunicazione e gestione dei canali marketing**
  Rilevante quando il codice riguarda siti, landing, strumenti web a supporto del marketing.

* **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo**
  Rilevante per integrazioni o automazioni sviluppate in GitLab che coinvolgono il CRM.

* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**
  Creazione di articoli KB che referenziano repository e documenti tecnici.

* **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**
  Criteri di pubblicazione di codice verso l’esterno, gestione release pubbliche e versioning.

---

## 3. Definizioni, acronimi e abbreviazioni

* **Git** – Sistema di versionamento distribuito per la gestione del codice sorgente.
* **GitLab** – Piattaforma per hosting Git, issue tracking, MR, CI/CD e code review, utilizzata come strumento principale per lo sviluppo.
* **Repository (repo)** – Insieme versionato di file di progetto (codice, configurazioni, script, documentazione tecnica).
* **Issue** – Ticket GitLab che rappresenta una user story, un bug, una technical task o una improvement.
* **Branch** – Ramificazione del codice sorgente a partire da un commit, usata per sviluppo parallelo.
* **Merge Request (MR)** – Richiesta di integrazione di un branch in un altro (di norma verso `develop` o `main`) dopo review.
* **CI/CD (Continuous Integration / Continuous Delivery)** – Pipeline automatiche di build, test e (eventuale) deploy.
* **Main** – Branch principale stabile (in produzione o pronto per produzione).
* **Develop** – Branch di integrazione per lo sviluppo continuo (se previsto per il progetto).
* **Feature branch** – Branch dedicato a una singola funzionalità o issue (`feature/...`).
* **Bugfix / Hotfix branch** – Branch per correzioni di bug, in particolare urgenti su `main` (`bugfix/...`, `hotfix/...`).
* **Semantic Versioning (SemVer)** – Schema di versione `MAJOR.MINOR.PATCH`, approfondito in SOP-DEV-02 per i pacchetti pubblici.
* **Deploy key** – Chiave SSH associata a un singolo repository, usata tipicamente per accesso da server o runner CI.
* **PAT (Personal Access Token)** – Token personale per autenticazione HTTPS verso GitLab, alternativo all’uso di SSH key.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

Il SOP riguarda l’**Area Sviluppo Software**, in coordinamento con:

* **Progetti & Delivery**

  * Pianificazione backlog;
  * definizione user story e criteri di accettazione;
  * validazione delle funzionalità sviluppate.

* **DevOps / Infrastruttura**

  * Configurazione pipeline CI/CD condivise e di progetto;
  * gestione runner, ambienti, sicurezza e deploy.

* **Commerciale & Marketing**

  * Quando sono coinvolte funzionalità che impattano CRM, siti, landing, API esposte a clienti/partner.

Ogni progetto software rilevante deve avere:

* un **Progetto in Odoo** (SOP-PRJ-01);
* uno o più **repository GitLab** collegati.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

Legenda: **R = Responsible**, **A = Accountable**, **C = Consulted**, **I = Informed**

* **CTO / Responsabile Sviluppo**

  * **A**: definizione delle regole generali di utilizzo GitLab, branching model standard, policy di protezione branch.
  * **R**: approvazione delle eccezioni al modello standard (es. progetti con branching dedicato).
  * **C/I**: consultato per decisioni architetturali e modifiche significative (tooling, pipeline globali).

* **Tech Lead / Maintainer di progetto**

  * **R**: configurazione del repository (branch protetti, impostazioni MR, pipeline base).
  * **A**: qualità del codice e delle integrazioni nel repository di competenza.
  * **C**: con PM/PO per priorità e scoping delle issue.
  * **I**: aggiorna il team su eventuali regole/procedure specifiche di progetto.

* **Developer**

  * **R**: sviluppo di feature/bugfix su branch dedicati, rispetto convenzioni di commit, apertura MR, gestione feedback di review.
  * **C**: con Tech Lead per scelte tecniche e dubbi su implementazione.
  * **I**: informato sulle decisioni di progetto tramite issue, MR, documentazione.

* **DevOps Engineer**

  * **R**: definizione e manutenzione delle pipeline CI/CD condivise; supporto ai team per pipeline custom.
  * **C**: con Tech Lead e CTO per politiche di deploy, sicurezza, risorse.
  * **I**: informato sui cambiamenti che impattano le pipeline e gli ambienti.

* **Project Manager / Product Owner**

  * **R**: collegamento tra Odoo (user story, task) e issue GitLab (SOP-PRJ-01); monitoraggio avanzamento.
  * **C**: con Tech Lead su priorità e pianificazione.
  * **I**: aggiornato sulle MR critiche e sulle release principali.

*(Una matrice RACI dettagliata può essere allegata al presente SOP.)*

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il processo di utilizzo di GitLab per lo sviluppo collaborativo copre:

1. **Creazione e configurazione dei repository**
   naming, visibilità, branch principali, protezioni, README, collegamenti a Odoo.

2. **Gestione delle issue**
   apertura, categorizzazione, assegnazione, link con user story/task Odoo.

3. **Gestione dei branch**
   creazione da `develop`/`main`, naming convention, durata, aggiornamento periodico.

4. **Merge Request (MR) e code review**
   apertura MR, regole di reviewer, vincoli CI, criteri di accettazione.

5. **CI/CD**
   configurazione `.gitlab-ci.yml`, stage minimi (lint, test, build, deploy), policy per branch protetti.

6. **Collegamento con Odoo**
   link incrociati tra issue/MR e user story/task; aggiornamento stati in Odoo.

7. **Manutenzione del repository**
   pulizia branch, gestione tag/versioni, individuazione refactoring, allineamento a SOP-DEV-02.

8. **Modalità di accesso ai repository privati**
   developer (SSH/PAT), server (deploy key/utente tecnico), divieti di condivisione credenziali.

9. **Workflow per postazioni con UI grafica**
   flusso standard di clone → branch → commit → push → MR via IDE/client Git.

10. **Workflow per sistemi server/headless**
    regole su clone/pull, divieto di sviluppo/commit sui server.

11. **Gestione collaboratori esterni e condivisione repo privati**
    ruoli GitLab, limiti di visibilità, revoca accessi.

---

### 5.2 Flusso operativo di alto livello

1. **Creazione del repository di progetto**

   * Il Tech Lead (o figura designata) crea un nuovo repository GitLab con naming standard:

     * `{{cliente}}-{{progetto}}-{{componente}}`
       es. `acme-portal-web`, `internal-llm-platform-backend`.

   * Vengono creati/validati i branch principali:

     * `main` – branch di produzione (sempre stabile);
     * `develop` – branch di integrazione (nei progetti che lo richiedono).

   * `main` (e, se usato, `develop`) vengono impostati come **branch protetti**:

     * nessun push diretto;
     * merge consentito **solo via MR approvate** e **pipeline CI verde**.

   * Nel `README.md` del repo devono essere indicati almeno:

     * descrizione sintetica del progetto;
     * link al Progetto Odoo corrispondente;
     * eventuali regole specifiche di quel repo (es. varianti al branching model standard).

2. **Gestione delle issue**

   * Ogni user story/task in Odoo (SOP-PRJ-01) che richiede sviluppo deve avere un’**issue GitLab** collegata (o viceversa un chiaro link incrociato).

   * Convenzione consigliata per il titolo issue:

     * `[ODOO-<ID>] Breve descrizione`
       es. `[ODOO-123] Implementare endpoint login SSO`.

   * Ogni issue deve includere:

     * link alla user story/task in Odoo;
     * label tipo (es. `feature`, `bug`, `refactor`, `spike`, `docs`);
     * label ambito (es. `backend`, `frontend`, `devops`);
     * assegnatario (Developer responsabile);
     * criteri di accettazione (direttamente o tramite link a Odoo).

3. **Branching per feature, bugfix e hotfix**

   * Ogni attività di sviluppo avviene su **branch dedicati**, creati da `develop` (o da `main` se il progetto non usa `develop`):

     * `feature/ODOO-123-nome-breve-feature`
     * `bugfix/ODOO-456-fix-descrittivo`
     * `hotfix/ODOO-789-fix-produzione-critico`

   * Regole di base:

     * un branch si riferisce idealmente a **una sola issue** (o gruppo molto correlato);
     * durata di vita breve (preferibilmente ≤ durata di uno sprint);
     * aggiornamento periodico da `develop`/`main` (pull/rebase) per ridurre conflitti.

4. **Commit e convenzioni di messaggio**

   * I messaggi di commit devono essere **chiari e significativi**, evitando generici “fix”, “changes”, “update”.

   * È raccomandato includere l’ID issue, ad es.:

     * `feat: add login endpoint [#123]`
     * `fix: handle null customer id [#456]`

   * Commit frequenti e atomici sono preferiti rispetto a commit monolitici poco leggibili.

5. **Merge Request (MR) e code review**

   * L’integrazione verso `develop` o `main` avviene **solo tramite MR**:

     * titolo MR coerente con l’attività (es. `Implement login endpoint [ODOO-123]`);
     * descrizione con:

       * sintesi dei cambi;
       * riferimenti a issue GitLab / story Odoo;
       * eventuali note su breaking change, migrazioni, configurazioni.

   * Regole minime:

     * almeno **1 reviewer** diverso dall’autore del branch;
     * **pipeline CI verde** (lint + test obbligatori) prima del merge;
     * niente merge con pipeline fallita o senza review.

   * L’approvazione MR implica che:

     * il codice rispetta le convenzioni del progetto;
     * sono presenti test minimi (dove applicabile);
     * documentazione tecnica minima aggiornata (README, commenti, file config, ecc. se necessari).

6. **CI/CD e qualità minima**

   * Ogni repository deve avere un file `.gitlab-ci.yml` con almeno i seguenti stage:

     * `lint` – controlli di stile e formattazione;
     * `test` – test automatici (unit, integration di base);
     * `build` (se applicabile) – build e packaging;
     * `deploy` (se previsto) – deploy verso ambienti di test/staging/prod.

   * Per le MR verso branch protetti:

     * `lint` e `test` sono **obbligatori**;
     * eventuali regole aggiuntive (coverage minima, static analysis) possono essere abilitate per progetti critici.

   * Le regole di deploy (automatica/manuale; ambienti interessati) vengono definite per singolo progetto da Tech Lead + DevOps e documentate (README o doc tecnica collegata).

7. **Collegamento con Odoo**

   * Ogni user story/task Odoo deve avere:

     * almeno una issue GitLab collegata;
     * link alle MR principali che chiudono la story.

   * In GitLab:

     * nelle issue e/o MR si inserisce il link alla pagina Odoo corrispondente.

   * A chiusura MR:

     * il Developer (o PM) aggiorna lo stato della user story in Odoo (es. `In sviluppo` → `In revisione` → `Pronto per rilascio`), secondo SOP-PRJ-01.

8. **Manutenzione del repository**

   * Il Tech Lead, con cadenza almeno **trimestrale**:

     * rimuove i branch già mergiati e non più necessari;
     * verifica i tag e le versioni rilasciate;
     * identifica debito tecnico o refactoring necessari (da trasformare in issue).

   * Per componenti destinati a pubblicazione esterna (pacchetti, librerie):

     * si segue il versioning descritto in **SOP-DEV-02** (tipicamente SemVer);
     * ogni release rilevante è tracciata da un **tag** (`vX.Y.Z`) e, se previsto, da una **release** formale.

---

### 5.3 Modalità di accesso ai repository privati

#### 5.3.1 Accesso da postazione sviluppatore

* Accesso ai repository privati consentito tramite:

  * **SSH key personale** (metodo raccomandato);
  * **HTTPS + Personal Access Token (PAT)**, se necessario.

* Regole:

  * ogni sviluppatore usa **chiavi/token personali**, mai account condivisi;
  * la chiave SSH privata deve essere protetta (es. passphrase, uso limitato alla macchina di lavoro);
  * è **vietato** condividere chiavi o PAT con altre persone (interne o esterne);
  * è **vietato** committare chiavi, token o credenziali nei repository.

#### 5.3.2 Accesso da server / sistemi headless

* L’accesso ai repository da **server** (es. ambienti di staging/prod, runner CI, bastion host) avviene solo tramite:

  * **Deploy key** associate al singolo repository; oppure
  * account tecnico dedicato con permessi limitati (no uso account personali).

* Regole:

  * è **vietato** configurare su server credenziali personali degli sviluppatori;
  * le chiavi e i token lato server devono essere gestiti come **secret** (es. variabili di ambiente protette in GitLab, vault).

---

### 5.4 Workflow su postazioni con interfaccia grafica (IDE / client Git)

Questa sezione descrive il flusso tipico di lavoro da PC con IDE o client Git grafico (es. VS Code, IDE JetBrains, GitKraken, ecc.). Gli strumenti sono liberi, purché rispettino il workflow GitLab definito.

#### 5.4.1 Prerequisiti

* Git configurato con **nome** ed **e-mail aziendale**;
* accesso configurato (SSH o HTTPS+PAT) nel client/IDE;
* repository GitLab individuato e autorizzato.

#### 5.4.2 Flusso standard per una feature

1. **Clonare il repository**

   * Usare l’URL SSH/HTTPS fornito da GitLab (`git@gitlab...` o `https://gitlab...`).
   * Clonare nella cartella di lavoro locale (tramite UI o terminale).

2. **Allinearsi al branch di base**

   * Dal client: `pull` del branch di riferimento (`develop` o `main`) per avere l’ultima versione.

3. **Creare il feature/bugfix branch**

   * Dal client/IDE: creare un nuovo branch da `develop`/`main` secondo naming convenzioni:

     * `feature/ODOO-123-descrizione`
     * `bugfix/ODOO-456-descrizione`

4. **Sviluppo e commit**

   * Eseguire cambi nel codice, con commit:

     * frequenti, atomici;
     * con messaggi chiari (non “varie modifiche”).

   * Gestire staging/commit tramite pannello Git dell’IDE o client.

5. **Aggiornarsi prima del push**

   * Prima del push, effettuare un `pull` (eventuale rebase) dal branch di base, risolvendo eventuali conflitti localmente.

6. **Push del branch remoto**

   * Effettuare `push` del nuovo branch su GitLab (dal client o dalla CLI).

7. **Apertura Merge Request**

   * Dal browser o dal client Git (se supportato), aprire una MR dal branch verso `develop` o `main`:

     * compilare titolo e descrizione;
     * assegnare reviewer;
     * collegare issue/story (closes #ID).

> Nota: anche se il client Git consente merge locali verso `main`/`develop`, è **vietato** usarli per saltare il flusso MR su GitLab.

---

### 5.5 Workflow su sistemi server / headless

Questa sezione si applica a server, VM, container e sistemi senza interfaccia grafica, utilizzati per **deploy, automazioni o consultazioni del codice**, non per sviluppo quotidiano.

#### 5.5.1 Principio generale

* Sui **server**:

  * **non si sviluppa** e **non si committa**;
  * non si creano branch di sviluppo;
  * si eseguono solo:

    * `git clone` del repo (prima volta);
    * `git fetch` / `git pull` su branch/tag già approvati;
    * `git checkout` di specifiche versioni/tag.

#### 5.5.2 Regole operative

* Usare solo **deploy key** o account tecnico dedicato.

* È **vietato**:

  * configurare account personali GitLab sui server;
  * eseguire `git commit`, `git push`, `git merge` lato server;
  * salvare credenziali in chiaro sui filesystem di produzione.

* Eventuali file temporanei, log o configurazioni locali non devono essere committati (utilizzare `.gitignore` appropriato).

#### 5.5.3 Dev-box e ambienti di sviluppo headless

* In caso di ambienti di sviluppo senza UI (es. WSL, container, VM remote) usati da uno sviluppatore:

  * è permesso sviluppare da CLI, purché:

    * si usino branch dedicati;
    * si rispettino le regole di commit e MR;
    * non si effettui mai push su `main`/`develop` senza MR.

---

### 5.6 Gestione collaboratori esterni e condivisione repository privati

#### 5.6.1 Aggiunta di collaboratori esterni

* Collaboratori esterni (freelance, partner, fornitori) accedono ai repo privati **solo tramite GitLab** tramite:

  * invito al singolo progetto; oppure
  * invito a un gruppo specifico con scope limitato.

* Regole:

  * assegnare il **ruolo minimo necessario** (`Reporter`, `Developer`, raramente `Maintainer`);
  * definire, se possibile, una **data di fine** o una procedura di revoca accesso a termine collaborazione;
  * non concedere accesso a gruppi/repo non necessari allo scopo del contratto.

#### 5.6.2 Limiti alla condivisione dei repository

* È **vietato**:

  * condividere credenziali, chiavi o PAT personali con collaboratori esterni;
  * creare fork pubblici di repository privati senza approvazione del CTO;
  * clonare repo privati su dispositivi non conformi alle policy aziendali (se definite a livello di sicurezza).

* In caso di necessità di open-source o condivisione pubblica:

  * si segue **SOP-DEV-02** per scelta licenza, contenuti, pulizia del repo prima della pubblicazione.

---

## 6. Strumenti e sistemi utilizzati

* **GitLab**

  * piattaforma centrale per:

    * repository Git;
    * issue, board, MR, code review;
    * CI/CD;
    * gestione permessi e deploy key.

* **Odoo (modulo Progetti / CRM)**

  * gestione progetti, backlog, user story e task (SOP-PRJ-01);
  * Odoo funge da “fonte di verità” per l’avanzamento e le priorità;
  * link reciproci Odoo ↔ GitLab (issue, MR).

* **Google Drive**

  * archiviazione di documentazione tecnica complementare (diagrammi, specifiche, note di design);
  * collegamento da Odoo e/o README secondo SOP-DOC-01.

* **GitHub / GitHub Pages**

  * utilizzati solo per:

    * pubblicazione di codice/librerie destinate all’esterno (SOP-DEV-02);
    * pubblicazione di documentazione e SOP (SOP-DOC-02).

* **IDE / Editor e client Git**

  * VS Code, IDE JetBrains, altri editor con integrazione Git;
  * client Git grafici (es. GitKraken, Sourcetree, ecc.);
  * l’uso è libero, purché:

    * si rispettino flussi e convenzioni definiti in questo SOP;
    * siano configurati linters/formatter coerenti con il progetto.

* **CLI Git**

  * uso della CLI (`git clone`, `git status`, `git add`, `git commit`, `git push`, ecc.) per:

    * ambienti headless;
    * developer che preferiscono terminale;
  * si applicano le stesse regole di branching, MR e divieti (es. niente commit su server di produzione).

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali del processo

* **R1 – Sviluppo non tracciato o fuori GitLab**
  Codice sviluppato localmente o su altri tool senza repository GitLab → perdita di tracciabilità, difficoltà di manutenzione.

* **R2 – Bypass delle regole di branch/MR**
  Push diretti su `main`/`develop`, merge senza review o senza test → rischio bug in produzione, regressioni.

* **R3 – Disallineamento GitLab ↔ Odoo**
  Issue non collegate alle user story, stati non aggiornati in Odoo → visione incompleta dell’avanzamento, pianificazione distorta.

* **R4 – Qualità insufficiente del codice**
  Assenza di test, lint non applicato, debito tecnico non tracciato → accumulo di problemi sul lungo periodo.

* **R5 – Pipeline inaffidabili**
  CI che fallisce spesso per motivi non correlati al codice → perdita di fiducia nello strumento, tentativo di aggirare la CI.

* **R6 – Sicurezza insufficiente sui repository**
  Secret committati, permessi troppo ampi, condivisione di credenziali → rischio di data leak o compromissione degli ambienti.

* **R7 – Gestione non controllata di collaboratori esterni**
  Accesso eccessivo o non revocato ai repo privati → rischio di divulgazione non autorizzata del codice.

### 7.2 Controlli e misure di mitigazione

* **C1 – Branch protetti**

  * `main` (e `develop` se usato) sono sempre protetti;
  * merge solo tramite MR con pipeline CI verde e almeno 1 reviewer.

* **C2 – Verifiche periodiche su link GitLab–Odoo**

  * campionamento progetti/story per verificare collegamenti e aggiornamento stati.

* **C3 – Norme minime di qualità CI**

  * obbligo di stage `lint` e `test` per MR verso branch protetti;
  * possibilità di introdurre soglie di coverage o static analysis.

* **C4 – Audit interni sul workflow Git**

  * verifica saltuaria dei log GitLab:

    * push diretti su branch protetti;
    * MR senza review;
    * pattern di commit non conformi.

* **C5 – Gestione sicura dei secret**

  * uso di variabili protette in GitLab CI;
  * divieto esplicito di committare file con credenziali, chiavi, configurazioni sensibili.

* **C6 – Revisione accessi collaboratori esterni**

  * controllo periodico membri dei progetti;
  * revoca accessi alla chiusura dei contratti.

### 7.3 KPI / Indicatori (se applicabili)

Esempi di KPI collegati a questo SOP:

* **KPI-DEV-01 – % MR con pipeline CI passata al primo tentativo**
* **KPI-DEV-02 – % branch chiusi (mergiati o rimossi) entro X giorni dalla creazione**
* **KPI-DEV-03 – % issue GitLab con link a user story/task Odoo**
* **KPI-DEV-04 – % MR con almeno 1 reviewer diverso dall’autore**
* **KPI-DEV-05 – Numero medio di bug rilevati in QA per release**

Dettagli (formula, target, frequenza, owner) possono essere formalizzati in una **Scheda KPI Sviluppo** allegata o in SOP di qualità.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* Il SOP è archiviato nel **repository documentale** secondo SOP-DOC-01 (es. `/SOP/SOP-DEV/`).
* La versione ufficiale approvata è resa disponibile:

  * nella **Odoo Knowledge Base** (categoria “SOP – Sviluppo Software”);
  * eventualmente su **GitHub Pages** nell’area documentazione interna (SOP-DOC-02).

### 8.2 Revisione e aggiornamento

* Il SOP viene rivisto:

  * in caso di modifiche significative al workflow Git/GitLab (es. cambio branching model, nuovo sistema CI/CD);
  * in caso di introduzione di nuove policy di sicurezza o standard qualità;
  * a seguito di non conformità o audit;
  * comunque entro la data di revisione prevista.

* Proposte di modifica possono essere presentate da CTO, Tech Lead, DevOps, PM/PO.

* Ogni nuova versione:

  * aggiorna numero di versione e data di emissione;
  * registra le modifiche nella **sezione 10 – Storico revisioni**.

### 8.3 Obbligatorietà e formazione

* Tutti gli **sviluppatori, Tech Lead, DevOps, PM/PO** che utilizzano GitLab devono conoscere e applicare il presente SOP.
* In occasione dell’introduzione o di revisioni rilevanti:

  * il CTO/Responsabile Sviluppo organizza momenti di formazione/comunicazione (sincroni o asincroni);
  * può essere richiesta la presa visione formale tramite canali aziendali (KB Odoo, comunicazioni interne).

---

## 9. Allegati (opzionale)

* **Allegato 1 – Matrice RACI dettagliata per utilizzo GitLab**
* **Allegato 2 – Linee guida standard per branching model e naming**
* **Allegato 3 – Template `.gitlab-ci.yml` base aziendale**
* **Allegato 4 – Esempi di convenzioni per i messaggi di commit**
* **Allegato 5 – Checklist di revisione MR (code review checklist)**
* **Allegato 6 – Scheda KPI sviluppo collaborativo**
* **Allegato 7 – Linee guida per gestione accessi (SSH key, PAT, deploy key, collaboratori esterni)**

*(Gli allegati sono archiviati nella stessa struttura del SOP o in cartelle dedicate collegate in Odoo KB.)*

---

## 10. Storico revisioni

| Versione | Data       | Descrizione modifica     | Redatto da                  | Verificato da                    | Approvato da             |
| -------- | ---------- | ------------------------ | --------------------------- | -------------------------------- | ------------------------ |
| 0.1      | 2025-11-16 | Prima emissione in bozza | CTO / Responsabile Sviluppo | Project Manager Progetti Interni | CEO / Direzione Generale |

