# SOP-DOC-03 – Struttura generale Google Drive multi-organizzazione (Schema macro-cartelle “v2”)

---

### 0. Metadati del documento

* **Codice SOP:** SOP-DOC-03
* **Titolo:** Struttura generale Google Drive multi-organizzazione (Schema macro-cartelle “v2”)
* **Versione:** 2.0
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Responsabile Qualità / Documentazione]*
* **Verificato da (se applicabile):** *[Ruolo/Funzionale]*
* **Approvato da:** *[Direzione]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

### 1.1 Scopo

Il presente SOP definisce la **struttura generale di Google Drive a livello di root**, in un contesto **multi-organizzazione** (es. società diverse, marchi, linee di business).

In particolare:

* stabilisce che nella root del Drive sia presente **una cartella per ciascuna organizzazione** gestita (società, brand, BU…);
* definisce le **macro-cartelle standard** presenti all’interno di ciascuna cartella-organizzazione, in funzione dello scopo (Anagrafiche, Commerciale, Progetti, Prodotti & Servizi, Formazione & Linee guida, Marketing & Comunicazione, Amministrazione & Finanza, Legale & Compliance, People & HR, IT Operations, Sicurezza, Template & Brand);
* descrive lo **scopo e l’utilizzo** di ciascuna macro-cartella, stabilendo criteri generali di collocazione dei documenti e **riducendo dispersione e duplicazioni**;
* chiarisce che la **struttura interna** (sottocartelle, naming di dettaglio, permessi fini, integrazione operativa con Odoo, ecc.) è disciplinata da **allegati specifici** (Allegati SOP-DOC-03-Axx), che fungono da “SOP di dettaglio” per ciascuna macro-cartella.

Questo SOP è quindi un **documento di cornice** sulla **mappa logica del Drive**:
non entra nelle procedure operative delle singole aree, che sono disciplinate da allegati dedicati.

### 1.2 Campo di applicazione

Il presente SOP si applica a:

* l’**intero Google Drive aziendale**, o al/i drive condiviso/i che ospitano i documenti di lavoro;
* tutte le **organizzazioni** gestite nel Drive (società del gruppo, marchi, linee di business, BU autonome);
* tutte le aree funzionali che utilizzano il Drive per la gestione documentale.

È direttamente collegato a:

* **SOP-DOC-01** (Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)), che presuppone la struttura definita in questo SOP;
* **SOP-DOC-02** (Pubblicazione documentazione e SOP su GitHub Pages), per distinguere ciò che ha fonte di verità in GitHub da ciò che è gestito in Drive.

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabili)

* **ISO 9001:2015** – Requisiti relativi alla gestione e al controllo delle informazioni documentate.
* **Regolamento (UE) 2016/679 – GDPR** – Per gli aspetti legati alla gestione di documenti contenenti dati personali.
* Eventuali norme di settore che impattano la conservazione e organizzazione dei documenti.

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-ORG-01 – Struttura organizzativa e sistema informativo aziendale**
* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
* **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**
* **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**

Allegati di dettaglio (parte integrante del presente SOP) per le singole macro-cartelle:

* **Allegato SOP-DOC-03-A00 – INBOX (regole, tempi di svuotamento, responsabilità)**
* **Allegato SOP-DOC-03-A01 – ANAGRAFICHE**
* **Allegato SOP-DOC-03-A02 – COMMERCIALE**
* **Allegato SOP-DOC-03-A03 – PROGETTI**
* **Allegato SOP-DOC-03-A04 – PRODOTTI_SERVIZI**
* **Allegato SOP-DOC-03-A05 – FORMATIVO_LINEE_GUIDA**
* **Allegato SOP-DOC-03-A06 – MARKETING_COMUNICAZIONE**
* **Allegato SOP-DOC-03-A07 – AMMINISTRAZIONE_FINANZA**
* **Allegato SOP-DOC-03-A08 – LEGALE_COMPLIANCE**
* **Allegato SOP-DOC-03-A09 – PEOPLE_HR**
* **Allegato SOP-DOC-03-A10 – IT_OPERATIONS**
* **Allegato SOP-DOC-03-A11 – SICUREZZA**
* **Allegato SOP-DOC-03-A12 – TEMPLATE_E_BRAND**

