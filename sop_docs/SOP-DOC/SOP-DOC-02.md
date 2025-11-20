# SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages

---

### 0. Metadati del documento

* **Codice SOP:** SOP-DOC-02
* **Titolo:** Pubblicazione documentazione e SOP su GitHub Pages
* **Versione:** 1.0
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Responsabile Qualità / Documentazione]*
* **Verificato da (se applicabile):** *[Ruolo/Funzionale]*
* **Approvato da:** *[Direzione]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna (consultabile anche via sito documentazione)

---

## 1. Scopo e campo di applicazione

### Scopo

Il presente SOP definisce, in modo **trasversale e di alto livello**, **quali tipologie di documentazione aziendale** vengono gestite tramite:

* **GitHub** come **fonte di verità** per i file sorgente (es. Markdown, file strutturati);
* **GitHub Pages** come piattaforma di **pubblicazione web** della documentazione (sito statico aziendale);

and con **quali criteri** si decide:

* cosa viene pubblicato su GitHub Pages;
* quando utilizzare GitHub/GitHub Pages rispetto ad altri sistemi (in particolare Google Drive e GitLab);
* come tali documenti vengono collegati alla **Knowledge Base Odoo** e agli altri moduli Odoo.

Il presente SOP è un **documento di cornice**:
definisce la **mappa delle tipologie documentali** gestite in GitHub e rimanda a SOP specifici che disciplinano in dettaglio la **redazione, gestione e aggiornamento** di ciascuna tipologia.

In particolare, il SOP disciplina:

* la classificazione delle tipologie di documentazione gestite su GitHub / GitHub Pages;
* i criteri generali per decidere se un documento debba avere **fonte di verità** in GitHub o altrove;
* il ruolo di GitHub Pages come **punto di accesso ufficiale** alla documentazione di riferimento;
* il collegamento con Odoo (Knowledge Base e moduli di processo);
* la gestione dei **template documentali**, chiarendo che i template ufficiali sono allegati ai **SOP specifici** che li regolano.

### Campo di applicazione

Il presente SOP si applica a:

* tutti i **SOP aziendali**, indipendentemente dalla macro-area (SOP-ORG, SOP-CRM, SOP-MKT, SOP-PRJ, SOP-DEV, SOP-DOC, SOP-KB, SOP-ACC, ecc.);
* la **documentazione ufficiale di riferimento**, in particolare:

  * manuali e guide di processo;
  * materiale formativo strutturato e linee guida operative interne;
  * documentazione tecnica di alto livello relativa a librerie, servizi, API aziendali;
  * policy, regolamenti interni e documentazione di governance.

Riguarda in modo particolare:

* **Responsabile Qualità / Documentazione**;
* **Responsabile IT / CTO**;
* **Responsabili di area / Owner di SOP**;
* chiunque contribuisca alla redazione e manutenzione della documentazione ufficiale.

### Esclusioni / limiti

Non rientrano nel campo del presente SOP:

* la gestione dei **documenti operativi e di lavoro** su Google Drive (disciplinata da **SOP-DOC-01**, dove Drive è repository operativo e **non** fonte di verità per la documentazione ufficiale);
* la gestione della documentazione **integrata al codice** (es. README tecnici di repository applicativi, doc generate automaticamente, commenti API inline, ecc.), per cui si rimanda a:

  * **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**
  * **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**
* la gestione dei contenuti del **sito web istituzionale**, del **blog** e delle **landing page marketing** (disciplinate da SOP-MKT-*).

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabili)

* **ISO 9001:2015** – Requisiti relativi al controllo delle informazioni documentate.
* **Regolamento (UE) 2016/679 – GDPR** – Per gli aspetti di pubblicazione ed eventuale accesso a documenti contenenti dati personali.
* Eventuali normative di settore che richiedano la presenza di procedure o manuali documentati.

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**
* **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**
* **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**

SOP di dettaglio (ipotizzati) per le singole tipologie documentali gestite in GitHub / GitHub Pages:

* **SOP-DOC-12 – Redazione, gestione e aggiornamento dei SOP aziendali**
  (disciplina nel dettaglio il ciclo di vita dei SOP: creazione, revisione, approvazione, pubblicazione, obsolescenza)

