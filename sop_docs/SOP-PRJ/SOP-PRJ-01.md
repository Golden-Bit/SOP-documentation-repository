# SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo

---

### 0. Metadati del documento

* **Codice SOP:** SOP-PRJ-01
* **Titolo:** Gestione progetti e metodologia Scrum multi-progetto su Odoo
* **Versione:** 1.0
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Project Management / PMO]*
* **Verificato da (se applicabile):** *[CTO / Responsabile IT]*
* **Approvato da:** *[Direzione]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

### Scopo

Il presente SOP definisce in modo standard:

* il modello di **gestione progetti su Odoo** basato su una versione iniziale di **template Scrum**;
* la modalità con cui vengono gestiti **progetti multipli** (multi-progetto) tramite:

  * un **“Main Project”** di coordinamento;
  * progetti Odoo specifici per clienti e iniziative interne;
* l’uso di **schede (card)** con etichette standard per distinguere:

  * *PROJECT* (riferimento ad altri progetti Odoo),
  * *EPIC*,
  * *STORY*,
  * *TASK* (inclusi sottotipi BUG, FIX, ecc.);
* l’utilizzo dei campi personalizzati **Sprint** e **Story Point** e il collegamento tra task Odoo e **ticket GitLab** per lo sviluppo tecnico;
* la **standardizzazione delle informazioni di progetto** tramite una **descrizione strutturata** in ciascun progetto Odoo, che includa:

  * meta-informazioni Scrum (durata Sprint, Scrum Master, frequenza dei Daily, ecc.);
  * riferimenti a documentazione (GitHub Pages, KB Odoo, cartelle Google Drive);
* l’**obbligo di associare a ogni progetto** un **Documento di Progetto** (interno o esterno) redatto secondo i template ufficiali allegati al presente SOP.

### Campo di applicazione

Il SOP si applica a tutti i progetti:

* **interni** (progetti di miglioramento, R&D, iniziative aziendali);
* **per clienti** (commesse, prodotti, servizi erogati);

e a tutte le figure coinvolte nella gestione e nell’esecuzione dei progetti, in particolare:

* Direzione / Management;
* PMO / Project Manager Senior;
* Project Manager / Product Owner;
* Scrum Master (se presente);
* Team di sviluppo;
* Risorse di supporto (es. amministrazione per la parte economica, commerciale per allineamento con offerte, ecc.).

Sono esclusi da questo documento:

* i dettagli delle pratiche amministrativo-contabili (coperti da **SOP-ACC-01**);
* i dettagli tecnici di sviluppo su GitLab (coperti da **SOP-DEV-01** e **SOP-DEV-02**);
* le modalità di gestione documentale e KB (coperte da **SOP-DOC-01**, **SOP-DOC-02**, **SOP-KB-01**).

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabile)

*Da compilare in caso di adozione di standard formali (es. ISO 9001 per il project management, normative contrattuali di settore, ecc.).*

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
* **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo**
* **SOP-MKT-01 – Immagine, comunicazione e gestione dei canali marketing**
* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**
* **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**
* **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**
* **SOP-ACC-01 – Gestione contabile e tesoreria su Odoo**
* **SOP-INDEX-01 – Indice generale delle Procedure Operative Standard (SOP)**

> **SOP da prevedere in futuro (raccomandati):**
>
> * *SOP-PRJ-02 – Stima effort e gestione degli Story Point*
> * *SOP-PRJ-03 – Gestione capacity e carico risorse sui progetti*
> * *SOP-DOC-03 – Struttura standard dei repository documentali di progetto*

---

## 3. Definizioni, acronimi e abbreviazioni

