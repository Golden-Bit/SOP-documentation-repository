# SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna

---

### 0. Metadati del documento

* **Codice SOP:** SOP-KB-01
* **Titolo:** Knowledge Base Odoo e collegamento alla documentazione esterna
* **Versione:** 1.0
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Responsabile Qualità / Documentazione]*
* **Verificato da (se applicabile):** *[Ruolo/Funzionale]*
* **Approvato da:** *[Direzione]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna (eventualmente con sezioni/viste condivisibili verso clienti/partner, se previsto da policy specifiche)

---

## 1. Scopo e campo di applicazione

### Scopo

Il presente SOP definisce il **modello di riferimento** per l’utilizzo della **Knowledge Base (KB) di Odoo** come:

* **punto di accesso centrale** alla conoscenza aziendale strutturata;
* **hub di collegamento** tra:

  * SOP e documentazione ufficiale su **GitHub / GitHub Pages**;
  * documentazione operativa e materiali su **Google Drive**;
  * documentazione tecnica integrata al codice su **GitLab / GitHub**;
  * eventuali altre fonti esterne (siti, manuali vendor, documentazione clienti ecc.).

In particolare, il SOP:

* definisce **quando** e **perché** un contenuto deve essere rappresentato da un articolo della KB;
* spiega **come** gli articoli KB devono referenziare in modo coerente:

  * SOP e manuali ufficiali (fonte di verità: GitHub Pages, secondo SOP-DOC-02);
  * documenti operativi su Drive (secondo SOP-DOC-01 e SOP-DOC-03/…);
  * documentazione tecnica su GitLab/GitHub (secondo SOP-DEV-01/02);
* descrive il ruolo della KB come **interfaccia informativa** integrata nei moduli Odoo (CRM, Progetti, Contabilità, Documenti, ecc.);
* individua i **processi editoriali** e di **governo della KB** che richiedono SOP specifici dedicati (SOP-KB-02, SOP-KB-03, SOP-KB-04, SOP-KB-05).

Il presente SOP è quindi un **documento di cornice**: non entra nel dettaglio di ogni passaggio operativo di redazione, revisione e pubblicazione degli articoli (che saranno disciplinati nei SOP-KB-* dedicati), ma:

* stabilisce i principi generali;
* definisce i ruoli;
* descrive il flusso globale di utilizzo della KB come sistema di knowledge management integrato.

### Campo di applicazione

Il SOP si applica a:

* **tutte le aree aziendali** che producono o utilizzano contenuti di conoscenza strutturata:

  * Organizzazione & Governance;
  * Commerciale & CRM;
  * Marketing & Comunicazione;
  * Progetti & Delivery;
  * Sviluppo Software;
  * Amministrazione & Contabilità;
  * Documentazione & Knowledge Management;
  * Sicurezza & Compliance;
* tutto il personale che:

  * consulta la KB per eseguire le attività lavorative;
  * propone, redige, revisiona o approva articoli KB;
  * gestisce documentazione su GitHub Pages, Google Drive, GitLab/GitHub che deve essere collegata alla KB.

La KB è principalmente **ad uso interno**; eventuali porzioni di contenuto rese disponibili a **clienti/partner** (es. articoli di help, FAQ, manuali) devono rispettare le policy e i SOP specifici di sicurezza, privacy e gestione accessi.

### Esclusioni / limiti

Non rientrano nel campo del presente SOP:

* le modalità operative di **redazione di SOP e manuali** (gestite da:

  * SOP-DOC-12 – *Redazione, gestione e aggiornamento dei SOP aziendali*;
  * SOP-DOC-13 – *Gestione del materiale formativo e delle linee guida interne su GitHub Pages*;
  * SOP-DOC-14 – *Documentazione tecnica di librerie, servizi e API*;
  * SOP-DOC-15 – *Gestione di policy e regolamenti interni*);