* **SOP-DOC-13 – Gestione del materiale formativo e delle linee guida interne su GitHub Pages**
  (disciplina la gestione di corsi, pillole formative, slide, linee guida operative, ecc.)

* **SOP-DOC-14 – Documentazione tecnica di librerie, servizi e API**
  (disciplina la documentazione tecnica di alto livello per componenti software, integrata con quanto previsto in SOP-DEV-01/02)

* **SOP-DOC-15 – Gestione di policy e regolamenti interni**
  (disciplina la gestione di policy aziendali, regolamenti, codici interni pubblicati su GitHub Pages)

Eventuali policy IT, policy di sicurezza, policy privacy interne.

---

## 3. Definizioni, acronimi e abbreviazioni

* **SOP (Standard Operating Procedure)** – Procedura Operativa Standard.
* **GitHub** – Piattaforma per repository Git; per questo SOP è la **fonte di verità** per la documentazione ufficiale pubblicata su GitHub Pages.
* **GitHub Pages** – Servizio di hosting di siti statici collegato a GitHub; ospita il **sito documentale aziendale** (SOP, manuali, guide, policy).
* **Repository documentazione** – Uno o più repository GitHub dedicati alla documentazione (non necessariamente coincidenti con i repository di codice).
* **Documentazione di processo** – SOP, manuali e guide che descrivono “come” l’azienda opera.
* **Materiale formativo** – Presentazioni, corsi, schede formativi, “how-to” pensati per trasferire competenze interne.
* **Documentazione tecnica (alto livello)** – Documentazione concettuale, architetturale e funzionale di librerie, servizi e API (overview, guide d’uso, scenari), distinta dalla doc strettamente integrata al codice.
* **Policy / Regolamenti interni** – Documenti che definiscono regole, vincoli, standard di comportamento e di sicurezza interni.
* **Template documentale** – Modello standard (es. .docx, .pptx, .md) da utilizzare per redigere una certa tipologia di documento; il template ufficiale è allegato al relativo SOP specifico.
* **Fonte di verità** – Sistema e posizione in cui risiede la versione ufficiale di un documento (per le tipologie trattate in questo SOP: **GitHub / GitHub Pages**).

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

La pubblicazione della documentazione su GitHub Pages riguarda trasversalmente:

* **Organizzazione & Governance** (SOP-ORG);
* **Documentazione & Gestione Documentale** (SOP-DOC);
* tutte le aree che producono documentazione “stabile” e di riferimento:

  * Commerciale & CRM
  * Marketing & Comunicazione
  * Progetti & Delivery
  * Sviluppo Software
  * Knowledge Management
  * Amministrazione & Contabilità
  * IT / Sicurezza, ecc.

Questo SOP non entra nelle modalità operative di redazione delle singole tipologie, ma stabilisce **quando e perché** esse vengono pubblicate in GitHub/GitHub Pages e **a quali SOP specifici** occorre fare riferimento.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

Legenda: **R = Responsible**, **A = Accountable**, **C = Consulted**, **I = Informed**

* **Direzione**

  * A: approvazione dei documenti strategici (SOP chiave, policy principali).
  * C/I: informata sulla strategia di gestione documentale ufficiale.

* **Responsabile Qualità / Documentazione**

  * A: governo complessivo del sistema documentale ufficiale su GitHub / GitHub Pages.
  * R: definizione e mantenimento delle **regole di classificazione** della documentazione e dei **criteri di pubblicazione**.
  * R: coordinamento della coerenza tra i vari SOP di dettaglio (**SOP-DOC-12/13/14/15**).
  * C: per la definizione di nuovi SOP documentali o modifiche significative.

* **Responsabile IT / CTO**

  * A: configurazione tecnica di GitHub e GitHub Pages (permessi, visibilità, integrazioni).
  * R: implementazione delle scelte di governance definite nel presente SOP e nei SOP correlati.
  * C: su aspetti di sicurezza, accesso e integrazione con altri sistemi (Odoo, GitLab, ecc.).

* **Responsabili di Area / Owner di SOP**

  * R: contenuti dei documenti relativi alla propria area (SOP, manuali, linee guida, doc tecniche, policy).
  * R: scelta, sulla base dei criteri di questo SOP, se e come i propri documenti debbano essere pubblicati in GitHub / GitHub Pages.
  * C: per l’aggiornamento dei SOP specifici di tipologia (**SOP-DOC-12/13/14/15**).