Eventuali **policy IT**, policy di **sicurezza** e **privacy** interne.

---

## 3. Definizioni, acronimi e abbreviazioni

* **Organizzazione** – Società, marchio, BU o linea di business per cui viene mantenuta una struttura documentale autonoma nel Drive (es. “ACME S.r.l.”, “Brand X”, “Business Unit Y”).
* **Cartella-organizzazione** – Cartella di primo livello nella root del Drive, dedicata a una specifica organizzazione (es. `ORG-001_ACME_SRL`).
* **Macro-cartella** – Cartella di secondo livello all’interno di una cartella-organizzazione, che raccoglie documenti per ambito (Anagrafiche, Commerciale, Progetti, ecc.).
* **Root Drive** – Livello più alto della struttura di Google Drive (unità condivisa o spazio principale) da cui dipendono tutte le cartelle-organizzazione.
* **INBOX** – Cartella di ingresso temporaneo per file non ancora classificati; non è un archivio definitivo.
* **Anagrafiche** – Documentazione collegata a soggetti anagrafici (clienti, fornitori, partner, ecc.), coerente con anagrafiche in Odoo.
* **Commerciale** – Documentazione presales e sales (offerte, proposte, presentazioni cliente, preventivi, materiali commerciali) coerente con pipeline e opportunità in Odoo.
* **Progetti** – Documentazione collegata a progetti e commesse (interni/esterni), coerente con gestione progetti in Odoo.
* **Prodotti e Servizi** – Documenti che descrivono, definiscono e supportano l’offerta aziendale.
* **Materiale formativo & Linee guida** – Documenti didattici, manuali operativi, istruzioni, linee guida interne.
* **Marketing & Comunicazione** – Materiali marketing e comunicazione (piani editoriali, campagne, contenuti, report, bozze operative).
* **Amministrazione & Finanza** – Documentazione amministrativa e finanziaria non interamente gestita in Odoo (o di supporto operativo).
* **Legale & Compliance** – Documentazione legale e di compliance “di pratica” (contratti reali, NDA firmati, DPA, audit legali, ecc.).
* **People & HR** – Documentazione HR/People (onboarding/offboarding, formazione obbligatoria, documentazione personale/ruoli ove applicabile).
* **IT Operations** – Documentazione operativa IT (runbook, configurazioni operative, procedure tecniche, inventari, guide strumenti) distinta dalla sicurezza.
* **Sicurezza** – Documentazione di sicurezza, privacy, compliance security, incident, audit, policy di sicurezza, controlli.
* **Template & Brand** – Libreria ufficiale di template e asset (template contratti e documenti, loghi, brand identity, linee guida, ecc.).
* **Fonte di verità** – Sistema e posizione in cui risiede la versione ufficiale di un documento.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

Il presente SOP riguarda la **struttura “fisica” del Drive**:

* come vengono organizzate le cartelle a livello di root;
* come vengono create e gestite le **cartelle-organizzazione**;
* quali **macro-cartelle** devono essere presenti per ciascuna organizzazione;
* lo scopo/uso generale di ciascuna macro-cartella (criteri di collocazione dei documenti).

Non disciplina:

* le modalità operative interne alle singole macro-cartelle (che sono demandate agli **Allegati SOP-DOC-03-Axx**);
* il dettaglio dell’integrazione Odoo/Drive (SOP-DOC-01);
* la gestione della documentazione ufficiale su GitHub (SOP-DOC-02).

### 4.2 Ruoli e responsabilità (RACI di alto livello)

**Legenda:** R = Responsible, A = Accountable, C = Consulted, I = Informed

* **Direzione**
  * A: approvazione del modello generale di struttura Drive multi-organizzazione.
  * C/I: informata sulle modifiche rilevanti (nuove organizzazioni, ristrutturazioni).

* **Responsabile Qualità / Documentazione**
  * A: definizione e mantenimento del presente SOP-DOC-03 e dei relativi Allegati Axx.
  * R: governo del modello di struttura root e coerenza con i SOP collegati (DOC-01, DOC-02, KB, ORG).
  * C: consultato in caso di creazione/eliminazione di cartelle-organizzazione o macro-cartelle.