* la gestione di dettaglio del **modello documentale integrato** tra Odoo, Google Drive e GitHub (disciplinato da **SOP-DOC-01** e SOP-DOC-03/… per le strutture Drive);
* la gestione puntuale dei **repository di codice** e della documentazione integrata al codice in GitLab/GitHub (SOP-DEV-01, SOP-DEV-02);
* gli aspetti tecnici di **configurazione applicativa** della KB Odoo (permessi di sistema, installazione moduli), trattabili in istruzioni tecniche interne o SOP IT dedicati.

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabile)

* **ISO 9001:2015** – Requisiti relativi alla gestione delle informazioni documentate e alla conoscenza organizzativa.
* **Regolamento (UE) 2016/679 – GDPR** – Per la gestione di eventuali dati personali contenuti in articoli, allegati o documentazione collegata.
* Eventuali altre norme di settore che richiedano la tracciabilità e la disponibilità di procedure, manuali o evidenze documentali.

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
  (descrive il modello complessivo e i collegamenti tra Odoo, Drive, GitLab, GitHub, GitHub Pages)

* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
  (ruolo di Odoo come hub e di Drive/GitHub come repository documentali)

* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
  (fonte di verità per SOP, manuali, policy, documentazione ufficiale)

* **SOP-DOC-03/… – SOP di struttura e gestione cartelle su Google Drive**
  (Struttura generale multi-organizzazione, Anagrafiche, Progetti, Formazione, Contabilità, ecc.)

* **SOP-DOC-12 – Redazione, gestione e aggiornamento dei SOP aziendali**

* **SOP-DOC-13 – Gestione del materiale formativo e delle linee guida interne su GitHub Pages**

* **SOP-DOC-14 – Documentazione tecnica di librerie, servizi e API**

* **SOP-DOC-15 – Gestione di policy e regolamenti interni**

* **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo**

* **SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo**

* **SOP-ACC-01 – Gestione contabile e tesoreria su Odoo**

* **SOP-MKT-01 / SOP-MKT-02 – Marketing & Comunicazione**

* **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**

* **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**

SOP specifici di futura definizione per la macro area KB (da considerare come **rimandi previsti** dal presente documento):

* **SOP-KB-02 – Tassonomia, categorie e linee guida di redazione degli articoli KB**
  (definisce struttura, categorie, tag, metadata, stile e template degli articoli)
* **SOP-KB-03 – Workflow di redazione, revisione, approvazione e pubblicazione articoli KB**
  (definisce step, stati, ruoli e controlli di qualità degli articoli)
* **SOP-KB-04 – Gestione feedback, manutenzione periodica e miglioramento continuo della KB**
  (gestione commenti/feedback, revisione periodica, deprecazione articoli)
* **SOP-KB-05 – Gestione dei permessi, visibilità e accesso alla KB (interno/esterno)**
  (regole per visibilità per ruolo, eventuale esposizione verso clienti/partner)

---

## 3. Definizioni, acronimi e abbreviazioni

* **SOP (Standard Operating Procedure)** – Procedura Operativa Standard.
* **Odoo** – Gestionale ERP aziendale, hub per anagrafiche, progetti, contabilità, documenti, KB.
* **Knowledge Base (KB) Odoo** – Modulo/area di Odoo che contiene articoli strutturati (testo, immagini, link) utilizzati come base di conoscenza interna e, se previsto, esterna.
* **Articolo KB** – Unità informativa autonoma all’interno della KB (how-to, guida, FAQ, policy, SOP, manuale sintetico, ecc.).
* **Link esterno** – Collegamento ipertestuale da un articolo KB verso una risorsa esterna:

  * pagina GitHub Pages (SOP, manuali, policy);
  * file o cartella su Google Drive;
  * repository o pagina di documentazione GitLab/GitHub;
  * sito o risorsa web esterna.