* **Main Project** – Progetto Odoo di livello più alto, utilizzato da Direzione / PMO per coordinare l’intero portafoglio progetti (interni ed esterni).
* **Progetto Odoo** – Progetto operativo (interno o per cliente) gestito come istanza specifica nel modulo Progetti di Odoo.
* **Board Scrum (Kanban)** – Vista a colonne del progetto in Odoo, articolata in: **BACKLOG**, **ASSIGNED**, **IN PROGRESS**, **DONE**.
* **Scheda / Card** – Elemento del board che rappresenta un’unità di lavoro (PROJECT, EPIC, STORY, TASK).
* **Card di tipo PROJECT** – Scheda che rappresenta un **riferimento a un altro progetto Odoo** (interno o per cliente). Usata per collegare progetti tra loro (es. dipendenze, iniziative di coordinamento).
* **EPIC** – Iniziativa di livello alto che aggrega più Story/Task. Nella fase iniziale, un potenziale progetto (non ancora contrattualizzato) viene tracciato come EPIC.
* **STORY (User Story)** – Requisito funzionale o incremento di valore, scomponibile in Task tecnici o operativi.
* **TASK** – Attività eseguibile, granularità operativa. Può avere sottotipi (tramite etichette): *TASK* standard, *BUG*, *FIX*, ecc.
* **Etichette (Label)** – Tag Odoo utilizzati per distinguere il tipo di card: PROJECT, EPIC, STORY, TASK, BUG, FIX, ecc.
* **Sprint** – Periodo temporale definito (es. 1–2 settimane) in cui viene pianificato un insieme di Story/Task. Gestito tramite campo personalizzato nelle schede.
* **Story Point** – Misura relativa dell’effort/complessità di una Story/Task, gestita tramite campo personalizzato.
* **Ticket GitLab (Issue)** – Elemento di tracciamento tecnico nello sviluppo software, collegato a Story/Task Odoo di tipo tecnico.
* **Descrizione Progetto standardizzata** – Testo descrittivo del progetto Odoo che segue uno schema minimo comune, includendo una descrizione libera, meta-informazioni Scrum e riferimenti documentali.
* **Documento di Progetto** – Documento formale associato a ogni progetto Odoo, che descrive contesto, obiettivi, scope, stakeholder, setup Scrum, piano di lavoro, rischi, riferimenti e allegati.

  * **Documento di Progetto – Progetto Esterno (Cliente)** – Versione del template usata per progetti verso clienti esterni.
  * **Documento di Progetto – Progetto Interno** – Versione del template usata per progetti interni.
* **Repository documentale di progetto (repo principale)** – Repository Git (es. su GitHub/GitLab) dedicato alla **documentazione di progetto** (non al codice sorgente), creato in modo standard per ogni progetto.
* **Cartella Drive di progetto** – Cartella principale su Google Drive associata a ogni progetto, che contiene documenti operativi, allegati, esportazioni, output, ecc.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

L’azienda è una **software house** orientata a progetti multi-cliente e iniziative interne.

L’area di riferimento principale per questo SOP è:

* **Progetti & Delivery**, in stretta collaborazione con:

  * **Sviluppo Software** (per gli aspetti tecnici e GitLab);
  * **Commerciale & Marketing** (per la transizione da opportunità a progetto);
  * **Amministrazione & Contabilità** (per coerenza con contratti, budget e consuntivi);
  * **Direzione** (per il governo del portafoglio tramite Main Project).

### 4.2 Ruoli e responsabilità (RACI di alto livello)

Legenda: **R = Responsible**, **A = Accountable**, **C = Consulted**, **I = Informed**

* **Direzione / Management**

  * A: definizione delle priorità del portafoglio progetti (Main Project).
  * A: approvazione di nuovi progetti strategici.
  * C/I: consultata e informata sullo stato delle EPIC e dei PROJECT card principali.

* **PMO / Project Manager Senior (Main Project)**

  * R: gestione del **Main Project** in Odoo.
  * R: creazione e manutenzione di EPIC e card PROJECT che rappresentano i vari progetti/sottoprogetti.
  * C: coordinamento con Direzione, Commerciale e Sviluppo per roadmap e dipendenze.

* **Project Manager / Product Owner (per singolo progetto)**

  * R: gestione del progetto Odoo specifico (interno o cliente).
  * R: definizione di EPIC, STORY e TASK nel progetto di competenza.
  * R: compilazione e aggiornamento della **Descrizione Progetto standardizzata** (vedi §5.3.1).
  * R: redazione e manutenzione del **Documento di Progetto** (vedi §5.3.1 – punto 5).
  * R: assegnazione delle card alle risorse e gestione delle colonne BACKLOG/ASSIGNED/IN PROGRESS/DONE.
  * C: interfaccia con PMO e Direzione per allineamento su scope, priorità, avanzamento.

