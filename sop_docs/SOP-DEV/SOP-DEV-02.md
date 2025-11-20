# SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub

---

### 0. Metadati del documento

* **Codice SOP:** SOP-DEV-02
* **Titolo:** Gestione repository pubblici e rilascio pacchetti su GitHub
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

Il presente SOP definisce le regole per la **gestione dei repository pubblici** e il **rilascio di pacchetti e progetti open-source o pubblici** su GitHub, con particolare riferimento a:

* criteri per decidere **cosa può essere pubblicato** su GitHub e in che forma (open-source, codice esempio, demo, template);
* relazione tra **GitLab (sviluppo interno)** e **GitHub (pubblicazione esterna)**;
* struttura, naming e contenuti minimi dei **repository GitHub** aziendali;
* gestione di **versioni**, **tag** e **release** (Semantic Versioning);
* scelta e gestione delle **licenze** open-source;
* requisiti minimi per **README**, **CHANGELOG** e documentazione tecnica associata;
* regole per la pubblicazione di **documentazione** e **siti demo** tramite GitHub Pages (in coordinamento con SOP-DOC-02);
* controlli per evitare la pubblicazione involontaria di **informazioni sensibili** (segreti, dati cliente, IP proprietaria non autorizzata).

### 1.2 Campo di applicazione

Il SOP si applica a:

* tutti i repository **GitHub** che:

  * espongono codice o pacchetti sviluppati dall’azienda;
  * contengono librerie, SDK, template, esempi di codice, demo pubbliche;
  * ospitano documentazione tecnica, siti demo o pagine prodotto (via GitHub Pages);

* tutte le figure che:

  * propongono la pubblicazione di codice/progetti su GitHub (CTO, Tech Lead, Developer, Marketing);
  * gestiscono repository GitHub aziendali (maintainer, owner, DevOps);
  * contribuiscono a progetti open-source a nome aziendale.

Sono esclusi:

* i repository interni e privati gestiti su **GitLab**, regolati da **SOP-DEV-01**;
* la pubblicazione del **sito documentale dei SOP** su GitHub Pages, disciplinata da **SOP-DOC-02** (qui si applicano solo i principi generali).

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabile)

* *Eventuali linee guida interne su sicurezza, proprietà intellettuale e open-source (da definire, se formalizzate).*
* *Eventuale riferimento a policy cliente/contrattuali in tema di IP, se rilevanti per progetti specifici.*

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
  Per il contesto complessivo e la distinzione GitLab (sviluppo interno) / GitHub (pubblicazione esterna).

* **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**
  Per il workflow di sviluppo interno, gestione branch, MR, CI/CD.

* **SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo**
  Per la tracciabilità tra progetti Odoo, backlog e attività di sviluppo collegate a rilasci pubblici.

* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
  Per la gestione di documentazione tecnica non pubblica, collegata a progetti che generano anche componenti pubblici.

* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
  Per la gestione della documentazione istituzionale (SOP, manuali, ecc.) e la struttura del sito documentale.

* **SOP-MKT-01 – Immagine, comunicazione e gestione dei canali marketing**
  Per l’uso di repository pubblici e GitHub Pages come parte dell’immagine aziendale e del posizionamento tecnico.

* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**
  Per la creazione di articoli KB che referenziano repository GitHub (pacchetti, librerie, demo).

---

## 3. Definizioni, acronimi e abbreviazioni

* **GitHub** – Piattaforma di hosting Git per repository pubblici e privati, orientata alla condivisione verso l’esterno.
* **Repository pubblico** – Repository GitHub visibile almeno in lettura a tutti (open-source o sorgente consultabile).
* **Repository privato GitHub** – Repository visibile solo a membri autorizzati, ma comunque su piattaforma esterna (GitHub); usato solo in casi specifici.
* **Pacchetto / Libreria** – Componente riutilizzabile (es. libreria Python/JS, modulo, SDK) rilasciata come versione numerata.
* **Release** – Versione pacchettizzata di un software, identificata da un **tag Git** e metadati (titolo, note di rilascio).
* **Semantic Versioning (SemVer)** – Schema di versionamento `MAJOR.MINOR.PATCH` (es. `1.4.2`).
* **LICENSE** – File che definisce la licenza open-source o i termini d’uso del codice.
* **README** – File principale di descrizione del repository (obiettivi, installazione, uso).
* **CHANGELOG** – File che riepiloga le modifiche tra versioni/release.
* **GitHub Pages** – Servizio di hosting statico per documentazione, demo e siti collegati ai repository.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