* **Fonte di verità** – Posizione/sistema che contiene la **versione ufficiale** di un documento:

  * per SOP, manuali, policy, doc ufficiale → GitHub / GitHub Pages (SOP-DOC-02);
  * per documenti operativi → Google Drive, secondo SOP-DOC-01 e SOP-DOC-03/…;
  * per documentazione integrata al codice → GitLab/GitHub (SOP-DEV-01/02).
* **Tag / Etichetta** – Metadato che descrive un articolo KB (es. area, processo, prodotto, ruolo destinatario).
* **Tassonomia KB** – Struttura logica di categorie/sottocategorie e criteri di classificazione degli articoli; sarà normata in dettaglio in **SOP-KB-02**.
* **Owner di contenuto** – Ruolo o persona responsabile del contenuto di uno o più articoli KB (per area/processo).
* **Visibilità KB** – Ambito di accesso a un articolo (solo interno, solo specifici ruoli, clienti/partner, ecc.), gestito in dettaglio in **SOP-KB-05**.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

La KB Odoo è un **asset trasversale** a tutte le aree aziendali e rappresenta:

* il **catalogo indicizzato** dei riferimenti documentali ufficiali (SOP, manuali, policy, doc tecniche, materiale formativo);
* la **porta di ingresso** verso la documentazione esterna:

  * GitHub Pages per SOP e doc ufficiale;
  * Google Drive per documenti operativi;
  * GitLab/GitHub per doc tecnica integrata al codice.

È utilizzata:

* dalla Direzione per veicolare policy e documentazione strategica;
* da Commerciale & Marketing per allineare offerta, materiali standard e processi CRM;
* da Progetti & Delivery per procedure operative, template, best practice;
* da Sviluppo Software per guideline tecniche, architetturali e processuali;
* da Amministrazione & Contabilità per manuali d’uso Odoo e procedure amministrativo-contabili;
* da Documentazione & Knowledge Management come strumento di knowledge governance.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

Legenda: **R = Responsible**, **A = Accountable**, **C = Consulted**, **I = Informed**

* **Direzione**

  * A: approvazione del presente SOP e delle principali linee guida sulla gestione della conoscenza.
  * C/I: informata sui KPI della KB e sui piani di miglioramento continuo.
  * C: coinvolta nella definizione di articoli KB strategici (policy, regolamenti, documenti istituzionali).

* **Responsabile Qualità / Documentazione**

  * A: governo complessivo del sistema KB e dei SOP-KB-*.
  * R: definizione e aggiornamento delle regole generali di utilizzo della KB (questo SOP).
  * R: coordinamento della coerenza tra articoli KB, SOP su GitHub Pages e documentazione su Drive.
  * C: consultato per la creazione di nuove categorie, sezioni, tipologie di articoli.

* **Responsabile IT / CTO**

  * A: configurazione tecnica del modulo KB in Odoo, permessi e integrazioni.
  * R: gestione tecnica dei collegamenti tra Odoo e sistemi esterni (GitHub Pages, Drive, GitLab).
  * C: consultato per requisiti tecnici legati alla visibilità (interno/esterno) e alle performance.

* **Knowledge Manager / KB Owner** (se distinto dal Responsabile Qualità/Doc)

  * A: gestione operativa della KB (monitoraggio, qualità, completezza).
  * R: supervisione della tassonomia, dei template e dello stile editoriale (SOP-KB-02).
  * R: gestione del workflow di revisione e pubblicazione articoli (SOP-KB-03).
  * R: raccolta e gestione dei feedback e dei miglioramenti (SOP-KB-04).

* **Responsabili di Area / Process Owner**

  * A (per i contenuti della propria area): approvazione degli articoli KB che descrivono processi, procedure e strumenti di propria competenza.
  * R: identificazione dei contenuti critici da documentare in KB (SOP, how-to, FAQ).
  * C: collaborazione nella definizione della tassonomia per la propria area (SOP-KB-02).
  * I: aggiornati sugli audit e feedback relativi agli articoli della propria area.

