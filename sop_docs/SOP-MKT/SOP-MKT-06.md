# SOP-MKT-06 – Gestione Google (SEO, Google Ads e ricerca lead)

---

### 0. Metadati del documento

* **Codice SOP:** SOP-MKT-06
* **Titolo:** Gestione Google (SEO, Google Ads e ricerca lead)
* **Versione:** 0.1
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Responsabile Marketing / Growth]*
* **Verificato da (se applicabile):** *[Responsabile Commerciale / Sales Lead]*
* **Approvato da:** *[Direzione / CEO]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

### 1.1 Scopo

Il presente SOP definisce come l’azienda utilizza l’**ecosistema Google** per:

* **farsi trovare** dai potenziali clienti B2B tramite **ricerca organica (SEO)**;
* **intercettare domanda attiva** tramite **Google Ads** (ricerca, eventualmente display/YouTube);
* svolgere **ricerca manuale di lead B2B su Google** (prospecting outbound) con particolare focus su:

  * **aziende di finanza agevolata**;
  * **aziende informatiche / software house / agenzie digital** che hanno necessità di esternalizzare sviluppo o DevOps;
* assicurare che i **lead generati o identificati tramite Google** siano:

  * registrati correttamente in **Odoo CRM**,
  * **non duplicati**,
  * qualificati e instradati verso il processo commerciale (SOP-CRM-01).

Il SOP disciplina:

* la **strategia e governance SEO** (on‑site e, ove rilevante, off‑site);
* la **pianificazione e gestione delle campagne Google Ads**;
* il **processo strutturato di ricerca lead su Google** (ricerche manuali, raccolta dati, deduplica, creazione lead);
* il **collegamento dati / tracking** tra Google (Analytics, Ads, Search Console) e Odoo;
* il **monitoraggio continuo** e il miglioramento del canale Google.

> **Nota:** questo SOP **non fissa obiettivi numerici** (es. n° lead/mese, budget Ads, soglie KPI), che sono definiti in **allegati operativi** (piano Google, schede KPI, ecc.).

### 1.2 Campo di applicazione

Il SOP si applica a tutte le attività che coinvolgono:

* **SEO** del sito web, blog e landing page aziendali;
* **campagne Google Ads** (rete di ricerca, eventuali campagne display o YouTube collegate al business B2B);
* utilizzo di **Google come strumento di ricerca lead** (manuale/outbound);
* **raccolta e tracciamento dei lead** provenienti da:

  * traffico organico Google → form sito/landing;
  * Google Ads → form, call, richieste;
  * ricerca manuale lead.

Coinvolge principalmente:

* Area **Marketing & Comunicazione** (SEO, Ads, strategia Google);
* Area **Commerciale / Sales & CRM** (gestione lead generati o identificati tramite Google);
* Area **Sviluppo / Web** (implementazione tecnica di sito, landing, tracking);
* eventuale **Data/BI** se presente (cruscotti).

Sono esclusi:

* altri motori di ricerca e piattaforme adv non Google (disciplinati da SOP dedicati, se previsti);
* la gestione tecnica approfondita del sito, che è coperta da **SOP-MKT-05 – Gestione sito web, blog e landing page** (quando redatto).

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabile)

* **Regolamento (UE) 2016/679 – GDPR**
  Per il trattamento dei dati personali raccolti tramite form, eventi di conversione, tracciamenti.

* **Normativa nazionale su cookie, tracciamento e comunicazioni commerciali**
  (es. Cookie law, ePrivacy, norme su pubblicità e trasparenza delle offerte).

* **Policy Google Ads e norme di Google**
  (termini di servizio, norme sugli annunci, restrizioni di contenuto e targeting).

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
  Per il contesto generale di sistemi e integrazioni (Odoo, Drive, Git, GitHub Pages).

* **SOP-MKT-01 – Immagine aziendale, comunicazione e gestione dei canali marketing**
  Quadro generale di branding, tono di voce, gestione canali.

* **SOP-MKT-02 – Pianificazione marketing, lead generation e misurazione delle performance**
  Riferimento per:

  * pianificazione strategica e budget;
  * definizione MQL/SQL;
  * framework KPI complessivo.