* **Autori / Redattori**

  * R: redazione e aggiornamento dei documenti, seguendo le regole del presente SOP e dei SOP di dettaglio.

* **Tutto il personale**

  * I: utilizzo della documentazione, tramite accesso a GitHub Pages e Odoo KB.
  * R: segnalazione di contenuti obsoleti, mancanti o incoerenti.

---

## 5. Descrizione del processo

### 5.1 Tipologie di documentazione gestite in GitHub / GitHub Pages e criteri di utilizzo

Le principali tipologie di documentazione gestite con **fonte di verità** in GitHub / GitHub Pages sono:

1. **SOP aziendali e manuali di processo**

   * Comprendono:

     * SOP di tutte le macro-aree (SOP-ORG, SOP-CRM, SOP-MKT, SOP-PRJ, SOP-DEV, SOP-DOC, SOP-KB, SOP-ACC, ecc.);
     * eventuali manuali o linee guida di processo strettamente collegati ai SOP.
   * Criterio:

     * sono documenti **normativi e di riferimento**, validi per l’intera organizzazione o per una macro-area;
     * richiedono **controllo di versione** formale e tracciabilità delle revisioni;
     * devono essere facilmente consultabili e linkabili da Odoo, da altri SOP e dalla KB.
   * Gestione di dettaglio: rimando a **SOP-DOC-12 – Redazione, gestione e aggiornamento dei SOP aziendali**.

2. **Materiale formativo e linee guida specifiche**

   * Comprendono:

     * corsi interni, pillole formative, manualetti “how-to”, slide standard di formazione;
     * linee guida operative su strumenti, processi, ruoli (es. guida all’uso di un modulo Odoo, guida al processo di onboarding).
   * Criterio:

     * contenuti **stabili o semi-stabili**, di interesse trasversale (non legati a un singolo progetto o cliente);
     * destinati a essere riutilizzati più volte nel tempo;
     * devono essere raggiungibili da Odoo KB come **materiale ufficiale** di formazione.
   * Gestione di dettaglio: rimando a **SOP-DOC-13 – Gestione del materiale formativo e delle linee guida interne su GitHub Pages**.

3. **Documentazione tecnica di librerie, servizi e API (alto livello)**

   * Comprende:

     * overview funzionali e architetturali di moduli, librerie, servizi interni;
     * guide per l’integrazione e l’utilizzo delle API;
     * descrizione delle dipendenze e dei casi d’uso principali.
   * Criterio:

     * documentazione **cross-repo** o **cross-prodotto**, non limitata al singolo repository di codice;
     * utile per sviluppatori, integratori, consulenti, e, se previsto, per alcuni clienti;
     * non sostituisce la doc integrata al codice, ma la integra con un livello più alto di sintesi.
   * Gestione di dettaglio: rimando a **SOP-DOC-14 – Documentazione tecnica di librerie, servizi e API** e alle integrazioni con **SOP-DEV-01 / SOP-DEV-02**.

4. **Policy e regolamenti interni**

   * Comprendono:

     * policy di sicurezza informatica;
     * policy sull’uso degli strumenti aziendali;
     * regolamenti interni, codici di condotta, regolamenti privacy interni, ecc.
   * Criterio:

     * documenti con valenza **normativa e vincolante** per il personale;
     * richiedono **maggiore controllo** di approvazione e di visibilità;
     * possono essere accessibili solo internamente o, ove previsto, anche a clienti/partner.
   * Gestione di dettaglio: rimando a **SOP-DOC-15 – Gestione di policy e regolamenti interni**.

In tutti i casi, GitHub / GitHub Pages costituisce la **fonte di verità** per queste tipologie documentali; eventuali copie su Drive o altri sistemi hanno funzione **operativa** o di **bozza**, ma non costituiscono la versione ufficiale.

### 5.2 Flusso operativo di alto livello (comune alle tipologie)

Indipendentemente dalla tipologia, il processo segue un flusso comune ad alto livello:

1. **Classificazione del documento**

   * L’Owner o l’Autore individua la **tipologia** (SOP, materiale formativo, doc tecnica, policy) e verifica che rientri tra quelle gestite su GitHub / GitHub Pages ai sensi del presente SOP.
   * In base alla tipologia, si applica il SOP specifico (**SOP-DOC-12/13/14/15**).

