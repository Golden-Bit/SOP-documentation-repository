# SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)

---

### 0. Metadati del documento

* **Codice SOP:** SOP-DOC-01
* **Titolo:** Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)
* **Versione:** 1.0
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Responsabile Qualità / Documentazione]*
* **Verificato da (se applicabile):** *[Ruolo/Funzionale]*
* **Approvato da:** *[Direzione]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

### Scopo

Il presente SOP definisce il **modello complessivo di gestione documentale aziendale**, descrivendo come vengono utilizzati in modo integrato:

* **Odoo** come **gestionale centrale** e “punto di verità logico” per:

  * tracciabilità dei documenti rispetto a **clienti**, **fornitori**, **progetti**, **prodotti/servizi** e **processi interni**;
  * indicizzazione e accesso ai documenti tramite **Knowledge Base (KB)** e campi link nei vari moduli.
* **Google Drive** come sistema principale di **archiviazione e condivisione dei documenti operativi** (bozze, documenti di progetto, amministrazione, marketing, ecc.).
* **GitHub / GitHub Pages** come **fonte di verità per SOP e documentazione ufficiale di riferimento**, nonché per parte della documentazione tecnica ad alto livello, in coordinamento con GitLab per la documentazione integrata al codice.

Il presente SOP:

* definisce le **famiglie documentali** e il relativo sistema di **fonte di verità** (Drive, GitHub, GitLab);
* stabilisce i **principi generali** di utilizzo di Drive e GitHub in congiunzione con Odoo;
* chiarisce il ruolo di **Odoo KB** come punto di accesso interno ai documenti ufficiali pubblicati su GitHub Pages e ai documenti operativi su Drive;
* rimanda ai SOP specifici per i **dettagli operativi**:

  * **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
    (documentazione ufficiale, SOP, manuali, policy, doc tecniche di alto livello);
  * **SOP-DOC-03 – Struttura generale Google Drive multi-organizzazione**
    (struttura generale del Drive a livello di root, macro-cartelle e logica per organizzazioni, anagrafiche, progetti, ecc.).

Ulteriori SOP di dettaglio (SOP-DOC-04 e seguenti) disciplinano in modo specifico singole aree di documentazione su Drive e su GitHub.

### Campo di applicazione

Il presente SOP si applica a **tutto il personale** (interno/esterno) che:

* crea, modifica, condivide o consulta documenti aziendali, siano essi:

  * **documenti operativi** archiviati su Google Drive;
  * **documentazione ufficiale** (SOP, manuali, policy, guide, doc tecniche) pubblicata su GitHub Pages;
  * **documentazione integrata al codice** presente in GitLab/GitHub code;
* utilizza Odoo per:

  * gestire **clienti, lead, opportunità**;
  * gestire **progetti e commesse**;
  * gestire **prodotti/servizi**;
  * gestire **amministrazione e contabilità**;
  * consultare la **Knowledge Base** e i collegamenti documentali.

Il SOP definisce **il modello e i principi**; non entra nel dettaglio di:

* struttura fisica delle cartelle su Drive (disciplinata da **SOP-DOC-03** e dai SOP DOC-04…11);
* struttura del sito documentale e delle tipologie di documentazione pubblicate su GitHub Pages (disciplinata da **SOP-DOC-02** e dai SOP DOC-12…15).

### Esclusioni / limiti

Non rientrano nel campo del presente SOP:

* la gestione del **codice sorgente** e della documentazione **strettamente integrata al codice** (disciplinata da SOP-DEV-01 e SOP-DEV-02; fonte di verità: repository GitLab / GitHub codice);
* la descrizione di dettaglio:

  * della **struttura delle cartelle** su Drive (macro-cartelle, pattern di naming, permessi, flussi operativi), trattata in **SOP-DOC-03** e SOP collegati;
  * delle modalità operative per la pubblicazione della documentazione ufficiale su GitHub Pages (branch, build, indici, gestione dei template), trattate in **SOP-DOC-02** e SOP collegati (SOP-DOC-12…15);