* **SOP-MKT-03 – Gestione canale LinkedIn**
  Per coordinare le attività Google con le attività LinkedIn (cross‑canale, campagne integrate, messaggi coerenti).

* **SOP-MKT-05 – Gestione sito web, blog e landing page** (da redigere)
  Per il dettaglio operativo su:

  * aggiornamento contenuti;
  * struttura pagine;
  * aspetti tecnici del sito (performance, mobile, ecc.).

* **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo**
  Per il ciclo di vita lead/opportunità, pipeline, assegnazioni e antduplicazione nel CRM.

* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
  Per l’archiviazione di:

  * piani keyword;
  * piani campagne;
  * report SEO/Ads;
  * export dati.

* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
  Per eventuali materiali tecnici/marketing legati alle pagine target.

* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**
  Per articoli interni che descrivono best practice SEO/Ads e procedure.

* **SOP-ALLEGATI-STANDARD.md – Catalogo allegati standard per i SOP aziendali**
  Per la scelta e classificazione degli allegati (diagrammi, WI, template, ecc.).

---

## 3. Definizioni, acronimi e abbreviazioni

* **SEO (Search Engine Optimization)** – Insieme di attività per migliorare la visibilità organica del sito nei risultati di ricerca.

* **SEA / Google Ads** – Attività di advertising a pagamento su Google (principalmente rete di ricerca; eventualmente display/YouTube).

* **SERP (Search Engine Results Page)** – Pagina dei risultati di ricerca di Google.

* **Keyword / Parola chiave** – Termine o frase di ricerca per cui si vuole apparire in organico o con annunci.

* **Campagna (Ads)** – Struttura di alto livello in Google Ads che contiene gruppi di annunci con obiettivi e budget.

* **Gruppo di annunci** – Sottoinsieme di una campagna che raccoglie annunci e keyword strettamente correlati.

* **Landing page** – Pagina web dedicata, progettata per una specifica offerta/azione (richiesta di contatto, call, demo, ecc.).

* **Conversione** – Azione compiuta dall’utente che rappresenta un obiettivo (es. invio form, richiesta contatto).

* **UTM** – Parametri aggiunti alle URL per tracciare sorgente, mezzo e campagna nelle analytics.

* **Ricerca manuale lead su Google** – Attività outbound che utilizza Google per individuare aziende target, visitare i siti, raccogliere dati chiave e alimentare il CRM.

* **MQL / SQL** – Marketing Qualified Lead / Sales Qualified Lead, come definiti in SOP-MKT-02 e SOP-CRM-01.

* **Work Instruction (WI) / How‑to** – Istruzioni operative dettagliate (clic‑per‑clic), spesso con screenshot, collegate a questo SOP come allegati.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

L’azienda opera B2B fornendo:

* **sviluppo software** e servizi digitali;
* **servizi DevOps / CI/CD / Cloud**.

Google è utilizzato in tre modi principali:

1. **SEO** – far trovare l’azienda da potenziali clienti che cercano soluzioni/servizi affini.
2. **Google Ads** – intercettare domanda attiva per servizi specifici (DevOps, sviluppo, verticali come finanza agevolata, ecc.).
3. **Ricerca manuale lead su Google** – individuare aziende target (finanza agevolata, software house, agenzie digital) per attività di outbound.

Il processo coinvolge in modo trasversale:

* Marketing (SEO, Ads, strategia);
* Sales (lavorazione lead e prospect trovati via Google);
* Web/Dev (tecnica sito e tracking);
* Direzione (approvazione priorità e budget).

### 4.2 Ruoli e responsabilità (RACI di alto livello)

* **Direzione / CEO**

  * **A**: approvazione budget Google Ads, priorità di canale, scelte strategiche (es. vertical da presidiare).
  * **C**: definizione posizionamento e messaggi chiave.
  * **I**: informata sui risultati complessivi (report periodici).

* **Responsabile Marketing / Growth**

  * **A**: governance complessiva dell’utilizzo di Google.
  * **R**: definizione strategia SEO/Ads, linee guida per ricerca lead.
  * **R**: approvazione piani keyword, piani campagne, priorità verticali.
  * **C**: con Sales e Tech per offerte, fattibilità e messaggi.
  * **I**: aggiornato su qualità lead, conversioni, feedback dal commerciale.