2. **Redazione e lavoro di bozza**

   * La redazione può avvenire:

     * su Google Drive (documento di lavoro), oppure
     * direttamente in GitHub (branch dedicato, file di lavoro).
   * In ogni caso, il testo e la struttura devono rispettare il template previsto dal SOP specifico.

3. **Revisione e approvazione**

   * Il documento viene revisionato secondo quanto previsto nel SOP specifico di tipologia.
   * Al termine della revisione:

     * l’Owner e il Responsabile Qualità / Documentazione validano contenuti, stato (Bozza/Emesso) e versione;
     * dove richiesto, interviene la Direzione per approvazione.

4. **Pubblicazione e aggiornamento su GitHub / GitHub Pages**

   * Il documento approvato viene reso **versione ufficiale** in GitHub;
   * GitHub Pages viene aggiornato (automatizzato o manuale, secondo le regole tecniche definite a livello IT);
   * eventuali versioni precedenti vengono marcate come obsolete o archiviate, secondo il SOP specifico.

5. **Collegamento con Odoo e altri sistemi**

   * La Knowledge Base Odoo viene aggiornata con:

     * un articolo riassuntivo;
     * il link alla pagina GitHub Pages del documento.
   * Se rilevante, i moduli Odoo (CRM, Progetti, Amministrazione, ecc.) possono contenere link diretti al documento.

6. **Monitoraggio e revisione periodica**

   * Questi documenti sono soggetti a revisione periodica (frequenza e modalità definite nei SOP specifici);
   * eventuali non conformità o feedback portano a nuove versioni.

### 5.3 Rinvio ai SOP specifici di tipologia

Per evitare di duplicare le regole di dettaglio, il presente SOP rimanda ai seguenti SOP (ipotizzati):

* **SOP-DOC-12 – Redazione, gestione e aggiornamento dei SOP aziendali**

  * definisce struttura dei SOP, metadati, iter di approvazione, regole di versione, gestione dello storico.

* **SOP-DOC-13 – Gestione del materiale formativo e delle linee guida interne su GitHub Pages**

  * definisce criteri per identificare cosa è formativo, modalità di aggiornamento, gestione di video, slide, esercizi, ecc.

* **SOP-DOC-14 – Documentazione tecnica di librerie, servizi e API**

  * definisce standard per descrivere architetture, endpoint, integrazioni;
  * chiarisce i rapporti con la doc integrata al codice e con i repository tecnici.

* **SOP-DOC-15 – Gestione di policy e regolamenti interni**

  * definisce livelli di approvazione, visibilità, obbligatorietà di presa visione, ecc.

### 5.4 Gestione dei template documentali

I **template ufficiali** delle diverse tipologie di documenti:

* non sono gestiti in un SOP unico, ma sono **allegati** ai **SOP specifici** che li regolano; ad esempio:

  * template dei SOP → allegati a **SOP-DOC-12**;
  * template di slide/formato standard per il materiale formativo → allegati a **SOP-DOC-13**;
  * template di schede tecniche, datasheet, guide API → allegati a **SOP-DOC-14**;
  * template di policy/regolamenti → allegati a **SOP-DOC-15**.

Principi:

* la **fonte di verità** dei template è sempre GitHub (nel repository documentazione);
* eventuali copie su Drive o altrove sono copie operative;
* ogni SOP specifico deve indicare chiaramente:

  * dove si trova il template ufficiale;
  * come e quando può essere aggiornato;
  * chi approva le modifiche al template.

---

## 6. Strumenti e sistemi utilizzati

* **GitHub**

  * Fonte di verità per la documentazione ufficiale descritta al §5.1.
  * Gestione delle versioni tramite Git.

* **GitHub Pages**

  * Piattaforma di pubblicazione web del sito documentale aziendale.
  * Punto di accesso unico per la consultazione dei SOP e della documentazione ufficiale.

* **Odoo**

  * **Knowledge Base**: indicizza i documenti e contiene i link alle pagine GitHub Pages.
  * Moduli operativi (CRM, Progetti, Amministrazione, ecc.): possono referenziare documenti specifici.