* la gestione delle **email** e della relativa archiviazione (disciplinate da policy IT specifiche);
* gli aspetti di **sicurezza informatica** di dettaglio (password, backup, dispositivi), disciplinati da SOP e policy IT dedicati.

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabili)

* **ISO 9001:2015** – Requisiti relativi alla gestione documentale e al controllo delle informazioni documentate.
* **Regolamento (UE) 2016/679 – GDPR** – Per la gestione dei documenti contenenti dati personali.
* Normativa fiscale e civilistica italiana (per documenti amministrativo-contabili).

*(L’elenco potrà essere ampliato in funzione di specifiche certificazioni o norme di settore.)*

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
  (contesto generale, ruoli, architettura Odoo / Drive / GitLab / GitHub / GitHub Pages)
* **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo**
* **SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo**
* **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**
* **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**
* **SOP-MKT-01 / SOP-MKT-02 – Marketing & Comunicazione, pianificazione e performance**
* **SOP-ACC-01 – Gestione contabile e tesoreria su Odoo**
* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**

SOP documentali di dettaglio:

* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
  (fonte di verità per SOP e documentazione ufficiale versionata su GitHub / GitHub Pages)
* **SOP-DOC-03 – Struttura generale Google Drive multi-organizzazione**
  (struttura root del Drive per organizzazioni, anagrafiche, progetti, ecc.)
* **SOP-DOC-04…11** – Gestione delle diverse macro-cartelle Drive (Anagrafiche, Progetti, Formazione, Contabilità, Prodotti/Servizi, Template & Grafica, Marketing, Sicurezza & Compliance).
* **SOP-DOC-12…15** – Gestione di specifiche tipologie documentali ufficiali su GitHub (SOP, materiale formativo, doc tecniche, policy).

Eventuali **policy IT**, policy di **sicurezza** e **privacy** interne.

---

## 3. Definizioni, acronimi e abbreviazioni

* **SOP (Standard Operating Procedure)** – Procedura Operativa Standard.

* **Odoo** – Gestionale ERP aziendale, punto di verità per:

  * anagrafiche (clienti, fornitori, partner);
  * progetti/commesse;
  * prodotti/servizi;
  * contabilità e amministrazione;
  * articoli di **Knowledge Base** e collegamenti a documenti esterni (Drive, GitHub, siti).

* **Google Drive (Drive)** – Sistema principale di archiviazione e condivisione **dei documenti operativi** (file di lavoro, documenti di progetto, materiali marketing, ecc.).
  Le regole di struttura e gestione operative sono descritte in **SOP-DOC-03** e nei SOP DOC-04…11.

* **GitHub / GitHub Pages** –

  * **GitHub**: repository Git utilizzato come **fonte di verità** per SOP e documentazione ufficiale di riferimento (manuali, guide, policy, doc tecniche di alto livello).
  * **GitHub Pages**: piattaforma che ospita il **sito documentale aziendale** (versione consultabile dei documenti ufficiali).

* **GitLab / GitHub (codice)** – Repository per il **codice sorgente** e la documentazione integrata al codice (README, doc generate, commenti inline). Regole in SOP-DEV-01/02.

* **Documentazione operativa (Drive)** – Documenti operativi di lavoro (bozze, report di progetto, documenti contabili operativi, presentazioni, ecc.) la cui **fonte di verità è Drive**, salvo esplicito diverso accordo.

* **Documentazione ufficiale di riferimento (GitHub)** – SOP, manuali, policy, linee guida, documentazione tecnica di alto livello la cui **fonte di verità è GitHub / GitHub Pages** (file sorgente nel repo + pubblicazione sul sito documentale).

* **Documentazione integrata al codice** – Documentazione che vive nei repository di codice (es. README, doc API generate, wiki di progetto) e ha come fonte di verità GitLab/GitHub codice.

* **KB (Knowledge Base)** – Base di conoscenza Odoo che raccoglie articoli con:

  * link ai SOP e alla documentazione ufficiale su GitHub Pages;
  * link a documenti operativi su Drive;
  * riferimenti a documentazione tecnica (GitHub / GitLab / altri siti).