* **Scrum Master** (se previsto)

  * R: facilitazione del processo Scrum (cerimonie, rimozione impedimenti).
  * R: proposta/gestione di durata Sprint, orari e frequenza dei Daily, da riportare nella Descrizione Progetto e nel Documento di Progetto.
  * C: supporto al PM/PO per la qualità del flusso e il rispetto del processo.

* **Team di Sviluppo**

  * R: esecuzione delle STORY/TASK tecniche.
  * R: gestione dei ticket GitLab corrispondenti e aggiornamento dello stato (su GitLab e, a fine lavoro, su Odoo).
  * C/I: informato/consultato per la stima degli Story Point.

* **Amministrazione**

  * C: consultata per verificare coerenza tra progetti Odoo, contratti e fatturazione (SOP-ACC-01).
  * I: informata sulle fasi chiave di vita dei progetti (apertura, chiusura, variazioni rilevanti).

* **Commerciale & Marketing**

  * R: gestione delle opportunità in Odoo (SOP-CRM-01).
  * C/I: coordina la transizione da opportunità a EPIC e quindi a PROJECT (quando il progetto viene ufficializzato).

Dettagli RACI più granulari possono essere definiti in una matrice allegata (vedi sezione 9).

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il processo di gestione progetti su Odoo prevede:

* un **Main Project** che rappresenta il livello di coordinamento top-down (Direzione/PMO);
* progetti Odoo specifici (interni o cliente) gestiti con **board Scrum** articolato in fasi: BACKLOG, ASSIGNED, IN PROGRESS, DONE;
* utilizzo di **card etichettate** (PROJECT, EPIC, STORY, TASK) per distinguere i livelli di astrazione;
* utilizzo di **campi personalizzati** per Sprint e Story Point su Story/Task;
* collegamento delle **Story/Task tecniche** a corrispondenti **ticket GitLab**, dove viene gestito il dettaglio operativo dello sviluppo;
* un ciclo di vita che parte da un **potenziale progetto** (EPIC) e, una volta ufficializzato, porta alla creazione di un **progetto Odoo dedicato** e alla trasformazione in card di tipo PROJECT;
* la presenza, in ogni progetto, di:

  * una **Descrizione Progetto standardizzata** nel record del progetto Odoo;
  * un **Documento di Progetto** redatto con il template appropriato (interno o esterno);
  * un **repository documentale di progetto** e una **cartella Drive di progetto** creati contestualmente e collegati al progetto.

### 5.2 Flusso operativo di alto livello

1. **Arrivo del potenziale progetto**

   * Dal CRM (SOP-CRM-01) un’opportunità matura viene identificata come potenziale progetto.
   * Nel **Main Project** viene creata una **EPIC** che rappresenta il potenziale progetto (non ancora ufficializzato).

2. **Valutazione e pianificazione preliminare**

   * La EPIC viene descritta, discussa e, se necessario, scomposta in prime STORY/TASK di analisi.
   * Possono essere registrati primi Story Point di alto livello (stima grossolana).

3. **Ufficializzazione del progetto**

   * A seguito di approvazione economica/contrattuale (preventivo accettato, contratto firmato, decisione interna formale), il potenziale progetto diventa progetto effettivo.
   * Si crea un **nuovo progetto Odoo** dedicato (interno o cliente).
   * La EPIC nel Main Project viene evoluta/collegata a una **card di tipo PROJECT** che fa riferimento al nuovo progetto Odoo.
   * Vengono creati contestualmente:

     * la **Cartella Drive di progetto** (vedi §5.3.6);
     * il **Repository documentale di progetto** (repo principale, vedi §5.3.6);
   * Il PM/PO compila la **Descrizione Progetto standardizzata** e avvia la redazione del **Documento di Progetto** (interno o esterno) utilizzando i template ufficiali.

4. **Gestione del progetto nel proprio board**

   * Nel progetto Odoo specifico vengono definiti:

     * EPIC di dettaglio;
     * STORY e TASK (con eventuali sottotipi: BUG, FIX, ecc.).
   * Le card transitano tra le colonne BACKLOG → ASSIGNED → IN PROGRESS → DONE secondo lo stato del lavoro.
   * Sprint e Story Point vengono valorizzati sulle STORY/TASK pertinenti.