* **SEO Specialist / Web Marketing (se presente)**

  * **R**: analisi keyword, ottimizzazioni SEO on‑site, monitoraggio Search Console.
  * **C**: con sviluppatori per implementazioni tecniche.

* **Performance Marketer / Google Ads Specialist (se presente)**

  * **R**: configurazione, gestione e ottimizzazione campagne Google Ads.
  * **R**: monitoraggio budget, CPC, conversioni.
  * **C**: con Responsabile Marketing e Sales per allineare offerte, landing, messaggi.

* **Team Sviluppo / Web Developer**

  * **R**: implementazione tecnica di:

    * landing page e pagine servizi;
    * eventi di tracciamento analytics;
    * integrazione tra form sito e Odoo;

  * **C**: con Marketing su priorità e requisiti tecnici.

* **Responsabile Commerciale / Sales Lead**

  * **A**: gestione pipeline commerciale a valle dei lead Google.
  * **C**: definizione dei criteri MQL/SQL e feedback su qualità dei lead.
  * **I**: informato su performance Ads/SEO che influenzano la pipeline.

* **Sales / Business Developer**

  * **R**: lavorazione lead Google (follow‑up, call, opportunità in Odoo).
  * **R**: partecipazione alla **ricerca manuale lead su Google** (prospecting) secondo le linee guida.
  * **C**: con Marketing per feedback su tipologie di aziende trovate e messaggistica.

Una **matrice RACI dettagliata** può essere predisposta come allegato (es. “Allegato 2 – Matrice RACI Google”).

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il processo di gestione Google si sviluppa in 7 macro‑fasi:

1. **Pianificazione strategia Google** (SEO + Ads + ricerca manuale lead).
2. **Setup tecnico e tracking** (Analytics, Tag Manager, Search Console, conversioni).
3. **Gestione SEO (on‑site e di base off‑site)**.
4. **Gestione campagne Google Ads**.
5. **Ricerca manuale lead su Google** e raccolta informazioni.
6. **Raccolta, registrazione e qualifica lead in Odoo CRM** (inclusa deduplica).
7. **Monitoraggio KPI e miglioramento continuo**.

Le istruzioni operative di dettaglio (configurazioni, screenshot, script, esempi di query Google, ecc.) sono fornite in **Work Instructions / How‑to** allegati, non nel corpo del SOP.

---

### 5.2 Flusso operativo di alto livello

1. **Pianificazione**

   * Input: Piano marketing (SOP-MKT-02), storico SEO/Ads, budget disponibile, priorità settori (finanza agevolata, software house, ecc.).
   * Output: Piano Google (SEO+Ads+ricerca lead) con:

     * cluster keyword;
     * pagine da creare/ottimizzare;
     * campagne Ads da attivare o ottimizzare;
     * linee guida per ricerca manuale lead.

2. **Setup tecnico**

   * Configurazione/aggiornamento:

     * Analytics (o sistema di analytics usato);
     * Google Tag Manager;
     * Search Console;
     * conversioni Ads;
     * form collegati a Odoo (SOP-MKT-05 / SOP-CRM-01).

3. **SEO**

   * Analisi keyword;
   * ottimizzazioni pagine esistenti;
   * creazione nuove pagine/landing verticali;
   * monitoraggio posizionamenti e traffico organico.

4. **Google Ads**

   * Struttura campagne (ricerca + eventuale display/YouTube);
   * configurazione targeting, keyword, annunci;
   * monitoraggio e ottimizzazione continua.

5. **Ricerca manuale lead su Google**

   * uso di Google per trovare aziende target (finanza agevolata, software house, agenzie);
   * raccolta dati essenziali;
   * integrazione con Odoo evitando duplicati.

6. **Registrazione lead in Odoo e passaggio a Sales**

   * creazione/aggiornamento lead con fonte corretta;
   * prima qualifica marketing (MQL/non MQL);
   * assegnazione al commerciale (SOP-CRM-01).

7. **Monitoraggio e miglioramento**

   * raccolta KPI da Google e Odoo;
   * analisi periodica;
   * azioni di ottimizzazione (SEO, Ads, ricerca lead, landing).

---

### 5.3 Istruzioni operative / Dettaglio per fasi