* **Fonte di verità** – Sistema e posizione (Drive, GitHub, GitLab) che contengono la versione ufficiale e controllata di un documento.

Ulteriori definizioni specifiche possono essere introdotte nei SOP di dettaglio (SOP-DOC-02, SOP-DOC-03, SOP-DOC-12…15).

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

La gestione documentale integrata Odoo / Drive / GitHub riguarda trasversalmente:

* **Direzione / Management**
* **Commerciale & Marketing**
* **Progetti & Delivery**
* **Sviluppo Software**
* **Amministrazione & Contabilità**
* **Documentazione & Knowledge Management**
* **IT / Sicurezza**

Il presente SOP definisce:

* **come si ripartiscono le tipologie documentali** tra Drive, GitHub e GitLab;
* **come Odoo** viene utilizzato come “hub” per:

  * collegare documenti a clienti, fornitori, progetti, prodotti/servizi;
  * esporre i link ufficiali alla documentazione (GitHub Pages, Drive, siti esterni) tramite KB e campi link.

I dettagli operativi per:

* **documentazione ufficiale su GitHub** sono trattati in **SOP-DOC-02** e SOP collegati;
* **documentazione operativa su Drive** sono trattati in **SOP-DOC-03** e SOP collegati.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

Legenda: **R = Responsible**, **A = Accountable**, **C = Consulted**, **I = Informed**

* **Direzione**

  * A: approvazione del presente SOP e dei principali documenti ufficiali strategici (SOP, policy).
  * C/I: informata sulle principali scelte relative alla strategia documentale e ai sistemi utilizzati.

* **Responsabile Qualità / Documentazione**

  * A: governo complessivo del **modello documentale integrato** (Drive, GitHub, GitLab, Odoo).
  * R: definizione e aggiornamento del presente SOP-DOC-01.
  * R: coerenza tra le regole generali e i SOP di dettaglio (SOP-DOC-02, SOP-DOC-03, SOP-DOC-12…15).
  * C: supporto ai Responsabili di area nella classificazione dei documenti e nella scelta del sistema di fonte di verità.

* **Responsabile IT / CTO**

  * A: configurazione tecnica dei sistemi (Drive, GitHub, GitLab, Odoo) e delle relative integrazioni.
  * R: gestione permessi, gruppi, visibilità dei repository e delle unità condivise.
  * C: per la definizione di nuove tipologie documentali o cambiamenti architetturali.

* **Responsabili di Area / Owner di SOP**

  * R: contenuti dei documenti relativi alla propria area (SOP, manuali, doc tecniche, report).
  * R: corretta classificazione dei documenti tra Drive, GitHub e GitLab, in linea con il presente SOP e con SOP-DOC-02 / SOP-DOC-03.
  * C: nella definizione di nuovi SOP documentali di dettaglio.

* **Project Manager / Product Owner**

  * R: garantire che documenti chiave di progetto (operativi e ufficiali) siano correttamente archiviati nel sistema appropriato (Drive o GitHub) e collegati ai progetti Odoo.
  * C: coordinamento con Sviluppo, Commerciale, Amministrazione.

* **Tutto il personale**

  * R: rispetto delle regole generali di questo SOP per la creazione, classificazione e archiviazione dei documenti.
  * I: consapevolezza di dove si trova la fonte di verità per ciascuna tipologia documentale (Drive, GitHub, GitLab) e di come accedervi tramite Odoo/KB.

Una matrice RACI dettagliata può essere predisposta come **allegato** (vedi sezione 9).

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il processo di gestione documentale integrata Odoo / Drive / GitHub comprende le seguenti macro-attività:

1. **Classificazione della tipologia documentale**

   * identificare se un contenuto è:

     * documento operativo di lavoro (Drive),
     * documentazione ufficiale di riferimento (GitHub),
     * documentazione integrata al codice (GitLab/GitHub codice),
     * o combinazione (es. bozza su Drive → versione ufficiale su GitHub).