5. **Gestione delle attività tecniche su GitLab**

   * Per le **STORY/TASK di tipo tecnico**, viene creato o collegato un **ticket GitLab**.
   * Il lavoro di sviluppo viene gestito in GitLab (issue, branch, merge request, CI/CD).
   * A completamento, il ticket GitLab viene chiuso e la card Odoo corrispondente viene aggiornata (spostata in DONE e completati i campi di riferimento).

6. **Monitoraggio multi-progetto**

   * Il **Main Project** rimane il punto di controllo per:

     * stato di avanzamento dei principali progetti (card PROJECT);
     * pianificazione di alto livello tramite EPIC e TASK gestionali (es. assegnazione risorse, scelte strategiche).
   * I singoli progetti Odoo alimentano il quadro complessivo tramite l’aggiornamento regolare delle card e dei link.
   * La Descrizione Progetto standardizzata e il Documento di Progetto permettono di comprendere rapidamente setup Scrum, contesto e riferimenti.

7. **Chiusura progetto**

   * Una volta completato il progetto:

     * le card principali vengono marcate come DONE;
     * il Documento di Progetto viene aggiornato con gli esiti finali (retrospettiva, lesson learned, ecc.);
     * vengono aggiornati riferimenti documentali (Drive, GitHub Pages, KB, stato in CRM/contabilità);
     * si effettua un eventuale *retrospective* e, se necessario, si aggiornano SOP/KB.

---

### 5.3 Istruzioni operative / Dettaglio per fasi

#### 5.3.1 Struttura progetti: Main Project, progetti specifici e Descrizione standardizzata

* **Main Project**

  * Contiene:

    * card di tipo PROJECT per ciascun progetto Odoo rilevante (interno o cliente);
    * EPIC e TASK di livello gestionale/strategico (es. allocazione risorse, iniziative cross-progetto);
  * È utilizzato principalmente da Direzione, PMO e PM senior.

* **Progetti specifici (Clienti / Interni)**

  * Ogni progetto ha la propria board con colonne standard:

    * **BACKLOG** – elementi noti ma non ancora prioritizzati o assegnati;
    * **ASSIGNED** – card assegnate a una risorsa o a un team, in attesa di lavorazione;
    * **IN PROGRESS** – card su cui è in corso il lavoro;
    * **DONE** – card completate e verificate.
  * Ogni progetto può, a sua volta, contenere card PROJECT che referenziano **sotto-progetti** o progetti collegati.

* **Descrizione Progetto standardizzata (campo descrizione progetto Odoo)**
  Per ogni progetto Odoo deve essere compilata una descrizione con la seguente struttura minima:

  1. **Descrizione generale del progetto**

     * Obiettivo principale.
     * Cliente (se applicabile).
     * Contesto e scope ad alto livello.

  2. **Setup Scrum del progetto**

     * **Durata Sprint:** es. “Sprint di 2 settimane (lun–ven)”.
     * **Periodo di riferimento (se noto):** es. “Periodo previsto progetto: 2025-01 → 2025-06”.
     * **Scrum Master:** nome/ruolo.
     * **Project Manager / Product Owner:** nome/ruolo.
     * **Frequenza e orario Daily:** es. “Daily: ogni giorno lavorativo alle 9:30”.
     * **Cerimonie principali:** es. “Sprint Planning/Review/Retro a inizio/fine Sprint”.

  3. **Riferimenti documentali**

     * **Drive – Cartella progetto:** link alla directory principale su Google Drive.
     * **Repository documentale di progetto (repo principale):** link al repository Git relativo alla documentazione del progetto.
     * **GitHub Pages – Documentazione:** link alla pagina/sito documentazione progetto (se presente).
     * **Odoo KB – Articolo di riferimento:** link all’articolo Knowledge Base che sintetizza il progetto (se esiste).

  4. **Note operative (opzionale)**

     * Regole particolari (es. orari di contatto con il cliente, vincoli di ambiente, dipendenze con altri progetti).
     * Eventuali eccezioni rispetto al processo standard definito in questo SOP.

> Ove possibile, i link a Drive, al repository documentale e a GitHub Pages devono essere coerenti con i campi personalizzati configurati sul progetto Odoo (vedi §6).

#### 5.3.2 Documento di Progetto

Per **ogni progetto Odoo** deve esistere un **Documento di Progetto** aggiornato, archiviato nella cartella Drive di progetto e nel repository documentale.