Il presente SOP riguarda in particolare:

* **Area Sviluppo Software** – responsabile della qualità tecnica del codice pubblicato;
* **CTO / Responsabile Sviluppo** – garante delle scelte di licenza, del modello di pubblicazione e del rispetto di IP e sicurezza;
* **Marketing & Comunicazione** – coinvolta per l’allineamento tra repository pubblici, branding e strategia di posizionamento;
* **Progetti & Delivery** – coinvolta nei casi in cui il codice pubblicato derivi da progetti cliente e richieda verifiche contrattuali.

GitLab rimane il **sistema principale** per lo sviluppo interno; GitHub viene utilizzato come:

* vetrina tecnico/commerciale (pacchetti open-source, esempi, demo);
* canale di distribuzione per componenti pubbliche.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

* **CTO / Responsabile Sviluppo**

  * **A**: politiche complessive di utilizzo GitHub, licenze, livelli di apertura (public vs private).
  * **R**: approvazione finale dei repository resi pubblici o delle release significative.
  * **C**: con Marketing per repos “vetrina”; con Legal/Commerciale per aspetti IP/contrattuali se necessario.
  * **I**: informato sui principali rilasci open-source.

* **Tech Lead / Maintainer di progetto (GitHub)**

  * **R**: creazione e configurazione del repository GitHub (nome, struttura, settings).
  * **R**: gestione versioni, tag, release, roadmap tecnica del pacchetto/prodotto.
  * **C**: con CTO per scelte di licenza e aperture importanti.
  * **I**: aggiorna il team (Dev, Marketing, PM) su roadmap e rilasci.

* **Developer**

  * **R**: contribuzione tecnica ai repository pubblici (attraverso PR/MR, issue, documentazione).
  * **C**: con Tech Lead per nuove funzionalità, bugfix e miglioramenti.
  * **I**: informato sulle linee guida di contribuzione e release.

* **DevOps Engineer**

  * **R**: eventuale setup di mirroring GitLab → GitHub e integrazioni CI/CD per automatizzare release.
  * **C**: con Tech Lead/CTO per pipeline, sicurezza, secret management.

* **Marketing / Comunicazione**

  * **C**: per repository che hanno impatto su brand e comunicazione esterna (es. prodotti, demo, AI, portali).
  * **I**: informato su nuovi rilasci pubblici, per eventuali attività di comunicazione.

* **Project Manager / Product Owner**

  * **R**: allineamento tra backlog (Odoo) e roadmap del pacchetto pubblico, quando il component è parte di un prodotto.
  * **C**: con Tech Lead per priorità e pianificazione rilasci.

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il processo di gestione dei repository pubblici e rilascio pacchetti su GitHub comprende:

1. **Valutazione di pubblicabilità** del codice o del componente.
2. **Scelta del tipo di repository** (open-source, esempio/dimostrativo, privato GitHub eccezionale).
3. **Creazione e configurazione del repository GitHub** (nome, visibilità, struttura, protezione branch).
4. **Definizione di licenza, README, CHANGELOG e linee guida di contribuzione**.
5. **Allineamento tecnico con GitLab** (mirroring, import/export, gestione sorgente principale).
6. **Gestione di versioning, tag e release**.
7. **Pubblicazione di documentazione e demo via GitHub Pages (se applicabile)**.
8. **Manutenzione del repository pubblico** (issue, PR, sicurezza, aggiornamento dipendenze).

---

### 5.2 Valutazione e approvazione della pubblicazione

1. **Proposta di pubblicazione**

   * Può essere iniziata da:

     * CTO / Responsabile Sviluppo;
     * Tech Lead/maintainer di un componente;
     * Developer (tramite proposta documentata);
     * Marketing (per asset demo e vetrina tecnica).

   * La proposta deve indicare almeno:

     * scopo del componente;
     * benefici della pubblicazione (riuso, visibilità, community, marketing);
     * sorgente del codice (progetto interno/prodotto/progetto cliente).