2. **Scelta del sistema di fonte di verità**

   * in base alla tipologia, si decide se:

     * la fonte di verità sarà **Google Drive** (documenti operativi, materiali di progetto, documenti contabili operativi, ecc.);
     * la fonte di verità sarà **GitHub / GitHub Pages** (SOP, manuali, policy, doc tecniche di alto livello);
     * la fonte di verità sarà **GitLab/GitHub codice** (doc integrata al codice).

3. **Redazione e gestione nel sistema scelto**

   * redazione, revisione, approvazione e versionamento sono gestiti secondo i SOP specifici:

     * SOP-DOC-02 e SOP-DOC-12…15 per doc ufficiale su GitHub;
     * SOP-DOC-03 e SOP-DOC-04…11 per doc operativa su Drive;
     * SOP-DEV-01/02 per doc integrata al codice.

4. **Collegamento a Odoo**

   * i documenti vengono collegati ai record Odoo rilevanti (clienti, progetti, prodotti, processi) tramite:

     * campi link;
     * allegati;
     * articoli di **Knowledge Base**.

5. **Consultazione e aggiornamento**

   * il personale accede ai documenti principalmente:

     * tramite Odoo (record + KB);
     * tramite il sito documentale GitHub Pages;
     * tramite le unità Drive strutturate.
   * ogni aggiornamento significativo segue il relativo flusso SOP (SOP-DOC-02, SOP-DOC-03, ecc.) e viene riflesso in Odoo (KB, link, riferimenti).

### 5.2 Criteri di scelta del sistema (Drive, GitHub, GitLab)

Per garantire coerenza, si adottano i seguenti criteri:

1. **Google Drive – Documentazione operativa**

   * **Quando**: documenti di lavoro, materiali di progetto, file amministrativi operativi, record di attività, presentazioni di singoli progetti, bozze di SOP o manuali, ecc.
   * **Fonte di verità**: Drive è fonte di verità per questi documenti, salvo esplicito trasferimento in GitHub come documentazione ufficiale.
   * **Dettaglio operativo**: in **SOP-DOC-03** (struttura generale Drive) e SOP-DOC-04…11 (macro-cartelle Drive).

2. **GitHub / GitHub Pages – Documentazione ufficiale di riferimento**

   * **Quando**: SOP aziendali, manuali di processo, policy, regolamenti interni, documentazione tecnica di alto livello (es. architetture, overview servizi/API), materiale formativo istituzionale.
   * **Fonte di verità**: GitHub (file sorgente) e GitHub Pages (versione consultabile).
   * **Dettaglio operativo**: in **SOP-DOC-02** e nei SOP-DOC-12…15.

3. **GitLab / GitHub (codice) – Documentazione integrata al codice**

   * **Quando**: doc che deve vivere insieme al codice (README, wiki tecniche di repo, doc API generate automaticamente, commenti, ecc.).
   * **Fonte di verità**: repository di codice.
   * **Dettaglio operativo**: SOP-DEV-01 e SOP-DEV-02.

4. **Relazioni tra i sistemi**

   * Un documento **può nascere in Drive** (bozza) ed essere poi trasformato in documentazione ufficiale su GitHub (SOP, manuale, guida).
   * In questi casi:

     * Drive rimane eventuale repository di lavoro;
     * GitHub diventa la **fonte di verità** per la versione ufficiale;
     * Odoo/KB punta alla versione su GitHub Pages, non alle copie su Drive.

### 5.3 Integrazione con Odoo e Knowledge Base

Odoo funge da **hub di accesso** alla documentazione, tramite:

1. **Moduli operativi (CRM, Progetti, Amministrazione, Prodotti, ecc.)**

   * Nei record di:

     * **clienti/fornitori/partner** → link a cartelle/doc operativi su Drive, eventuali manuali o contratti ufficiali (GitHub Pages o PDF su Drive).
     * **progetti/commesse** → link a cartelle di progetto su Drive, report chiave, eventuale documentazione ufficiale (manuali, guide) su GitHub Pages.
     * **prodotti/servizi** → link a:

       * documentazione marketing e commerciale (Drive, se operativa);
       * schede tecniche e manuali ufficiali (GitHub Pages).
     * **documenti contabili** → eventuali allegati o link a file giustificativi su Drive.