* **Responsabile IT / CTO**
  * A: configurazione tecnica del Drive, gestione permessi degli strati root / organizzazione.
  * R: creazione fisica delle cartelle-organizzazione e delle macro-cartelle “base” secondo questo SOP.
  * C: per valutare impatti di nuove organizzazioni o ristrutturazioni.

* **Responsabili di Area / Owner degli Allegati SOP-DOC-03-Axx**
  * R: contenuti e regole operative all’interno delle macro-cartelle del proprio ambito (Anagrafiche, Commerciale, Progetti, ecc.).
  * C: in caso di modifica del modello di struttura root che impatta la propria area.

* **Tutto il personale**
  * R/I: utilizzo delle cartelle in coerenza con la struttura definita, con il presente SOP e con gli Allegati Axx di riferimento.

---

## 5. Descrizione del processo

### 5.1 Modello generale di root Drive

A livello di root, il Drive aziendale è organizzato secondo il seguente modello:

1. Per ogni **organizzazione** gestita, viene creata una **cartella-organizzazione**:

   * es. `ORG-001_ACME_SRL`, `ORG-002_BRAND_X`, `ORG-003_BUSINESS_UNIT_Y`.
   * regole di naming e gestione dettagliate in questo SOP (§5.3.1).

2. All’interno di ciascuna cartella-organizzazione sono presenti una serie di **macro-cartelle standard**, comuni a tutte le organizzazioni:

   * `00_INBOX`
   * `01_ANAGRAFICHE`
   * `02_COMMERCIALE`
   * `03_PROGETTI`
   * `04_PRODOTTI_SERVIZI`
   * `05_FORMATIVO_LINEE_GUIDA`
   * `06_MARKETING_COMUNICAZIONE`
   * `07_AMMINISTRAZIONE_FINANZA`
   * `08_LEGALE_COMPLIANCE`
   * `09_PEOPLE_HR`
   * `10_IT_OPERATIONS`
   * `11_SICUREZZA`
   * `12_TEMPLATE_E_BRAND`

3. Ogni macro-cartella è disciplinata da un **Allegato** (SOP-DOC-03-Axx) che definisce:

   * struttura interna (sottocartelle e convenzioni di naming specifiche);
   * modalità di collegamento con Odoo, GitHub, GitLab e/o altri sistemi;
   * ruoli, permessi e regole operative di dettaglio;
   * eventuali checklist e criteri di archiviazione.

Il presente SOP **non entra nel dettaglio interno** delle singole macro-cartelle, ma definisce:

* **obbligatorietà** delle cartelle-organizzazione;
* **presenza minima** delle macro-cartelle standard;
* **scopo e utilizzo** di ciascuna macro-cartella;
* **criteri di creazione e manutenzione**.

### 5.2 Scopo e utilizzo delle macro-cartelle (criteri generali)

Di seguito lo scopo e l’uso atteso di ciascuna macro-cartella; la struttura interna e le regole operative di dettaglio sono negli **Allegati**.

#### 00_INBOX
**Scopo:** punto di ingresso temporaneo per file ricevuti o creati “al volo” non ancora classificati.  
**Uso:** depositare documenti da smistare; non è un archivio definitivo.  
**Regole:** tempi massimi di permanenza e responsabilità di svuotamento sono definiti in **Allegato SOP-DOC-03-A00**.

#### 01_ANAGRAFICHE
**Scopo:** documentazione associata a soggetti anagrafici (clienti, fornitori, partner, contatti chiave).  
**Uso:** raccogliere documenti collegati alle anagrafiche presenti in Odoo (coerenza e tracciabilità).  
**Dettaglio:** struttura interna, naming e mapping Odoo definiti in **Allegato SOP-DOC-03-A01**.

#### 02_COMMERCIALE
**Scopo:** documentazione di presales/sales (offerte, proposte, presentazioni cliente, preventivi, analisi, materiali commerciali specifici).  
**Uso:** supportare la gestione della pipeline e delle opportunità; i documenti sono normalmente collegati a record CRM/Odoo quando applicabile.  
**Dettaglio:** struttura interna e regole operative in **Allegato SOP-DOC-03-A02**.

#### 03_PROGETTI
**Scopo:** documentazione di progetto/commessa (delivery, analisi, meeting, piani, deliverable, documenti cliente di progetto).  
**Uso:** repository operativo della documentazione di progetto, coerente con la gestione progetti in Odoo.  
**Dettaglio:** struttura interna e mapping progetti Odoo in **Allegato SOP-DOC-03-A03**.