2. **Valutazione tecnica e IP**

   * A cura di CTO/Tech Lead, eventualmente con supporto Commerciale/Legal, verificando:

     * assenza di vincoli contrattuali o NDA che impediscano la pubblicazione;
     * assenza di codice proprietario del cliente o di terze parti non autorizzato;
     * assenza di dati sensibili o credenziali nel repository (anche nella history).

3. **Decisione di pubblicazione**

   * Il CTO approva (o respinge) la proposta e decide:

     * **tipo di repository**:

       * fully open-source;
       * codice di esempio/dimostrativo;
       * repository privato GitHub (caso eccezionale, es. con partner);

     * **licenza** da applicare (vedi §5.4).

---

### 5.3 Creazione e configurazione del repository GitHub

1. **Naming e struttura organizzativa**

   * I repository sono creati sotto l’**organizzazione GitHub aziendale**.
   * Convenzione di naming consigliata:

     * `{{prodotto}}-{{componente}}`
       es. `ai-toolkit-core`, `llm-integration-sdk`, `odoo-connector-template`.

2. **Visibilità**

   * Di default:

     * repository **pubblici** per componenti open-source/dimostrativi approvati;
     * repository **privati GitHub** solo se:

       * richiesti da specifiche collaborazioni esterne; e
       * approvati dal CTO.

3. **Branch principali**

   * Minimo:

     * `main` – branch stabile (rilasci pubblici);

   * Facoltativamente (per progetti più complessi):

     * `develop` – branch di integrazione.

   * Branch protetti:

     * `main` (e `develop` se usato) devono essere **protetti**:

       * niente push diretto;
       * merge solo via PR con check richiesti (CI, review).

4. **Impostazioni repository**

   * Abilitare:

     * **Issues** per segnalazioni bug/feature (se si accetta interazione pubblica);
     * **Pull Request** per contribuzioni esterne;
     * eventuali **template** per issue/PR (es. bug_report, feature_request).

---

### 5.4 Licenze, README e documentazione minima

1. **Licenza**

   * La scelta della licenza (MIT, Apache-2.0, GPL, ecc.) è effettuata da CTO/Tech Lead, in coerenza con:

     * obiettivi del repository;
     * eventuali dipendenze e licenze di terze parti;
     * strategia aziendale di open-source.

   * Il file `LICENSE` deve essere presente alla **root del repository**.

2. **README**

   Ogni repository GitHub deve avere un `README.md` con almeno:

   * descrizione sintetica del progetto (cosa fa, per chi è pensato);
   * requisiti minimi (linguaggi, runtime, dipendenze principali);
   * istruzioni di **installazione** e **utilizzo base**;
   * esempi minimi di codice/uso;
   * se pertinente: sezione “Contributing” con linee guida (branching, PR, coding style);
   * link a:

     * documentazione estesa (es. GitHub Pages, wiki, altri repo);
     * eventuale pagina prodotto/sito aziendale.

3. **CHANGELOG**

   * Per librerie/pacchetti versionati è fortemente raccomandato un `CHANGELOG.md` con:

     * elenco modifiche per versione (`[1.2.0] – yyyy-mm-dd`);
     * breve descrizione di nuove feature, bugfix, breaking changes.

4. **Altra documentazione**

   * Se necessario, aggiungere:

     * `/docs` per documentazione estesa;
     * esempi più complessi in `/examples` o `/demo`.

   * La pubblicazione di documentazione via GitHub Pages segue quanto indicato in **SOP-DOC-02**.

---

### 5.5 Sorgente principale: GitLab ↔ GitHub

1. **Principio generale**

   * **GitLab** è il sistema principale per lo **sviluppo interno** (SOP-DEV-01).
   * **GitHub** è usato per:

     * pubblicare snapshot o mirror del codice destinato a uso pubblico;
     * gestire rilasci open-source e contributi della community.

2. **Modalità operative**

   Possibili modalità, da scegliere per progetto:

   * **Mirror GitLab → GitHub**

     * il repository GitLab rimane “origine”;
     * GitHub è configurato come mirror (manuale o via CI), di norma su branch `main` (e tag).

   * **Import periodico**

     * per componenti semplici, si possono eseguire import/esport manuali (es. tag di release) da GitLab a GitHub.

   * In tutti i casi:

     * evitare sviluppo parallelo “non tracciato” su GitHub;
     * eventuali PR esterne su GitHub vanno poi integrate nel flusso GitLab (es. cherry-pick o sync) per non divergere.