* **Autori / Redattori KB**

  * R: redazione delle bozze degli articoli KB secondo le linee guida editoriali (SOP-KB-02).
  * R: proposta di aggiornamento degli articoli esistenti in base a cambiamenti di processo o feedback utenti.
  * C/I: interazione con Owner di contenuto e Knowledge Manager durante il workflow di revisione (SOP-KB-03).

* **Tutto il personale**

  * R: uso corretto della KB come fonte di informazione principale per SOP, procedure, manuali e linee guida.
  * R: segnalazione di errori, contenuti obsoleti o mancanti tramite i canali previsti (SOP-KB-04).
  * I: consapevolezza che la KB è il **punto di accesso** alla documentazione ufficiale (GitHub Pages) e operativa (Drive).

Una matrice RACI di dettaglio per i singoli processi (redazione, revisione, pubblicazione, manutenzione, gestione permessi) sarà riportata negli allegati o nei SOP-KB specifici.

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il processo di gestione della **Knowledge Base Odoo** comprende, ad alto livello:

* l’**identificazione dei contenuti** che devono essere presenti in KB (SOP, manuali, how-to, FAQ, materiale formativo, doc tecniche di riferimento);
* la **redazione e strutturazione** degli articoli KB, con collegamento alle fonti di verità:

  * GitHub Pages per SOP, manuali, policy;
  * Google Drive per documenti operativi e materiali di progetto/formazione;
  * GitLab/GitHub per doc tecnica integrata al codice;
* la **revisione, approvazione e pubblicazione** degli articoli;
* l’**integrazione** della KB con i moduli Odoo (CRM, Progetti, Contabilità, ecc.) tramite link o riferimenti contestuali;
* la **manutenzione periodica** degli articoli (aggiornamento, consolidamento, obsolescenza) e il miglioramento continuo basato su feedback e KPI.

Gli aspetti editoriali e di workflow più complessi sono delegati ai SOP-KB-* specifici, mentre il presente documento delinea il quadro generale e le interazioni con Drive, GitHub, Odoo e gli altri sistemi.

### 5.2 Flusso operativo di alto livello

1. **Identificazione del contenuto da rappresentare in KB**

   * Trigger:

     * emissione o aggiornamento di un SOP (SOP-DOC-12, SOP-DOC-13/14/15) su GitHub Pages;
     * creazione o aggiornamento di materiale formativo/documentazione su GitHub Pages o Drive;
     * esigenza operativa ricorrente (FAQ, istruzioni, best practice di progetto);
     * segnalazioni da audit, incident, feedback personale.
   * L’Owner di processo o il Responsabile Qualità / Knowledge Manager valuta se sia necessario:

     * un **nuovo articolo KB**;
     * o l’**aggiornamento** di un articolo esistente.

2. **Redazione della bozza di articolo KB**

   * L’Autore / Redattore:

     * crea una bozza in KB Odoo utilizzando struttura, tassonomia e template definiti (SOP-KB-02);
     * inserisce una **descrizione sintetica** del contenuto;
     * collega l’articolo alle **fonti di verità**:

       * URL GitHub Pages per SOP e manuali;
       * link a file/cartelle Drive per materiali operativi;
       * link a doc tecniche GitLab/GitHub per architetture, API, ecc.;
     * aggiunge tag/categorie appropriate.

3. **Revisione e approvazione**

   * L’Owner di contenuto e, se previsto, il Responsabile Qualità / Knowledge Manager:

     * verificano correttezza, completezza, coerenza con SOP di riferimento;
     * controllano che i link puntino alle **fonti di verità** corrette;
     * valutano la compatibilità con eventuali policy di sicurezza e privacy.
   * Gli step, gli stati (Bozza, In revisione, Pubblicato, Obsoleto) e i ruoli sono definiti in dettaglio in **SOP-KB-03**.