#### 5.3.1 Pianificazione strategia Google (SEO, Ads, ricerca lead)

Attività principali:

* **Allineamento con Piano Marketing (SOP-MKT-02)**
  Identificare:

  * servizi/offer prioritari da promuovere (DevOps, sviluppo su misura, verticali);
  * segmenti target (finanza agevolata, software house, agenzie digital);
  * ruoli e fasi del funnel da supportare (awareness, consideration, decision).

* **Definizione cluster di keyword**

  * cluster per **intento di ricerca**:

    * informativo (guide, “come fare…”);
    * transazionale (servizi, “sviluppo software per…”, “consulenza DevOps”);
    * branded (nome azienda, brand, prodotti).
  * cluster per **settore target**:

    * finanza agevolata (es. digitalizzazione bandi, portali, CRM per finanza agevolata);
    * software house/agency (es. outsourcing sviluppo, DevOps esterno, team augmentation).

* **Scelta mix SEO / Ads / ricerca manuale**

  * SEO: quali pagine ottimizzare o creare;
  * Ads: per quali intenti/servizi conviene attivare ricerca a pagamento;
  * Ricerca manuale: quali query useremo per scovare aziende target dove non c’è ancora domanda esplicita.

Il risultato è un **Piano Google** (SEO+Ads+ricerca lead) archiviato come allegato (es. “Allegato 3 – Piano Google SEO/Ads & ricerca lead”).

---

#### 5.3.2 Setup tecnico e tracking

Attività principali:

* **Analytics & Tag Manager**

  * verificare che il sito utilizzi un sistema di analytics (es. Google Analytics o Matomo);
  * se si usa Google Tag Manager:

    * controllare che sia installato correttamente;
    * configurare tag per:

      * pageview;
      * eventi (click CTA, invio form);
      * chiamate telefoniche (se tracciate).

* **Search Console**

  * collegare sito a Search Console;
  * verificare:

    * sitemap;
    * copertura (pagine indicizzate / errori);
    * eventuali segnalazioni (manual actions, problemi mobile, ecc.).

* **Tracciamento conversioni Ads**

  * configurare conversioni in Google Ads (import da Analytics o tag dedicati);
  * definire conversioni principali:

    * invio form contatto;
    * richiesta preventivo;
    * prenotazione call (se c’è una pagina di conferma);
  * assicurarsi che le landing usate per Ads abbiano tracking corretto.

* **Collegamento con Odoo**

  * garantire che i form di contatto/lead from sito/landing creino lead in Odoo (SOP-CRM-01, SOP-MKT-05);
  * definire mapping dei **campi di fonte** in Odoo:

    * “Google – organico”
    * “Google – Ads ricerca”
    * “Google – ricerca manuale (outbound)”
    * ecc.

I dettagli tecnici (config GA, Tag Manager, conversioni Ads) vengono descritti in WI dedicate (es. “WI-MKT-06-01 – Setup tracking Google” e simili).

---

#### 5.3.3 Gestione SEO (on‑site e di base off‑site)

Attività principali:

1. **Ricerca e mappatura keyword**

   * analizzare:

     * query esistenti da Search Console;
     * keyword potenziali con strumenti dedicati (anche gratuiti);
   * mappare keyword→pagine (es. foglio “Keyword mapping”).

2. **Ottimizzazione on‑site**

   Per ciascuna pagina:

   * assicurarsi di avere:

     * titolo (title) coerente e sintetico;
     * meta description descrittiva e con CTA;
     * heading strutturati (H1, H2…);
     * testo che risponda in modo chiaro all’intento di ricerca;
     * link interni verso altre pagine rilevanti (servizi, case study).

   * curare in particolare landing dedicate a:

     * servizi per finanza agevolata;
     * servizi per software house/agency (outsourcing sviluppo, DevOps esterno, team augmentation).

3. **Creazione/aggiornamento contenuti**

   * pubblicare e aggiornare regolarmente:

     * pagine servizi;
     * articoli blog/guide;
     * pagine verticali per settore (es. “Soluzioni per società di finanza agevolata”);
   * coordinare SEO con altri canali:

     * LinkedIn e YouTube possono spingere traffico verso queste pagine.