#### 04_PRODOTTI_SERVIZI
**Scopo:** documentazione relativa a prodotti/servizi/soluzioni (schede, configurazioni, presentazioni tecniche, materiali standard di offerta).  
**Uso:** mantenere un catalogo operativo per supportare commerciale e delivery; distinguere tra documenti “stabili” (eventualmente pubblicabili) e documenti operativi.  
**Dettaglio:** regole e struttura in **Allegato SOP-DOC-03-A04** e coerenza con SOP-DOC-02 (pubblicazione su GitHub Pages se pertinente).

#### 05_FORMATIVO_LINEE_GUIDA
**Scopo:** materiale formativo interno e linee guida operative (how-to, procedure non formalizzate in SOP, guide all’uso strumenti/processi).  
**Uso:** supportare onboarding, aggiornamento competenze e standardizzazione operativa; quando un contenuto diventa “ufficiale/stabile” può essere candidato a pubblicazione su GitHub Pages secondo SOP-DOC-02.  
**Dettaglio:** struttura interna e criteri in **Allegato SOP-DOC-03-A05**.

#### 06_MARKETING_COMUNICAZIONE
**Scopo:** contenuti e materiali operativi di marketing e comunicazione (piani editoriali, campagne, creatività, bozze, report performance, asset operativi).  
**Uso:** gestione del lavoro marketing (non libreria “master” dei template/brand, che risiede in 12_TEMPLATE_E_BRAND).  
**Dettaglio:** struttura interna e regole in **Allegato SOP-DOC-03-A06**.

#### 07_AMMINISTRAZIONE_FINANZA
**Scopo:** documentazione amministrativa e finanziaria di supporto (prospetti di lavoro, report, riconciliazioni operative, documenti amministrativi non gestiti interamente in Odoo).  
**Uso:** supportare i processi amministrativi garantendo ordine e reperibilità; separata dalla cartella Legale.  
**Dettaglio:** struttura interna e regole in **Allegato SOP-DOC-03-A07**.

#### 08_LEGALE_COMPLIANCE
**Scopo:** documentazione legale e di compliance “di pratica” (contratti reali e firmati, NDA firmati, DPA, audit legali, documenti vincolanti, evidenze compliance).  
**Uso:** conservazione e tracciabilità della documentazione legale operativa; i **template** legali non risiedono qui ma in 12_TEMPLATE_E_BRAND.  
**Dettaglio:** struttura interna e criteri di accesso/permessi in **Allegato SOP-DOC-03-A08**.

#### 09_PEOPLE_HR
**Scopo:** documentazione People/HR (onboarding/offboarding, formazione obbligatoria, ruoli/job description, procedure HR, documentazione interna HR ove applicabile).  
**Uso:** supportare la gestione del personale e i processi HR; attenzione a privacy e permessi.  
**Dettaglio:** struttura interna, criteri privacy e permessi in **Allegato SOP-DOC-03-A09**.

#### 10_IT_OPERATIONS
**Scopo:** documentazione operativa IT (runbook, procedure tecniche, configurazioni operative, inventario asset, guide strumenti, istruzioni operative).  
**Uso:** repository operativo per IT; distinta dalla Sicurezza, che contiene policy/audit/incident.  
**Dettaglio:** struttura interna e regole in **Allegato SOP-DOC-03-A10**.

#### 11_SICUREZZA
**Scopo:** documentazione di sicurezza, privacy e compliance security (policy, controlli, audit, incident, evidenze, piani di mitigazione, procedure di sicurezza).  
**Uso:** tenere separati contenuti security/compliance rispetto a IT Operations.  
**Dettaglio:** struttura interna, classificazione e permessi in **Allegato SOP-DOC-03-A11**.