4. **Pubblicazione e collegamento ad altri moduli Odoo**

   * L’articolo approvato viene messo nello stato **Pubblicato**:

     * è categorizzato in modo coerente per area/processo/prodotto;
     * è referenziato, ove opportuno, in:

       * record CRM (lead, opportunità) come guida operativa;
       * progetti/task in Odoo Progetti;
       * documenti contabili o amministrativi (come riferimento a procedure o manuali);
       * altri moduli (Helpdesk, ecc.).
   * Eventuali collegamenti da GitLab/GitHub verso la KB (e viceversa) sono gestiti secondo SOP-DEV-01/02.

5. **Utilizzo operativo della KB**

   * Il personale:

     * consulta la KB come **primo punto** per cercare SOP, manuali e how-to;
     * utilizza i link agli originali su GitHub Pages o Drive quando necessita del dettaglio completo;
     * evita di conservare copie locali non controllate, facendo riferimento sempre a KB + fonte di verità.

6. **Monitoraggio, manutenzione e miglioramento continuo**

   * Il Knowledge Manager / Responsabile Qualità:

     * monitora:

       * articoli non aggiornati da lungo tempo;
       * accessi, ricerche frequenti, articoli poco utilizzati;
     * coordina:

       * aggiornamento di contenuti obsoleti;
       * accorpamento o divisione di articoli sovrapposti;
       * eliminazione/archiviazione di articoli non più pertinenti.
   * Le modalità di raccolta e gestione dei feedback, i cicli di revisione programmata, e l’uso dei KPI sono disciplinati in dettaglio da **SOP-KB-04**.

7. **Gestione della visibilità e degli accessi**

   * In funzione delle policy aziendali, alcuni articoli possono essere:

     * visibili a tutta l’azienda;
     * visibili solo a specifici ruoli/gruppi (es. amministrazione, HR, sicurezza);
     * esposti, in parte o in copia/adattamento, verso clienti/partner.
   * Le regole su visibilità, permessi, eventuale duplicazione/adattamento di contenuti per uso esterno sono disciplinate in **SOP-KB-05** e nelle policy di sicurezza/privacy.

### 5.3 Istruzioni operative / Dettaglio per fasi (vista globale)

#### 5.3.1 Collegamento con GitHub / GitHub Pages

Principi generali:

* Per **ogni SOP** presente nel repository documentazione su GitHub e pubblicato su GitHub Pages (SOP-DOC-02, SOP-DOC-12/13/14/15):

  * deve esistere **almeno un articolo KB** che:

    * riporti **codice, titolo, versione** e una breve descrizione del SOP;
    * contenga il **link diretto** alla pagina GitHub Pages del SOP (fonte di verità);
    * indichi l’area di appartenenza (SOP-ORG, SOP-CRM, SOP-DOC, ecc.);
    * specifichi lo **stato** (Bozza/Emesso/Obsoleto) in coerenza con quanto indicato nel SOP stesso.
* Per i **manuali e le linee guida ufficiali** pubblicate su GitHub Pages:

  * la KB può ospitare:

    * articoli di tipo “guida rapida” o “FAQ” con link al manuale completo;
    * articoli di onboarding che aggregano più SOP/manuali secondo il profilo (es. “Onboarding Project Manager”).

Il dettaglio su naming degli articoli KB, struttura dei paragrafi e convenzioni di link sarà stabilito in **SOP-KB-02**.

#### 5.3.2 Collegamento con Google Drive

* I documenti la cui **fonte di verità** è Google Drive (soprattutto documenti operativi di progetto, report, template operativi, materiali formativi non istituzionali) possono essere:

  * referenziati in articoli KB che:

    * spiegano **in che contesto** usare quel documento;
    * contengono il **link alla cartella** o al file di fonte (Drive);
    * chiariscono, se necessario, la relazione con eventuali SOP o manuali su GitHub.

* Esempi:

  * Articolo KB “Gestione documenti di progetto su Drive” → link alle cartelle `PROGETTI` definite nei SOP-DOC-03/05, con rimando alle regole di struttura e naming.
  * Articolo KB “Template di presentazione offerta standard” → link al file template su Drive, con indicazione che eventuale descrizione formale del processo di offerta è in un SOP su GitHub Pages.