---

### 5.6 Versioning, tag e release

1. **Schema di versionamento**

   * Per librerie/pacchetti si adotta, salvo diversa indicazione, **Semantic Versioning (SemVer)**:

     * `MAJOR.MINOR.PATCH` (es. `1.4.2`).

   * Regole generali:

     * incremento **MAJOR** per breaking changes;
     * incremento **MINOR** per nuove funzionalità retrocompatibili;
     * incremento **PATCH** per bugfix retrocompatibili.

2. **Tag Git**

   * Ogni release è associata a un **tag Git**:

     * naming: `vMAJOR.MINOR.PATCH` (es. `v1.2.0`);
     * tag creato preferibilmente su `main`.

3. **Release GitHub**

   * Per release significative:

     * creare una **Release** su GitHub collegata al tag;
     * includere nelle **release notes**:

       * highlights delle novità;
       * eventuali avvisi su breaking changes;
       * link al `CHANGELOG`.

4. **Distribuzione pacchetti su registri esterni**

   * Se il pacchetto viene pubblicato su:

     * npm, PyPI, altri registry;

   * il flusso specifico (CI/CD per publish) deve:

     * essere descritto in documentazione tecnica interna;
     * rispettare i principi di versioning e tagging di questo SOP;
     * utilizzare credenziali/secret gestiti in sicurezza (no commit di token).

---

### 5.7 Documentazione e demo tramite GitHub Pages

1. **Uso di GitHub Pages per librerie/progetti**

   * Può essere usato per:

     * documentazione API;
     * guide di utilizzo passo-passo;
     * demo UI o piccoli showcase.

   * La struttura tecnica del sito e il collegamento con il sito documentale principale sono disciplinati da **SOP-DOC-02**.

2. **Requisiti minimi**

   * coerenza grafica di base con il brand aziendale (SOP-MKT-01);
   * chiara indicazione di:

     * stato del progetto (alpha/beta/stable);
     * compatibilità (versioni supportate, dipendenze principali).

---

### 5.8 Manutenzione, sicurezza e qualità dei repository pubblici

1. **Manutenzione continua**

   * Il maintainer di progetto si occupa di:

     * triage delle issue (bug, feature request, domande);
     * gestione delle PR (review, merge, chiusure);
     * aggiornamento dipendenze (soprattutto se con vulnerabilità note);
     * aggiornamento README/CHANGELOG quando necessario.

2. **Controlli di sicurezza**

   * Prima di rendere pubblico un repository o una release:

     * verificare che **non** siano presenti:

       * secret, token, chiavi, password;
       * file di configurazione sensibili;
       * dati di test reali o dataset privati.

     * se la history contiene segreti, valutare:

       * *secret rotation*;
       * rimozione dei segreti dalla history (git filter-repo / strumenti analoghi);
       * rigenerazione del repository, se necessario.

3. **Gestione vulnerabilità**

   * In caso di vulnerabilità segnalate:

     * aprire issue dedicata;
     * definire priorità e piano di correzione;
     * rilasciare patch (nuova versione) e aggiornare CHANGELOG e release notes.

---

## 6. Strumenti e sistemi utilizzati

* **GitHub**

  * hosting repository pubblici/privati;
  * gestione Issues, Pull Request, Releases, GitHub Actions (se usate);
  * GitHub Pages per documentazione e demo (in coordinamento con SOP-DOC-02).

* **GitLab**

  * sorgente principale per sviluppo interno (SOP-DEV-01);
  * eventuale origin per il mirror verso GitHub.

* **Odoo (modulo Progetti / KB)**

  * tracciabilità dei progetti che producono componenti open-source;
  * collegamento da articoli KB a repository GitHub.

* **Google Drive**

  * conservazione di documentazione tecnica non pubblica collegata ai progetti (SOP-DOC-01).

* **Strumenti CI/CD**

  * GitLab CI o GitHub Actions per automatizzare build/test/release e pubblicazioni su registry.

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali del processo

* **R1 – Pubblicazione di contenuti sensibili**

  * Esposizione di segreti, dati cliente, IP non autorizzata su repository pubblici.