#### 12_TEMPLATE_E_BRAND
**Scopo:** libreria ufficiale di **template e asset** dell’organizzazione, per evitare dispersione e garantire coerenza.  
**Uso:** raccogliere esclusivamente materiali “master/ufficiali”, tra cui:
* template di contratti (NDA, contratti, DPA, condizioni, lettere, procure, ecc.);
* template documenti (offerte, report, verbali, presentazioni standard, intestazioni);
* asset grafici (loghi, icone, immagini, illustrazioni, elementi visual ufficiali);
* documenti di brand identity (linee guida, tone of voice, palette, tipografia, usage rules).  
I documenti “operativi” derivati dai template (es. una specifica offerta cliente) risiedono in 02_COMMERCIALE o 03_PROGETTI, non in questa cartella.  
**Dettaglio:** struttura interna, versioning e regole di aggiornamento in **Allegato SOP-DOC-03-A12**.

### 5.3 Flusso operativo di alto livello

1. **Nuova organizzazione da gestire in Drive**
   * La Direzione o il Responsabile Qualità / Documentazione richiedono la creazione di una nuova **organizzazione** (nuova società, brand, BU).
   * Viene verificata la coerenza con SOP-ORG-01 (struttura organizzativa ufficiale).

2. **Creazione cartella-organizzazione**
   * Il Responsabile IT / CTO (o figura delegata):
     * crea la cartella-organizzazione nella root del Drive secondo le regole di naming (§5.4.1);
     * assegna i permessi di base (visibilità per Direzione, Responsabili di area, ecc.);
     * crea le **macro-cartelle standard** (§5.4.2).

3. **Configurazione delle macro-cartelle secondo Allegati**
   * I Responsabili di area/Owner degli Allegati SOP-DOC-03-Axx:
     * completano l’eventuale struttura interna (sottocartelle, naming specifico) secondo il proprio Allegato;
     * definiscono/validano i permessi più fini (chi può vedere cosa) all’interno della propria macro-cartella.

4. **Utilizzo operativo**
   * Il personale usa le cartelle secondo:
     * regole generali del presente SOP (collocazione corretta dei documenti);
     * regole operative degli Allegati Axx.
   * L’integrazione con Odoo (link a cartelle clienti, progetti, etc.) è gestita secondo SOP-DOC-01.

5. **Manutenzione e ristrutturazione**
   * Eventuali modifiche strutturali (rinomina dell’organizzazione, chiusura, merge, split) sono gestite:
     * a livello di root dal Responsabile IT / CTO,
     * a livello operativo di contenuto dai Responsabili di area,
     * con aggiornamento del presente SOP e/o degli Allegati, se necessario.

6. **Revisione periodica**
   * Con frequenza definita (es. annuale), Responsabile Qualità / Documentazione e Responsabile IT / CTO:
     * verificano che per ogni organizzazione esista la cartella-organizzazione con tutte le macro-cartelle standard;
     * rilevano anomalie (macro-cartelle mancanti, rename “creativi”, duplicazioni parallele).

### 5.4 Istruzioni operative / Dettaglio per fasi

#### 5.4.1 Regole per le cartelle-organizzazione

**Naming standard**:

`ORG-XXX_NomeOrganizzazione`

dove:

* `ORG-XXX` = codice univoco numerico o alfanumerico (es. `ORG-001`, `ORG-ACME`);
* `NomeOrganizzazione` = ragione sociale o nome breve del marchio, senza caratteri speciali (es. `ACME_SRL`, `BRAND_X`).

Esempi:

* `ORG-001_ACME_SRL`
* `ORG-002_BRAND_X`
* `ORG-003_BUSINESS_UNIT_Y`

**Regole generali**:

* Ogni organizzazione riconosciuta in **SOP-ORG-01** deve avere **esattamente una** cartella-organizzazione in root.

* È vietato creare cartelle di primo livello diverse da quelle:
  * di sistema (gestite da IT se necessario);
  * `ORG-XXX_…` definite in questo SOP.

* Eventuali cartelle “storiche” di primo livello, non conformi, devono essere:
  * migrate nella nuova struttura;
  * archiviate o rimosse secondo valutazione congiunta Qualità / IT.

#### 5.4.2 Macro-cartelle standard per ogni organizzazione

All’interno di ciascuna `ORG-XXX_NomeOrganizzazione` devono essere presenti **almeno** le seguenti macro-cartelle (set minimo obbligatorio):