La scelta di quali cartelle e file Drive referenziare nella KB deve essere coerente con **SOP-DOC-01** e con i SOP DOC-* di dettaglio sulle strutture Drive.

#### 5.3.3 Collegamento con GitLab / GitHub (documentazione tecnica)

* La KB Odoo deve fungere da **ponte** tra:

  * processi/procedure ad uso funzionale (SOP, manuali, guide);
  * documentazione tecnica integrata al codice (README, doc API, wiki di progetto).

* Esempio di pattern:

  * Articolo KB “Architettura del servizio XYZ”

    * breve overview funzionale comprensibile anche a ruoli non tecnici;
    * link alla documentazione architetturale su GitHub Pages (SOP-DOC-14);
    * link al repository GitLab/GitHub per dettagli tecnici, issue, CI/CD.

* I criteri per decidere cosa tenere nella KB e cosa lasciare nel solo contesto GitLab/GitHub sono descritti in **SOP-DOC-14** e **SOP-DEV-01/02**; la KB deve comunque contenere almeno un **punto di ingresso** per ogni componente o servizio rilevante.

#### 5.3.4 Collegamento con i moduli Odoo (CRM, Progetti, Contabilità, ecc.)

La KB è integrata nei flussi operativi Odoo tramite:

* **link contestuali**:

  * da record CRM (lead/opportunità) verso articoli KB su:

    * come gestire la pipeline;
    * quali template di offerta usare;
    * quali listini e allegati ufficiali sono disponibili (con link a GitHub Pages e Drive);
  * da progetti e task verso articoli KB su:

    * modalità di lavoro Scrum multi-progetto;
    * checklist di analisi, sviluppo, test;
    * documentazione di prodotto/servizio.
  * da registrazioni contabili verso articoli KB su:

    * procedure di fatturazione, riconciliazione, gestione scadenziari.

* **ricerca centralizzata**:

  * gli utenti possono cercare nella KB direttamente da Odoo per trovare:

    * SOP;
    * how-to su moduli Odoo;
    * link a documentazione esterna.

I dettagli su come configurare i link, utilizzare widget Odoo specifici e standardizzare i collegamenti saranno descritti in **SOP-KB-03** e, se necessario, in istruzioni operative tecniche.

---

## 6. Strumenti e sistemi utilizzati

* **Odoo – Modulo Knowledge Base**

  * Contiene gli articoli KB.
  * Gestisce:

    * contenuti testuali, immagini, snippet;
    * link verso GitHub Pages, Drive, GitLab/GitHub;
    * categorie, tag, permessi e, se configurato, eventuale versione.
  * È il **front-end** principale con cui il personale entra in contatto con la documentazione aziendale.

* **Odoo – Altri moduli (CRM, Progetti, Contabilità, Documenti, Helpdesk, ecc.)**

  * Consumano la KB tramite:

    * link diretti ad articoli KB;
    * funzioni di ricerca dalla UI;
    * eventuali snippet o widget integrati.
  * Forniscono il **contesto operativo** in cui la KB viene utilizzata.

* **GitHub / GitHub Pages**

  * Repository e hosting della **documentazione ufficiale** (SOP, manuali, policy, doc tecniche di alto livello), secondo SOP-DOC-02 e SOP-DOC-12/13/14/15.
  * Rappresenta la **fonte di verità** per tali documenti.
  * Gli articoli KB contengono link a GitHub Pages per la consultazione della versione ufficiale.

* **Google Drive**

  * Utilizzato per documenti operativi, di progetto, materiali formativi non istituzionali, report, ecc., secondo SOP-DOC-01 e SOP-DOC-03/… .
  * La KB referenzia tali documenti come **materiale di supporto**, specificando:

    * contesto d’uso;
    * relazione con SOP/manuali su GitHub.