2. **Knowledge Base (KB) Odoo**

   * La KB ospita articoli che:

     * descrivono sinteticamente SOP, manuali, policy, guide;
     * contengono link alla pagina GitHub Pages corrispondente (fonte di verità);
     * possono includere link a template operativi su Drive (ad es. modelli per offerte, report, presentazioni);
     * rimandano a doc tecniche su GitHub/GitLab o ad altri siti (es. documentazione pubblica di terze parti).

3. **Principi generali di collegamento**

   * KB e moduli Odoo devono sempre puntare:

     * alla **fonte di verità** (GitHub Pages per doc ufficiale; Drive per doc operativa; repository di codice per doc integrata al codice);
     * evitando di creare link a copie locali o non versionate.
   * Qualora un documento cambi fonte di verità (es. da Drive a GitHub):

     * si aggiorna l’articolo KB;
     * si aggiornano i link nei record Odoo interessati.

### 5.4 Flusso di alto livello (esempi tipo)

Senza entrare nei dettagli operativi (coperti da SOP-DOC-02/03 e successivi), il presente SOP descrive i **pattern tipici**:

1. **Nuovo progetto cliente**

   * Creazione record **Progetto** in Odoo (vedi SOP-PRJ-01).
   * Apertura cartella di progetto su Drive secondo SOP-DOC-03.
   * Collegamento in Odoo → link cartella Drive.
   * Eventuale creazione di materiale di riferimento (guide, SOP) → gestione come documentazione ufficiale su GitHub (SOP-DOC-02) e link in KB/Progetto.

2. **Nuovo SOP aziendale**

   * Bozza iniziale (Drive o direttamente GitHub).
   * Classificazione come documentazione ufficiale → fonte di verità in GitHub.
   * Pubblicazione su GitHub Pages secondo SOP-DOC-02.
   * Creazione/aggiornamento articolo KB con link al SOP.

3. **Nuova procedura operativa non normativa (es. checklist di progetto interna)**

   * Se destinata a singolo progetto o a uso operativo limitato → fonte di verità su Drive (SOP-DOC-03 + SOP-DOC-05 per cartelle Progetti).
   * Se diventa standard aziendale a lungo termine → trasformazione in SOP/guida ufficiale su GitHub (SOP-DOC-02 + SOP-DOC-12).

---

## 6. Strumenti e sistemi utilizzati

* **Odoo**

  * Gestionale centrale e punto di verità logico per:

    * anagrafiche, progetti, prodotti/servizi, contabilità;
    * KB e collegamenti documentali.
  * Integrazione con Drive (link a cartelle/file) e con GitHub/GitLab (link a doc ufficiali e doc tecniche).

* **Google Drive**

  * Archiviazione e condivisione di documentazione operativa.
  * Struttura generale e gestione definite in SOP-DOC-03 e SOP-DOC-04…11.

* **GitHub / GitHub Pages**

  * Fonte di verità per SOP e documentazione ufficiale (manuali, policy, doc tecniche di alto livello, materiale formativo istituzionale).
  * Modalità di gestione e pubblicazione definite in SOP-DOC-02 e SOP-DOC-12…15.

* **GitLab / GitHub (codice)**

  * Fonte di verità per il codice sorgente e la documentazione integrata al codice.
  * Modalità operative definite in SOP-DEV-01 e SOP-DEV-02.

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali del processo

* **Rischio di incoerenza tra sistemi**

  * Documento aggiornato su Drive, ma non su GitHub (o viceversa).
  * KB Odoo che punta a file obsoleti o non alla fonte di verità.

* **Rischio di classificazione errata**

  * Documenti che dovrebbero essere SOP/manuali ufficiali (GitHub) tenuti solo su Drive.
  * Documenti operativi di progetto erroneamente trattati come documentazione ufficiale.

* **Rischio di mancata tracciabilità**

  * Progetti, prodotti o clienti privi di link alla documentazione rilevante.
  * Documentazione tecnica dispersa tra Drive, GitHub e GitLab senza mappa chiara.

* **Rischio di accesso non autorizzato**

  * Permessi non corretti su Drive, GitHub o GitLab, con possibile esposizione di dati sensibili.