* `00_INBOX`
* `01_ANAGRAFICHE`
* `02_COMMERCIALE`
* `03_PROGETTI`
* `04_PRODOTTI_SERVIZI`
* `05_FORMATIVO_LINEE_GUIDA`
* `06_MARKETING_COMUNICAZIONE`
* `07_AMMINISTRAZIONE_FINANZA`
* `08_LEGALE_COMPLIANCE`
* `09_PEOPLE_HR`
* `10_IT_OPERATIONS`
* `11_SICUREZZA`
* `12_TEMPLATE_E_BRAND`

**Nota:**
Questo elenco definisce il **set minimo obbligatorio**. Ogni organizzazione può avere, in accordo con Responsabile Qualità / IT, macro-cartelle aggiuntive, purché documentate e coerenti con la struttura complessiva.

#### 5.4.3 Ruoli e rimandi agli Allegati (struttura interna)

Per evitare duplicazioni, il presente SOP **non descrive** la struttura interna e le regole operative di dettaglio di ciascuna macro-cartella.  
Tali aspetti sono disciplinati negli **Allegati SOP-DOC-03-Axx**, parte integrante del presente documento:

* **SOP-DOC-03-A00** – INBOX  
* **SOP-DOC-03-A01** – ANAGRAFICHE  
* **SOP-DOC-03-A02** – COMMERCIALE  
* **SOP-DOC-03-A03** – PROGETTI  
* **SOP-DOC-03-A04** – PRODOTTI_SERVIZI  
* **SOP-DOC-03-A05** – FORMATIVO_LINEE_GUIDA  
* **SOP-DOC-03-A06** – MARKETING_COMUNICAZIONE  
* **SOP-DOC-03-A07** – AMMINISTRAZIONE_FINANZA  
* **SOP-DOC-03-A08** – LEGALE_COMPLIANCE  
* **SOP-DOC-03-A09** – PEOPLE_HR  
* **SOP-DOC-03-A10** – IT_OPERATIONS  
* **SOP-DOC-03-A11** – SICUREZZA  
* **SOP-DOC-03-A12** – TEMPLATE_E_BRAND  

---

## 6. Strumenti e sistemi utilizzati

* **Google Drive**
  * Contiene la struttura root multi-organizzazione descritta nel presente SOP.
  * È gestito tecnicamente dal Responsabile IT / CTO per quanto riguarda permessi e struttura di alto livello.

* **Odoo**
  * Le cartelle `01_ANAGRAFICHE` e `03_PROGETTI` sono integrate con Odoo (contatti, progetti) secondo SOP-DOC-01, SOP-CRM-01, SOP-PRJ-01.
  * La KB Odoo può referenziare cartelle e risorse pertinenti (es. formazione, template ufficiali) secondo SOP-KB-01 e SOP-DOC-01.

* **GitHub / GitHub Pages**
  * Ospita i SOP e la documentazione ufficiale (fonte di verità) secondo SOP-DOC-02.
  * La struttura Drive deve essere coerente con quanto dichiarato nella documentazione ufficiale e nei rimandi KB.

* **GitLab**
  * Gestisce codice sorgente e documentazione integrata al codice (non direttamente oggetto del presente SOP), ma può referenziare documentazione e asset operativi dove previsto.

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali

* **Rischio di disallineamento strutturale**
  * Cartelle-organizzazione mancanti, duplicate o rinominate senza coordinamento.
  * Macro-cartelle assenti o denominate in modo non standard.

* **Rischio di dispersione documentale**
  * Documenti archiviati in cartelle “improvvisate” anziché nelle macro-cartelle corrette.
  * Difficoltà nel reperire documenti a livello di organizzazione.

* **Rischio di incoerenza con Odoo**
  * Struttura Drive non coerente con anagrafiche, progetti e processi mappati in Odoo (impatto su SOP-DOC-01).

* **Rischio di duplicazione dei “master”**
  * Template e asset duplicati tra aree (Commerciale/Marketing/Legale) con perdita di coerenza; mitigato dalla cartella `12_TEMPLATE_E_BRAND`.

### 7.2 Controlli e misure di mitigazione

* **Audit periodici (almeno annuali)**:
  * Verifica che per ogni organizzazione esista una cartella-organizzazione correttamente nominata.
  * Verifica della presenza di tutte le macro-cartelle standard (inclusa `12_TEMPLATE_E_BRAND`).
  * Verifica campionaria su corretto utilizzo (collocazione documenti “master” vs documenti operativi).