4. **Monitoraggio SEO**

   * controllare periodicamente:

     * trend di impression/click/posizione su query chiave (Search Console);
     * traffico organico (Analytics);
     * pagine con errori o problemi di copertura.

   * identificare opportunità:

     * pagine che già generano impression ma bassa CTR (ottimizzare snippet);
     * query per cui siamo in posizioni 5–15 ma con potenziale.

I dettagli operativi (es. come svolgere un SEO audit base, come compilare la keyword map) sono descritti in WI/How‑to dedicate.

---

#### 5.3.4 Gestione campagne Google Ads

Attività principali:

1. **Strutturazione account e convenzioni di naming**

   * definire convenzioni di nomenclatura per:

     * campagne (es. `PAESE_SERVIZIO_INTENTO`);
     * gruppi di annunci (cluster keyword stretti);
     * annunci (variante A/B/C).

   * distinguere campagne per:

     * servizi (DevOps, sviluppo su misura, verticali);
     * fasi del funnel (ricerca diretta di servizio vs. termini più generici).

2. **Configurazione campagne di ricerca**

   * scelta tipo campagna (ricerca “pura” per B2B, eventuale brand protection);

   * impostazione:

     * budget giornaliero;
     * area geografica;
     * lingua;
     * strategie di offerta (da definire in base all’esperienza interna).

   * definizione gruppi di annunci:

     * ciascun gruppo con keyword strettamente correlate;
     * annunci testuali che riflettono:

       * promessa di valore chiara;
       * target (es. “per software house”, “per società di finanza agevolata”).

3. **Landing page e coerenza messaggio**

   * ogni campagna/gruppo di annunci deve puntare a una landing/pagina:

     * coerente con la keyword e l’annuncio;
     * con CTA chiara (richiesta contatto, richiesta call, ecc.);
     * con tracking e collegamento a Odoo.

4. **Monitoraggio e ottimizzazione**

   * controllo regolare di:

     * CTR;
     * CPC;
     * tasso di conversione (visite → lead);
     * ricerche effettive (search terms) per escludere ricerche non pertinenti.

   * azioni tipiche:

     * aggiunta di negative keywords;
     * test di nuovi annunci;
     * spostamento budget verso campagne/gruppi performanti;
     * disattivazione di ciò che non converte.

Gli aspetti molto pratici (creazione campagna, esempi di annunci, negative list) sono dettagliati in WI (es. “WI-MKT-06-02 – Creazione e gestione campagne Google Ads”).

---

#### 5.3.5 Ricerca manuale lead su Google (prospecting outbound)

Oltre a SEO e Ads, Google viene usato per **trovare aziende target** per attività outbound, in particolare:

* **aziende di finanza agevolata**;
* **aziende informatiche / software house / agenzie digital** che possono avere bisogno di sviluppo/DevOps in esterno.

Attività principali:

1. **Definizione query di ricerca**

   Esempi (da adattare e aggiornare):

   * Finanza agevolata:

     * `"finanza agevolata" consulenza imprese`
     * `"finanza agevolata" "PMI"`
     * `"consulenza" "bandi europei"`

   * Software house / agenzie:

     * `"software house" sviluppo web`
     * `"sviluppo software su misura" azienda`
     * `"agenzia digitale" "sviluppo app"`

   * Query combinate con località (es. “Milano”, “Lombardia”, ecc.) se rilevante.

   (Una lista aggiornata di query suggerite può essere mantenuta come allegato / WI.)

2. **Selezione aziende e raccolta informazioni**

   * per ogni azienda trovata:

     * visitare il sito;
     * identificare:

       * ragione sociale;
       * indirizzo;
       * sito web;
       * eventuale pagina “Team” / “Chi siamo” / “Lavora con noi” (indicatore di attività sviluppo);
       * contatti (email, telefono, form, pagina LinkedIn).

   * facoltativamente annotare:

     * tecnologie citate;
     * servizi offerti (per capire se emergono possibili sinergie/outsourcing/DevOps).