* **Tipologia del Documento di Progetto**

  * Per progetti verso clienti esterni si usa il template:
    **“Documento di Progetto – Progetto Esterno (Cliente)”** (vedi Allegati).
  * Per progetti interni si usa il template:
    **“Documento di Progetto – Progetto Interno”** (vedi Allegati).

* **Contenuti principali**
  I template contengono sezioni standard, tra cui:

  * Metadati di progetto (codice, titolo, sponsor/cliente, PM/PO, Scrum Master, stato).
  * Contesto e obiettivi.
  * Scope (in/out).
  * Stakeholder e ruoli.
  * Setup Scrum e modalità di lavoro.
  * Backlog di alto livello (EPIC/macrostorie).
  * Piano di lavoro e milestone.
  * Rischi, assunzioni, mitigazioni.
  * Riferimenti a sistemi/documenti/SOP.
  * Allegati (diagrammi, specifiche, mockup, ecc.).

* **Responsabilità**

  * Il **PM/PO** è Responsible della creazione e manutenzione del Documento di Progetto.
  * Lo **Scrum Master** e il team contribuiscono all’aggiornamento di parti specifiche (es. rischi, setup Scrum, retrospettive).
  * La Direzione/PMO può richiedere aggiornamenti periodici e approvare versioni chiave.

* **Collegamenti**

  * Il Documento di Progetto:

    * deve essere linkato nella Descrizione Progetto Odoo (sezione “Riferimenti documentali”);
    * deve essere presente nella cartella Drive di progetto;
    * può essere richiamato in KB Odoo con un breve articolo di sintesi.

#### 5.3.3 Tipi di card e etichette

La distinzione dei tipi di card avviene tramite **etichette standardizzate**:

* **[PROJECT]**

  * Card che rappresenta un altro progetto Odoo.
  * Deve contenere:

    * riferimento al progetto Odoo (campo specifico o link);
    * eventuali EPIC/TASK gestionali collegate (es. coordinamento, dipendenze).

* **[EPIC]**

  * Utilizzata sia nel Main Project sia nei progetti specifici.
  * Una EPIC può rappresentare:

    * un potenziale progetto (fase iniziale, prima di contratto);
    * un’iniziativa di alto livello che aggrega più Story.

* **[STORY]**

  * Requisito funzionale o incremento di valore.
  * Deve includere:

    * descrizione chiara (come utente… voglio… per…);
    * criteri di accettazione;
    * Sprint e Story Point (quando stimati).

* **[TASK] / [BUG] / [FIX]**

  * Attività operative, tecniche o non tecniche.
  * Per TASK tecnici:

    * obbligatorio il collegamento al ticket GitLab (vedi §5.3.5).

> Le etichette devono essere mantenute **coerenti** su tutti i progetti per evitare ambiguità.

#### 5.3.4 Gestione Sprint e Story Point

* Ogni STORY/TASK può avere:

  * **Sprint** – selezionato tramite campo personalizzato (es. “Sprint 2025-01-A”).
  * **Story Point** – valore numerico o da scala predefinita (es. 1, 2, 3, 5, 8, 13).
* Attualmente, gli Story Point sono gestiti **a livello card**, non ancora per singolo assegnatario.
* La gestione avanzata degli Story Point per risorsa potrà essere:

  * definita in una futura revisione del presente SOP, oppure
  * dettagliata in *SOP-PRJ-02 – Stima effort e gestione degli Story Point*.

#### 5.3.5 Collegamento con GitLab per le attività tecniche

Per tutte le **Story/Task di tipo tecnico**:

1. Il PM/PO o lo sviluppatore:

   * crea un **ticket GitLab** corrispondente (issue), oppure
   * collega la card a un ticket GitLab già esistente.

2. Nella card Odoo:

   * viene inserito il riferimento al ticket GitLab (URL o campo dedicato);
   * lo stato della card segue lo stato di lavorazione reale (BACKLOG → ASSIGNED → IN PROGRESS → DONE).

3. In GitLab:

   * lo sviluppo viene gestito secondo **SOP-DEV-01**:

     * branch, merge request, code review, CI/CD.

4. A completamento:

   * il ticket GitLab viene chiuso;
   * la card Odoo viene spostata in **DONE** e, se previsto, vengono aggiornati output/documenti (link Drive, note, ecc.).