* **R2 – Violazioni di licenza**

  * Uso improprio di codice di terzi con licenze incompatibili.

* **R3 – Mancata manutenzione repository pubblici**

  * Repository obsoleti, non aggiornati, che danneggiano l’immagine aziendale.

* **R4 – Incoerenza tra GitLab e GitHub**

  * Divergenze tra il codice interno e quello pubblico, difficoltà di allineamento.

* **R5 – Versioning non gestito**

  * Rilasci senza regole di versioning chiare, che complicano l’adozione.

### 7.2 Controlli e misure di mitigazione

* **C1 – Revisione preventiva prima della pubblicazione**

  * Checklist obbligatoria (vedi allegato) per verificare assenza di segreti/dati sensibili.

* **C2 – Approvazione CTO per pubblicazioni**

  * Tutti i nuovi repository pubblici e release principali devono essere approvati.

* **C3 – Verifica licenze**

  * Controllo delle dipendenze e delle licenze prima di definire la licenza del progetto.

* **C4 – Revisione periodica repository pubblici**

  * Verifica almeno annuale dei repo pubblici per:

    * stato manutenzione;
    * presenza di issue critiche non gestite;
    * allineamento con strategia aziendale.

* **C5 – Linee guida di versioning**

  * Adozione SemVer e uso coerente di tag e release.

### 7.3 KPI / Indicatori (se applicabili)

Esempi di KPI:

* **KPI-OS-01 – N. repository pubblici attivi/manutenuti**
* **KPI-OS-02 – Tempo medio di risposta a issue pubbliche**
* **KPI-OS-03 – N. release/anno per pacchetto principale**
* **KPI-OS-04 – N. segnalazioni di vulnerabilità gestite entro X giorni**

Dettagli e target possono essere definiti in una scheda KPI dedicata o documenti di qualità.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* Il presente SOP è archiviato nel **repository documentale** secondo SOP-DOC-01 (es. `/SOP/SOP-DEV/`).
* La versione ufficiale approvata è resa disponibile:

  * nella **Odoo Knowledge Base** (categoria “SOP – Sviluppo Software”);
  * su **GitHub Pages** se incluso nel sito documentale dei SOP (SOP-DOC-02).

### 8.2 Revisione e aggiornamento

* Il SOP viene rivisto:

  * in caso di cambiamenti significativi nelle politiche di open-source o di utilizzo GitHub;
  * in caso di incidenti di sicurezza o non conformità;
  * a seguito di audit interni o feedback del team;
  * comunque entro la data di revisione prevista.

* Le modifiche vengono proposte da CTO, Tech Lead, DevOps, PM/PO e approvate dalla Direzione ove necessario.

### 8.3 Obbligatorietà e formazione

* Tutti gli sviluppatori, Tech Lead, DevOps e ruoli che pubblicano o mantengono repository GitHub devono conoscere il presente SOP.
* In occasione della prima emissione o di revisioni rilevanti:

  * il CTO organizza momenti di formazione/comunicazione;
  * può essere richiesta la presa visione tramite gli strumenti aziendali (KB Odoo, comunicazioni interne).

---

## 9. Allegati (opzionale)

* **Allegato 1 – Matrice RACI dettagliata per gestione repository GitHub**
* **Allegato 2 – Checklist pre-pubblicazione (controllo segreti, dati sensibili, IP)**
* **Allegato 3 – Linee guida interne sulle licenze open-source**
* **Allegato 4 – Template README per librerie/pacchetti**
* **Allegato 5 – Template CHANGELOG**
* **Allegato 6 – Linee guida per versioning e tagging (SemVer)**
* **Allegato 7 – Schema tipi di repository (open-source, demo, private GitHub eccezionali)**

*(Gli allegati sono archiviati nella stessa struttura del SOP o in cartelle dedicate collegate in Odoo KB.)*

---

## 10. Storico revisioni

| Versione | Data       | Descrizione modifica     | Redatto da                  | Verificato da                    | Approvato da             |
| -------- | ---------- | ------------------------ | --------------------------- | -------------------------------- | ------------------------ |
| 0.1      | 2025-11-16 | Prima emissione in bozza | CTO / Responsabile Sviluppo | Project Manager Progetti Interni | CEO / Direzione Generale |