* **GitLab / GitHub (repository di codice)**

  * Gestiscono il codice sorgente e parte della documentazione tecnica integrata.
  * La KB contiene link a tali repository, in particolare per:

    * doc tecniche di componenti critici;
    * guide per sviluppatori e integratori;
    * reference API.

* Eventuali altri strumenti (es. sistemi di ticketing esterni, portali clienti, piattaforme e-learning) potranno essere collegati alla KB secondo SOP specifici o istruzioni tecniche.

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali

* **Rischio di incoerenza tra KB e fonti di verità**

  * Articoli KB che puntano a documenti obsoleti su GitHub Pages o Drive.
  * Descrizioni in KB non allineate con l’ultima versione dei SOP o dei manuali.

* **Rischio di duplicazione e frammentazione della conoscenza**

  * Informazioni ripetute in più articoli KB senza coordinamento.
  * Coesistenza di documenti non referenziati in KB e articoli KB non collegati a fonti ufficiali.

* **Rischio di scarsa reperibilità**

  * Tassonomia e tag non coerenti → difficoltà a trovare contenuti pertinenti.
  * Articoli troppo lunghi o mal strutturati.

* **Rischio di utilizzo di documenti non ufficiali**

  * Personale che si basa su copie locali, link non controllati o vecchie versioni in Drive anziché passare da KB + fonte di verità.

* **Rischio di esposizione non controllata verso l’esterno**

  * Articoli contenenti informazioni riservate resi accessibili a clienti/partner senza adeguati controlli (trattato in SOP-KB-05 e policy di sicurezza).

### 7.2 Controlli e misure di mitigazione

* **Controlli periodici sulla coerenza dei link**

  * Verifica campionaria (es. trimestrale) che gli articoli KB puntino a:

    * pagine GitHub Pages corrette e aggiornate;
    * cartelle/file Drive previsti dai SOP-DOC-*;
    * repository GitLab/GitHub corretti.

* **Revisione programmata degli articoli KB**

  * Ciascun articolo KB deve avere un **Owner** e una **frequenza di revisione** indicativa (es. annuale, semestrale).
  * Il Knowledge Manager monitora articoli “scaduti” e attiva revisioni (SOP-KB-04).

* **Standardizzazione della tassonomia e dello stile**

  * Applicazione delle regole di **SOP-KB-02** per categorie, tag, naming, struttura degli articoli.
  * Uso di template standard per ridurre variabilità e migliorare la leggibilità.

* **Formazione e comunicazione interna**

  * Sessioni periodiche su:

    * come usare la KB;
    * come proporre modifiche;
    * differenze tra KB, GitHub Pages e Drive.

* **Controllo permessi e visibilità**

  * Configurazione dei permessi KB (SOP-KB-05) in coordinamento con il Responsabile IT/CTO e le policy di sicurezza:

    * articoli sensibili visibili solo a gruppi specifici;
    * chiara separazione tra contenuti interni e contenuti eventualmente esposti verso l’esterno.

### 7.3 KPI / Indicatori (se applicabili)

Esempi di KPI per monitorare l’efficacia del processo:

* **Copertura dei processi in KB**

  * % di processi core che hanno almeno un articolo KB dedicato.
* **Copertura dei SOP in KB**

  * % di SOP attivi su GitHub Pages che hanno un articolo KB associato.
* **Aggiornatezza KB**

  * % di articoli KB revisionati negli ultimi 12 mesi.
* **Utilizzo KB**

  * numero medio di visualizzazioni articoli / utente / mese;
  * ricerche più frequenti e tasso di ricerche “senza risultati” (proxy di contenuti mancanti).
* **Qualità percepita**

  * risultati di survey interne sul livello di soddisfazione rispetto a chiarezza, reperibilità e utilità degli articoli KB.
* **Non conformità documentali**

  * numero di NC rilevate in audit (es. uso di doc non aggiornati) attribuibili a carenze nella KB.