#### 5.3.6 Creazione automatica di repository documentale e cartella Drive di progetto

Per ogni **nuovo progetto Odoo ufficializzato** (interno o cliente) devono essere creati:

1. **Cartella Drive di progetto (obbligatoria)**

   * Funzione: archivio principale di:

     * Documento di Progetto (versione .docx e/o .md);
     * materiali di analisi;
     * verbali di riunione;
     * mockup, allegati, esportazioni;
     * eventuali documenti operativi non gestiti altrove.
   * **Standard di nomenclatura:**

     * `{{CODICE_PROGETTO}} - {{Titolo sintetico progetto}}`
     * Esempio: `PRJ-EXT-2025-001 - Piattaforma Ordini B2B`
   * La cartella viene:

     * creata automaticamente (o tramite procedura standard) sotto una root comune (es. `/Progetti/Clienti` o `/Progetti/Interni`);
     * linkata nel progetto Odoo:

       * in un **campo personalizzato** “Cartella Drive progetto”;
       * nella **Descrizione Progetto standardizzata** (sezione “Riferimenti documentali”).

2. **Repository documentale di progetto (repo principale – obbligatorio)**

   * Funzione: repository Git dedicato alla **documentazione di progetto** (non al codice), che può alimentare GitHub Pages o analoghi sistemi.
   * Contenuti tipici:

     * versione in Markdown del Documento di Progetto;
     * documentazione tecnica e funzionale (es. `/docs/` con architettura, specifiche, API, ecc.);
     * file di configurazione per la pubblicazione (es. GitHub Pages).
   * **Standard di nomenclatura del repository documentale:**

     * `{{codice_progetto_minuscolo}}-docs`
     * Dove `codice_progetto_minuscolo` è il codice progetto convertito in minuscolo con trattini.
     * Esempio:

       * Codice progetto: `PRJ-EXT-2025-001`
       * Nome repo: `prj-ext-2025-001-docs`
   * Il repository viene:

     * creato nel sistema scelto per la documentazione (es. GitHub o GitLab, secondo SOP-DOC-02 / SOP-DEV-02);
     * collegato al progetto Odoo:

       * in un **campo personalizzato** “Repository documentale progetto”;
       * nella **Descrizione Progetto standardizzata** (sezione “Riferimenti documentali”);
       * eventualmente tramite link nell’articolo KB di progetto.

3. **Altri repository e cartelle (opzionali)**

   * Il progetto può avere:

     * ulteriori cartelle Drive (es. condivise con partner o clienti specifici);
     * uno o più repository di **codice** (es. `prj-ext-2025-001-api`, `prj-ext-2025-001-frontend`, ecc.).
   * **Importante:**

     * I **repository di codice** devono rispettare gli standard e le convenzioni definiti nei SOP di sviluppo (**SOP-DEV-01**, **SOP-DEV-02** e, quando disponibile, SOP specifico per naming e struttura repo di codice).
     * La **struttura interna del repository documentale** (cartelle `docs/`, `spec/`, `adr/`, ecc.) sarà definita in **SOP-DOC-03 – Struttura standard dei repository documentali di progetto**.

---

## 6. Strumenti e sistemi utilizzati

* **Odoo – Modulo Progetti**

  * Strumento principale per la gestione di:

    * Main Project;
    * progetti specifici (interni e cliente);
    * board Scrum (BACKLOG, ASSIGNED, IN PROGRESS, DONE);
    * Sprint e Story Point (campi personalizzati);
    * etichette di tipo card (PROJECT, EPIC, STORY, TASK, BUG, FIX);
    * **Descrizione Progetto standardizzata**, contenente meta-informazioni Scrum e riferimenti documentali;
    * collegamenti a cartella Drive di progetto, repository documentale, Documenti di Progetto e articoli KB.

* **Odoo – CRM**

  * Fonte delle opportunità che possono evolvere in EPIC / PROJECT (SOP-CRM-01).

* **Google Drive**

  * Archivio dei file di progetto (documenti, specifiche, presentazioni, output, esportazioni).
  * Per ogni progetto Odoo:

    * viene creata una **Cartella Drive di progetto** con standard di nomenclatura descritto in §5.3.6;
    * la cartella è linkata in:

      * campo personalizzato “Cartella Drive progetto”;
      * Descrizione Progetto standardizzata;
      * eventualmente in KB Odoo.
  * Gestione secondo **SOP-DOC-01**.