3. **Registrazione lead potenziale in Odoo (con controllo duplicati)**

   * **Prima di creare un nuovo lead**, ricercare in Odoo:

     * per *nome azienda*;
     * per *dominio e‑mail* (es. `@azienda.it`);
     * per *partita IVA* (se disponibile).

   * Se l’azienda è **già presente**:

     * verificare se esiste già un lead/opportunità corrente;
     * aggiornare il record esistente con:

       * note sulla fonte (“Ricerca manuale Google”);
       * eventuali nuovi contatti o informazioni;
       * proposta di prossimi passi (es. contatto via email/LinkedIn).

   * Se l’azienda **non esiste**:

     * creare nuovo lead in Odoo secondo SOP-CRM-01, valorizzando:

       * nome lead (es. `Software house – Nome Azienda – Ricerca Google`);
       * azienda;
       * fonte = `Google – ricerca manuale` (specifica);
       * tag (es. `SOFTWARE_HOUSE`, `FINANZA_AGEVOLATA`, `POTENZIALE_PARTNER`);
       * note con:

         * query usata;
         * motivi d’interesse;
         * link al sito.

   * Dettagli passo‑passo per ricerca antduplicato e creazione lead sono in una WI dedicata (es. “WI-MKT-06-03 – Ricerca lead su Google e creazione lead in Odoo senza duplicati”).

4. **Passaggio a Sales e coordinamento con altri canali**

   * una volta identificato il prospect:

     * definire chi è l’**owner commerciale**;
     * concordare la **prima azione di contatto** (es. email, LinkedIn, call di presentazione);
     * coordinare eventuale contatto LinkedIn (vedi SOP-MKT-03) per massimizzare le possibilità di risposta.

   * eventuali script email/messaggi standard possono essere raccolti in un allegato (“Script contatto lead trovati da Google”).

---

#### 5.3.6 Raccolta, registrazione e qualifica lead da Google (SEO + Ads)

Attività principali:

1. **Punti di ingresso lead**

   * form contatto sul sito;
   * form su landing dedicate;
   * eventuali form specifici da campagne Ads;
   * click su CTA che portano a richiesta call/democall.

2. **Creazione lead automatica o semi‑automatica**

   * garantire che:

     * i form siano integrati con Odoo (SOP-CRM-01, SOP-MKT-05);
     * siano mappati i campi:

       * nome;
       * azienda;
       * email/telefono;
       * messaggio;
       * **fonte/medium** (es. `google / organic`, `google / cpc`, parametri UTM).

3. **Verifica e arricchimento**

   * Marketing/Commerciale verifica periodicamente nuovi lead con fonte Google:

     * controlla la completezza dei dati;
     * aggiunge tag (es. `DEVOPS`, `SVILUPPO`, `FINANZA_AGEVOLATA`, `SOFTWARE_HOUSE`);
     * aggiunge note su:

       * pagina di origine;
       * eventuali informazioni di contesto.

4. **Prima qualifica (MQL)**

   * utilizzo dei criteri MQL definiti in SOP-MKT-02 / allegato MQL per:

     * capire se il lead è potenzialmente in target;
     * decidere se passarlo immediatamente a Sales o inserirlo in eventuali flussi di nurturing (se previsti).

5. **Passaggio a pipeline commerciale**

   * in caso di MQL:

     * assegnare owner commerciale;
     * impostare la **prossima attività** (telefonata, email, proposta di call);
     * seguire SOP-CRM-01 per avanzamento a opportunità.

---

#### 5.3.7 Monitoraggio, reporting e miglioramento continuo

Attività principali:

1. **Raccolta dati**

   * da Google:

     * SEO:

       * Search Console (impression, click, posizione per keyword);
       * Analytics (sessioni organiche, conversioni per pagina sorgente).

     * Ads:

       * impression, click, CTR;
       * CPC medio;
       * conversioni registrate.

   * da Odoo:

     * n. lead con fonte Google (organico, Ads, ricerca manuale);
     * conversione lead→opportunità;
     * conversione opportunità→cliente;
     * valore opportunità generato.

2. **Analisi e insight**

   * per SEO:

     * quali pagine portano più lead;
     * quali keyword sembrano più promettenti;

   * per Ads:

     * campagne/gruppi/keyword con miglior rapporto costo/lead;
     * ricerche effettive da includere/escludere;

   * per ricerca manuale:

     * qualità dei prospect trovati;
     * tasso di risposta dopo primo contatto.