* **Checklist di creazione organizzazione**:
  * Ogni nuova organizzazione non è considerata “attiva” finché non sono create cartella-organizzazione e macro-cartelle.

* **Allineamento con SOP-DOC-01**:
  * Ogni revisione importante di SOP-DOC-01 o di SOP-ORG-01 comporta una verifica di coerenza con la struttura root Drive.

### 7.3 KPI / Indicatori (se applicabili)

Esempi:

* **% organizzazioni con struttura di macro-cartelle completa e conforme** (target ≥ 95%).
* **Numero di cartelle di primo livello non conformi** rilevate per audit.
* **Numero di segnalazioni interne** relative a difficoltà nel reperimento documenti dovute a struttura non conforme.
* **Numero di duplicati “master” rilevati** (template/asset non allineati) per periodo.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* La **fonte di verità** del presente SOP è il file sorgente nel repository GitHub documentazione (vedi SOP-DOC-02).
* La versione ufficiale è pubblicata su **GitHub Pages**.
* Un articolo in **Odoo KB** (categoria “SOP – Documentazione & Gestione Documentale”) riporta:
  * codice, titolo, versione;
  * breve descrizione;
  * link alla pagina GitHub Pages.

Eventuali bozze o note di lavoro possono essere temporaneamente salvate su Drive ma non costituiscono la versione ufficiale.

### 8.2 Revisione e aggiornamento

La revisione del presente SOP è attivata in caso di:

* introduzione di nuove organizzazioni o modifica del perimetro delle organizzazioni esistenti;
* modifiche importanti nella strategia documentale (ad es. nuove macro-cartelle standard);
* non conformità emerse da audit;
* modifiche a SOP-ORG-01, SOP-DOC-01 o SOP-DOC-02 che impattino la struttura root;
* necessità di rivedere scopi/ambiti delle macro-cartelle o degli Allegati Axx.

Ogni revisione comporta:

* aggiornamento della versione e della data di emissione;
* aggiornamento della sezione 10 – Storico revisioni;
* eventuale comunicazione interna.

### 8.3 Obbligatorietà e formazione

* Il **Responsabile IT / CTO** e il **Responsabile Qualità / Documentazione** devono conoscere e applicare il presente SOP per qualsiasi intervento sulla root del Drive.
* I **Responsabili di area** devono conoscere almeno:
  * collocazione della propria macro-cartella;
  * regole di base per non alterare la struttura root e per non duplicare template/asset fuori da `12_TEMPLATE_E_BRAND`.
* Il personale deve essere informato che:
  * le cartelle di primo livello si creano **solo** per nuove organizzazioni e **solo** secondo questo SOP;
  * per qualsiasi nuova esigenza di macro-cartella o modifica agli Allegati, si deve passare tramite Responsabile Qualità / IT.

---

## 9. Allegati (parte integrante)

* **Allegato SOP-DOC-03-A00 – INBOX**
* **Allegato SOP-DOC-03-A01 – ANAGRAFICHE**
* **Allegato SOP-DOC-03-A02 – COMMERCIALE**
* **Allegato SOP-DOC-03-A03 – PROGETTI**
* **Allegato SOP-DOC-03-A04 – PRODOTTI_SERVIZI**
* **Allegato SOP-DOC-03-A05 – FORMATIVO_LINEE_GUIDA**
* **Allegato SOP-DOC-03-A06 – MARKETING_COMUNICAZIONE**
* **Allegato SOP-DOC-03-A07 – AMMINISTRAZIONE_FINANZA**
* **Allegato SOP-DOC-03-A08 – LEGALE_COMPLIANCE**
* **Allegato SOP-DOC-03-A09 – PEOPLE_HR**
* **Allegato SOP-DOC-03-A10 – IT_OPERATIONS**
* **Allegato SOP-DOC-03-A11 – SICUREZZA**
* **Allegato SOP-DOC-03-A12 – TEMPLATE_E_BRAND**

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica           | Redatto da                   | Verificato da  | Approvato da  |
| -------- | ------------ | ------------------------------ | ---------------------------- | -------------- | ------------- |
| 1.0      | *[da comp.]* | Prima emissione del SOP-DOC-03 | *[Responsabile Qualità/Doc]* | *[Ruolo/Nome]* | *[Direzione]* |