* **Repository documentale di progetto (GitHub / GitLab)**

  * Repository git dedicato alla documentazione del progetto (principalmente Markdown, immagini, file di configurazione per GitHub Pages, ecc.).
  * Creato con standard di nomenclatura `{{codice_progetto_minuscolo}}-docs` (es. `prj-ext-2025-001-docs`).
  * Può essere utilizzato per:

    * pubblicazione della documentazione su GitHub Pages o analoghi;
    * versionamento della documentazione di progetto.
  * Configurazione e pubblicazione secondo:

    * **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**;
    * eventuale futuro **SOP-DOC-03** per struttura interna.

* **Odoo – Knowledge Base**

  * Utilizzata per documentare:

    * linee guida sul project management;
    * articoli esplicativi collegati a questo SOP;
    * articoli specifici di progetto (riassunto, link rapidi a repo e cartella Drive).
  * Collegamenti gestiti secondo **SOP-KB-01**.

* **GitLab**

  * Strumento di riferimento per lo sviluppo tecnico:

    * repository di codice;
    * issue/ticket;
    * CI/CD.
  * Uso disciplinato da **SOP-DEV-01** (e, per pubblicazione esterna, da **SOP-DEV-02**).

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali del processo

* **Rischio R1 – Mancata coerenza Odoo ↔ GitLab**

  * Task tecnici non collegati a ticket GitLab o viceversa.
  * Impatto: perdita di tracciabilità tra requisiti e codice.

* **Rischio R2 – Uso incoerente delle etichette di tipo card**

  * EPIC, STORY, TASK, PROJECT non uniformi tra progetti.
  * Impatto: difficoltà di lettura dei board, confusione nel reporting.

* **Rischio R3 – Mancata evoluzione dei potenziali progetti**

  * EPIC che non vengono aggiornate quando il progetto diventa ufficiale.
  * Impatto: disallineamento tra CRM, Main Project e progetti effettivi.

* **Rischio R4 – Mancato utilizzo di Sprint e Story Point**

  * Stime non formalizzate, difficoltà di pianificazione e previsione.
  * Impatto: pianificazione debole, carichi non bilanciati.

* **Rischio R5 – Descrizioni Progetto incomplete o non standardizzate**

  * Assenza di informazioni su durata Sprint, Scrum Master, Daily, link documentazione.
  * Impatto: difficoltà di onboarding, dipendenza eccessiva da conoscenza informale.

* **Rischio R6 – Mancata creazione o mancato utilizzo di cartella Drive e repository documentale standard**

  * Documentazione dispersa o non rintracciabile.
  * Impatto: perdita di informazioni, difficoltà in audit interni/esterni e nel passaggio di consegne.

### 7.2 Controlli e misure di mitigazione

* Controlli periodici (es. mensili) su:

  * percentuale di Story/TASK tecniche con link a GitLab;
  * coerenza delle etichette sui progetti di nuova creazione;
  * allineamento tra EPIC del Main Project e progetti Odoo effettivi;
  * presenza e completezza della **Descrizione Progetto standardizzata** (tutti i blocchi principali compilati);
  * esistenza di:

    * cartella Drive di progetto;
    * repository documentale (`{{codice_progetto_minuscolo}}-docs`);
    * Documento di Progetto aggiornato (almeno in versione iniziale).

* Revisioni periodiche del presente SOP e degli articoli KB associati (SOP-KB-01).

* Possibile introduzione di checklist di controllo, ad es.:

  * “Checklist apertura progetto Odoo” (inclusa verifica creazione repo e cartella Drive);
  * “Checklist collegamento Odoo ↔ GitLab”;
  * “Checklist chiusura progetto”.

### 7.3 KPI / Indicatori (esempi)

* **KPI1 – % Story/TASK tecniche con ticket GitLab collegato**
  Obiettivo: ≥ 90%.

* **KPI2 – % backlog stimato con Story Point**
  Obiettivo: percentuale di Story/TASK con Story Point valorizzati ≥ soglia definita.