* **Google Drive**

  * Utilizzato come ambiente di lavoro per bozze e materiali in corso di elaborazione (fonte di verità: GitHub).
  * Integrato con Odoo per la documentazione operativa (vedi SOP-DOC-01).

* **GitLab**

  * Utilizzato per la gestione del codice sorgente e della documentazione integrata al codice;
  * può referenziare documentazione di alto livello pubblicata su GitHub Pages (es. link nei README).

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali

* **Rischio di classificazione errata**

  * Documenti che dovrebbero essere in GitHub mantenuti solo su Drive, o viceversa.

* **Rischio di incoerenza tra fonti**

  * Versioni divergenti dello stesso documento tra GitHub, Drive, Odoo KB.

* **Rischio di policy non correttamente pubblicate**

  * Policy o regolamenti non aggiornati; personale che si riferisce a versioni vecchie.

* **Rischio di scarsa reperibilità**

  * Documenti correttamente pubblicati ma difficili da trovare per mancanza di indicizzazione in KB o link nei moduli Odoo.

### 7.2 Controlli e misure di mitigazione

* Verifiche periodiche (es. annuali) sul **campione di documenti** per controllare:

  * corretta collocazione (GitHub vs Drive);
  * coerenza tra KB Odoo e GitHub Pages.

* Revisione periodica dei SOP di tipologia (**SOP-DOC-12/13/14/15**).

* Introduzione di **checklist** per i Responsabili di area quando vengono emessi nuovi documenti di riferimento.

### 7.3 KPI / Indicatori (se applicabili)

Esempi:

* **% di documenti di riferimento correttamente linkati in Odoo KB** rispetto al totale dei documenti pubblicati in GitHub Pages.
* **% SOP/documenti di riferimento revisionati negli ultimi 12 mesi** per tipologia.
* **Numero di non conformità documentali** rilevate in audit interni (ad es. documenti obsoleti o fonte di verità non chiara).

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* La **fonte di verità** del presente SOP è il file sorgente in GitHub (repository documentazione).
* La versione ufficiale è pubblicata su **GitHub Pages**.
* Un articolo in **Odoo Knowledge Base** (categoria “SOP – Documentazione & SOP Repository”) contiene:

  * codice, titolo, versione, breve descrizione;
  * link alla pagina GitHub Pages di questo SOP.

### 8.2 Revisione e aggiornamento

La revisione del presente SOP è attivata in caso di:

* introduzione di nuove tipologie documentali gestite in GitHub;
* modifica degli strumenti o della strategia di pubblicazione (es. nuovo sito documentale, nuovo tool);
* modifiche significative ai SOP di tipologia (**SOP-DOC-12/13/14/15**);
* non conformità emerse da audit o richieste della Direzione.

Ogni revisione comporta:

* aggiornamento della versione e della data di emissione;
* aggiornamento della sezione 10 – Storico revisioni;
* eventuale comunicazione interna e aggiornamento dell’articolo KB.

### 8.3 Obbligatorietà e formazione

* I **Responsabili di area** e gli **Owner di SOP** devono conoscere il presente SOP e applicarne i criteri di classificazione e pubblicazione.
* Il resto del personale deve conoscere che:

  * la documentazione di riferimento si consulta via **GitHub Pages**;
  * la KB Odoo è il punto di accesso interno ai link ufficiali.
* In caso di modifiche significative, possono essere previste brevi sessioni di formazione o comunicazioni interne specifiche.

---

## 9. Allegati (opzionale)

Esempi di allegati:

* **Allegato 1 – Schema di classificazione delle tipologie documentali**
* **Allegato 2 – Esempi di mappatura documento → sistema (GitHub vs Drive vs GitLab)**
* **Allegato 3 – Checklist per la scelta del sistema di pubblicazione**

Gli allegati, se ufficiali, hanno fonte di verità nel repository documentazione e sono pubblicati (se opportuno) su GitHub Pages.

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica           | Redatto da                   | Verificato da  | Approvato da  |
| -------- | ------------ | ------------------------------ | ---------------------------- | -------------- | ------------- |
| 1.0      | *[da comp.]* | Prima emissione del SOP-DOC-02 | *[Responsabile Qualità/Doc]* | *[Ruolo/Nome]* | *[Direzione]* |