3. **Report periodici**

   * predisporre report (mensili/trimestrali) secondo modello standard:

     * panoramica traffico e lead da Google;
     * performance SEO;
     * performance Ads;
     * risultati della ricerca manuale lead;
     * proposte di ottimizzazione.

   * struttura del report e dettagli KPI sono definiti in allegati (es. “Scheda KPI Google”, “Modello report Google”).

4. **Miglioramento continuo**

   * aggiornare:

     * piano keyword;
     * struttura e contenuti landing;
     * configurazione campagne Ads;
     * lista query per ricerca manuale lead;

   * riallocare budget e tempo verso attività più efficaci;

   * proporre eventuali modifiche a SOP, WI o allegati se emergono nuovi bisogni.

---

## 6. Strumenti e sistemi utilizzati

* **Google Search Console** – Monitoraggio visibilità organica, query, copertura, problemi tecnici.

* **Google Analytics / Matomo / altro sistema analytics** – Analisi traffico, sorgenti, conversioni.

* **Google Tag Manager** – Gestione centralizzata dei tag di tracciamento (se adottato).

* **Google Ads** – Gestione campagne a pagamento (ricerca, eventuale display/YouTube).

* **Sito web / CMS** – Pagine servizi, blog, landing; integrazione form.

* **Odoo CRM** – Gestione lead/opportunità, tracciamento fonti, report di conversione (SOP-CRM-01).

* **Google Sheets / strumento BI** – Piani keyword e campagne, cruscotti KPI (se non integrati altrove).

* **Google stesso come motore di ricerca** – Strumento di ricerca manuale lead.

* **Google Drive / repository documentali** – Archiviazione di piani, export, report, WI (SOP-DOC-01).

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali

* **R1 – Spreco di budget Ads**
  Targeting errato, keyword non pertinenti, landing poco efficaci → costi senza lead di qualità.

* **R2 – Lead non tracciati o tracciati male**
  Form non collegati a Odoo, fonti non valorizzate, eventi di conversione mancanti.

* **R3 – Duplicazione lead in Odoo**
  Lead creati più volte per la stessa azienda/persona (soprattutto nella ricerca manuale), con confusione su responsabilità e storico.

* **R4 – SEO trascurato o incoerente**
  Pagine non aggiornate, assenza di strategia → perdita di opportunità organiche.

* **R5 – Non conformità normativa (cookie/privacy)**
  Tracciamento non conforme, mancanza di informative o consensi corretti.

* **R6 – Messaggi non allineati con l’offerta reale**
  Annunci o pagine che promettono ciò che servizi/processi non possono garantire → clienti insoddisfatti.

### 7.2 Controlli e misure di mitigazione

* **C1 – Revisione periodica delle campagne Ads**
  Verifica regolare di keyword, annunci, search terms, conversioni, costo/lead.

* **C2 – Audit periodico di tracking**
  Controllo che form, eventi, conversioni e fonti siano configurati e funzionanti.

* **C3 – Procedure antduplicato in Odoo**
  Obbligo di ricerca in Odoo prima di creare nuovi lead (soprattutto per ricerca manuale Google), supportato da WI.

* **C4 – Allineamento SEO–Sito–Offerta**
  Coordinamento stretto tra Marketing, Dev e Delivery per garantire che pagine e testi riflettano servizi reali.

* **C5 – Verifica compliance privacy/cookie**
  Coinvolgimento di chi gestisce compliance per:

  * banner cookie;
  * informative privacy;
  * gestione consensi.

* **C6 – Review KPI e ri‑pianificazione**
  Review periodica KPI (SEO/Ads/ricerca lead) e adeguamento Piano Google e Piano marketing.

### 7.3 KPI / Indicatori (senza valori numerici)

Esempi di KPI collegati a questo SOP:

* n. **lead da Google – organico** / periodo;
* n. **lead da Google Ads** / periodo;
* n. **lead da ricerca manuale Google** / periodo;
* tasso di conversione **visite → lead** per pagine/landing chiave;
* tasso di conversione **lead Google → opportunità** in Odoo;
* tasso di conversione **opportunità Google → cliente**;
* **CPL (Cost per Lead)** per campagne Ads;
* trend di **impression/click/posizione** per cluster di keyword strategiche;
* % di lead Google con fonte/ campagna correttamente valorizzate.