* **KPI3 – Lead time medio per Story**
  Tempo medio dalla colonna ASSIGNED a DONE.

* **KPI4 – % progetti con link Drive e repository documentale valorizzati**
  Misura la completezza della configurazione documentale.

* **KPI5 – % progetti con Descrizione Progetto completa**
  Verifica se tutte le sezioni minime (descrizione generale, setup Scrum, riferimenti documentali) sono presenti.

* **KPI6 – % progetti con Documento di Progetto presente e aggiornato**
  Controlla quanti progetti hanno almeno una versione del Documento di Progetto conforme ai template allegati.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* Il presente SOP è archiviato e pubblicato su **GitHub Pages** all’interno del **SOP repository**.
* Un link diretto è presente:

  * nella **Knowledge Base Odoo**, categoria “SOP – Progetti & Delivery”;
  * ove opportuno, nel modulo Progetti di Odoo (es. campo “Documentazione SOP progetto”).

### 8.2 Revisione e aggiornamento

La revisione del presente SOP è necessaria in caso di:

* cambiamenti significativi nella metodologia (es. introduzione di nuove colonne/fasi, nuovo template Scrum, aggiunta di Kanban personalizzati);
* modifiche nel modo in cui viene gestito il multi-progetto (Main Project, riferimenti a progetti/sotto-progetti);
* cambiamenti nei sistemi (nuove integrazioni Odoo–GitLab, strumenti alternativi a Drive/GitHub Pages);
* evoluzione delle convenzioni sulla **Descrizione Progetto standardizzata**, sui **Documenti di Progetto** o sugli standard di naming di cartelle/repository;
* output di audit interni o retrospettive che evidenziano criticità.

Ogni revisione deve:

* aggiornare versione e data di emissione;
* riportare le modifiche nella sezione **10 – Storico revisioni**.

### 8.3 Obbligatorietà e formazione

* Tutti i PM/PO, Scrum Master e membri del team coinvolti nella gestione e nell’esecuzione dei progetti sono tenuti a:

  * conoscere il presente SOP;
  * utilizzarlo come riferimento per la configurazione e gestione dei progetti Odoo;
  * assicurare che la **Descrizione Progetto standardizzata**, la **Cartella Drive di progetto**, il **Repository documentale** e il **Documento di Progetto** siano creati e mantenuti aggiornati.

* In caso di modifiche significative:

  * è raccomandata una **sessione di formazione** o comunicazione interna (es. articolo KB, breve video, riunione di allineamento);
  * può essere richiesta la **presa visione** formale del SOP aggiornato.

---

## 9. Allegati (opzionale)

*Da definire e pubblicare nel repository dedicato alla documentazione SOP.*

Esempi di allegati previsti:

* **Allegato 1 – Diagramma di flusso del processo multi-progetto (Main Project ↔ Progetti specifici)**
* **Allegato 2 – Matrice RACI dettagliata per ruoli PMO / PM / Dev**
* **Allegato 3 – Checklist apertura progetto Odoo**

  * Include verifica di:

    * creazione progetto in Odoo;
    * compilazione minima Descrizione Progetto;
    * creazione cartella Drive;
    * creazione repository documentale `{{codice_progetto_minuscolo}}-docs`;
    * creazione Documento di Progetto (bozza iniziale).
* **Allegato 4 – Checklist collegamento Odoo ↔ GitLab**
* **Allegato 5 – Template testuale per Descrizione Progetto standardizzata**

  * Piccolo snippet copiabile/incollabile nella descrizione progetto Odoo.
* **Allegato 6 – Template “Documento di Progetto – Progetto Esterno (Cliente)”**

  * Versione Markdown e DOCX, come definito nei template ufficiali dell’azienda.
* **Allegato 7 – Template “Documento di Progetto – Progetto Interno”**

  * Versione Markdown e DOCX, come definito nei template ufficiali dell’azienda.

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica                                                                                | Redatto da      | Verificato da   | Approvato da  |
| -------- | ------------ | --------------------------------------------------------------------------------------------------- | --------------- | --------------- | ------------- |
| 1.0      | *[da comp.]* | Prima emissione del SOP-PRJ-01, inclusa definizione Documenti di Progetto, repo/cartolette standard | *[PMO / Ruolo]* | *[CTO / Ruolo]* | *[Direzione]* |