La definizione puntuale dei KPI, delle soglie target e delle modalità di raccolta dati sarà dettagliata in **SOP-KB-04** o in appositi allegati.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* La **fonte di verità** del presente SOP è il file sorgente nel **repository GitHub** dedicato alla documentazione (formato controllato, es. Markdown).
* La versione ufficiale approvata è pubblicata su **GitHub Pages** secondo quanto previsto da **SOP-DOC-02**.
* Un articolo nella **Knowledge Base Odoo** (categoria “SOP – Knowledge Management / KB Odoo”) contiene:

  * codice, titolo, versione e breve descrizione;
  * link alla pagina GitHub Pages di questo SOP;
  * eventuali link a SOP-KB-* correlati.
* Eventuali bozze o materiali di lavoro possono essere archiviati su Google Drive in una cartella dedicata alla documentazione/SOP (fonte di lavoro, non ufficiale).

### 8.2 Revisione e aggiornamento

La revisione del presente SOP è attivata in caso di:

* modifiche significative alle funzionalità o al ruolo della KB Odoo;
* introduzione di nuovi SOP-KB-* o modifica sostanziale di quelli esistenti (SOP-KB-02/03/04/05);
* cambiamenti architetturali nel sistema informativo (SOP-ORG-01, SOP-DOC-01, SOP-DEV-01/02);
* non conformità rilevate in audit;
* nuove esigenze di compliance, certificazioni o richieste della Direzione.

Ogni revisione comporta:

* aggiornamento del numero di versione e della data di emissione;
* aggiornamento dei riferimenti interni e dei rimandi ai SOP-KB-* specifici;
* registrazione delle modifiche nella sezione 10 – Storico revisioni;
* comunicazione interna (es. notifica in KB Odoo, comunicazioni via canali aziendali).

### 8.3 Obbligatorietà e formazione

* Tutto il personale è tenuto a:

  * utilizzare la KB Odoo come canale privilegiato di accesso alla documentazione;
  * non creare canali paralleli non controllati (doc locali, link “privati” non indicizzati).
* I **Responsabili di area** e gli **Owner di processo**:

  * devono conoscere il presente SOP e i SOP-KB-*;
  * sono responsabili di garantire che i processi di loro competenza siano adeguatamente documentati in KB.
* In occasione della prima emissione o di revisioni significative:

  * possono essere organizzate sessioni di formazione (live, video, guide illustrate);
  * può essere richiesta la **presa visione** formale del documento tramite la KB Odoo o altri strumenti aziendali.

---

## 9. Allegati (opzionale)

Esempi di allegati potenzialmente collegati a questo SOP:

* **Allegato 1 – Schema logico della tassonomia KB (categorie e sottocategorie)**
  (in coerenza con SOP-KB-02)
* **Allegato 2 – Template standard di articolo KB**
  (campi obbligatori, sezioni consigliate, elementi di stile)
* **Allegato 3 – Matrice RACI dettagliata per gestione KB**
  (per processi: redazione, revisione, pubblicazione, manutenzione, gestione permessi)
* **Allegato 4 – Esempi di articoli KB “tipo”**
  (es. articolo SOP, articolo how-to, articolo prodotto, FAQ)
* **Allegato 5 – Schema di integrazione tra KB, GitHub Pages, Drive, GitLab**

Gli allegati ufficiali sono archiviati come fonte di verità nel repository GitHub della documentazione e, se opportuno, pubblicati su GitHub Pages. Versioni modificabili di lavoro possono essere conservate in apposite cartelle su Drive.

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica          | Redatto da                   | Verificato da  | Approvato da  |
| -------- | ------------ | ----------------------------- | ---------------------------- | -------------- | ------------- |
| 1.0      | *[da comp.]* | Prima emissione del SOP-KB-01 | *[Responsabile Qualità/Doc]* | *[Ruolo/Nome]* | *[Direzione]* |