> **Nota:** formule, fonti dati, frequenza di rilevazione ed eventuali soglie target sono definiti in **Schede KPI e modelli di report allegati**, non in questo SOP.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* Il presente SOP è archiviato nel repository documentale secondo SOP-DOC-01 (es. cartella `/SOP/SOP-MKT/`).
* La versione ufficiale approvata è resa disponibile tramite:

  * **Odoo Knowledge Base** (SOP-KB-01);
  * eventualmente **GitHub Pages** se utilizzato come repository dei SOP.
* Il personale deve consultare la **versione “Emesso”** più aggiornata.

### 8.2 Revisione e aggiornamento

La revisione è attivata in caso di:

* cambiamenti significativi nella strategia o negli strumenti (nuovo sistema analytics, cambio struttura sito, maggior peso all’Ads, ecc.);
* modifiche sostanziali delle policy Google o della normativa (privacy/cookie);
* difficoltà operative, non conformità o esiti di audit;
* almeno entro la data di revisione prevista.

Ogni nuova versione:

* aggiorna numero di versione e data;
* viene registrata nella sezione **10 – Storico revisioni**;
* può richiedere aggiornamenti coordinati di WI, allegati, SOP correlati (MKT‑01/02/05, CRM‑01).

### 8.3 Obbligatorietà e formazione

* Tutte le figure che:

  * gestiscono SEO/Ads;
  * sfruttano Google per ricerca manuale lead;
  * lavorano lead provenienti da Google;

  devono conoscere e applicare il presente SOP nella parte di competenza.

* In occasione della prima emissione o di revisioni rilevanti:

  * il Responsabile Marketing organizza brevi sessioni di formazione/comunicazione;
  * può essere richiesta la **presa visione formale** tramite KB Odoo o strumenti interni.

---

## 9. Allegati

Per tipologia e gestione degli allegati fare riferimento al documento **“Catalogo allegati standard per i SOP aziendali” (`SOP-ALLEGATI-STANDARD.md`)**.

Alcuni allegati tipici per SOP-MKT-06:

* **Allegato 1 – Diagramma di flusso Google → Odoo**
  Schema del flusso da:

  * ricerca organica / Ads / ricerca manuale → visita → form / contatto → lead in Odoo → opportunità.

* **Allegato 2 – Matrice RACI Google**
  Dettaglio dei ruoli (Marketing, Sales, Dev, Direzione) per attività SEO, Ads, ricerca lead e reporting.

* **Allegato 3 – Piano Google SEO/Ads & ricerca lead**
  Documento operativo che definisce:

  * cluster keyword;
  * pagine/landing;
  * campagne attive;
  * vertical e query per ricerca manuale lead.

* **Allegato 4 – Work Instructions / How‑to operativi**
  Esempi:

  * WI-MKT-06-01 – Setup tracking Google (Analytics, Tag Manager, conversioni);
  * WI-MKT-06-02 – Creazione e gestione campagne Google Ads;
  * WI-MKT-06-03 – Ricerca lead su Google e creazione lead in Odoo senza duplicati;
  * WI-MKT-06-04 – SEO audit di base del sito.

* **Allegato 5 – Script e template**

  * Esempi di email / messaggi per contattare lead trovati tramite ricerca manuale Google;
  * template per risposta a richieste in arrivo da landing/Ads.

* **Allegato 6 – Scheda KPI Google**
  Elenco KPI con definizione, formula, fonte dati, frequenza e responsabilità.

* **Allegato 7 – Modello report Google**
  Template di report periodico (mensile/trimestrale) per canale Google (SEO+Ads+ricerca lead).

La posizione di archiviazione (Drive, KB Odoo, GitHub Pages) deve essere specificata nella versione definitiva del SOP.

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica                | Redatto da                          | Verificato da                             | Approvato da        |
| -------- | ------------ | ----------------------------------- | ----------------------------------- | ----------------------------------------- | ------------------- |
| 0.1      | *[da comp.]* | Prima emissione in bozza SOP-MKT-06 | *[Responsabile Marketing / Growth]* | *[Responsabile Commerciale / Sales Lead]* | *[Direzione / CEO]* |