* **Rischio di utilizzo di documenti obsoleti**

  * SOP o policy superate non marcate come tali e ancora linkate dalla KB o dai moduli Odoo.

### 7.2 Controlli e misure di mitigazione

* **Verifiche periodiche (es. annuali) di coerenza**

  * Campionamento di SOP, manuali, policy:

    * verifica che la fonte di verità sia GitHub/GitHub Pages;
    * controllo che la KB Odoo punti correttamente a tali fonti.
  * Campionamento di progetti e clienti:

    * verifica dell’esistenza di cartelle Drive corrette;
    * verifica dei link a documentazione ufficiale.

* **Audit documentali interni**

  * Controllo dell’applicazione dei criteri di scelta sistema (Drive vs GitHub vs GitLab).
  * Verifica di permessi e condivisioni critiche.

* **Allineamento periodico dei SOP documentali**

  * Revisione di SOP-DOC-01, SOP-DOC-02, SOP-DOC-03, SOP-DOC-12…15 per mantenerli coerenti con l’evoluzione degli strumenti.

### 7.3 KPI / Indicatori

Esempi di KPI:

* **% di articoli KB che puntano alla fonte di verità corretta** (GitHub Pages, Drive, GitLab).
* **% di progetti con documentazione chiave collegata in Odoo** (cartella Drive + eventuali manuali GitHub).
* **% di SOP/documenti ufficiali revisionati negli ultimi 12 mesi**.
* **Numero di non conformità documentali** rilevate in audit / trimestre.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* La **fonte di verità** del presente SOP è il file sorgente nel **repository GitHub documentazione**, come definito in SOP-DOC-02.
* La versione ufficiale approvata e consultabile è pubblicata su **GitHub Pages**.
* Un articolo in **Odoo KB** (categoria “SOP – Documentazione & Gestione Documentale”) contiene:

  * codice, titolo, versione;
  * breve descrizione del modello integrato;
  * link alla pagina GitHub Pages del presente SOP.

### 8.2 Revisione e aggiornamento

La revisione del presente SOP è attivata in caso di:

* modifiche significative al modello documentale (nuovi sistemi, cambi di strategia tra Drive/GitHub/GitLab);
* modifiche rilevanti a SOP-DOC-02, SOP-DOC-03 o ai SOP documentali di dettaglio;
* non conformità emerse in audit o richieste della Direzione.

Ogni revisione comporta:

* aggiornamento del numero di versione;
* aggiornamento della data di emissione;
* registrazione delle modifiche nella **sezione 10 – Storico revisioni**;
* comunicazione interna e aggiornamento dell’articolo KB.

### 8.3 Obbligatorietà e formazione

* Tutto il personale coinvolto nella creazione/gestione di documenti deve:

  * conoscere il presente SOP per la parte di pertinenza;
  * sapere dove risiede la fonte di verità dei diversi tipi di documenti.
* In occasione della prima emissione e delle revisioni significative:

  * possono essere organizzati brevi momenti di formazione;
  * può essere richiesta la presa visione del SOP tramite Odoo KB.

---

## 9. Allegati (opzionale)

Possibili allegati:

* **Allegato 1 – Schema grafico del modello integrato Odoo / Drive / GitHub / GitLab**
* **Allegato 2 – Tabella di mappatura tipologia documentale → fonte di verità (Drive / GitHub / GitLab)**
* **Allegato 3 – Esempi di casi d’uso (progetto, prodotto, policy)**

Gli allegati, se ufficiali, hanno fonte di verità nel repository GitHub documentazione e, se opportuno, sono pubblicati su GitHub Pages.

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica                                                    | Redatto da                   | Verificato da  | Approvato da  |
| -------- | ------------ | ----------------------------------------------------------------------- | ---------------------------- | -------------- | ------------- |
| 1.0      | *[da comp.]* | Prima emissione del SOP-DOC-01 come modello integrato Odoo/Drive/GitHub | *[Responsabile Qualità/Doc]* | *[Ruolo/Nome]* | *[Direzione]* |