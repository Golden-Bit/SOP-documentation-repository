# SOP-DOC-03 – Struttura generale Google Drive multi-organizzazione

---

### 0. Metadati del documento

* **Codice SOP:** SOP-DOC-03
* **Titolo:** Struttura generale Google Drive multi-organizzazione
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

Il presente SOP definisce la **struttura generale di Google Drive a livello di root**, in un contesto **multi-organizzazione** (es. società diverse, marchi, linee di business).

In particolare:

* stabilisce che nella root del Drive sia presente **una cartella per ciascuna organizzazione** gestita (società, brand, BU…);
* definisce le **tipologie standard di cartelle** presenti all’interno di ciascuna cartella-organizzazione, in funzione dello scopo (Anagrafiche, Progetti, Formazione & Linee guida, Contabilità, Prodotti & Servizi, Template & Grafiche, Marketing, Sicurezza…);
* descrive i **criteri generali di utilizzo** di tali macro-cartelle,
  **rimandando ai relativi SOP-DOC specifici** per le regole di dettaglio (struttura interna, naming, permessi, integrazione con Odoo, ecc.).

Questo SOP è quindi un **documento di cornice** sulla **mappa logica del Drive**:
non entra nelle procedure operative delle singole aree, che sono disciplinate da SOP dedicati.

### Campo di applicazione

Il presente SOP si applica a:

* l’**intero Google Drive aziendale**, o al/i drive condiviso/i che ospitano i documenti di lavoro;
* tutte le **organizzazioni** gestite nel Drive (società del gruppo, marchi, linee di business, BU autonome);
* tutte le aree funzionali che utilizzano il Drive per la gestione documentale.

È direttamente collegato a:

* **SOP-DOC-01** (Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)), che presuppone la struttura definita in questo SOP;
* **SOP-DOC-02** (pubblicazione documentazione e SOP su GitHub Pages), per distinguere ciò che ha fonte di verità in GitHub da ciò che è gestito in Drive.

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

SOP specifici (da redigere) a cui il presente documento rimanda per le singole macro-cartelle:

* **SOP-DOC-04 – Gestione cartelle Anagrafiche su Google Drive**
* **SOP-DOC-05 – Gestione cartelle Progetti su Google Drive**
* **SOP-DOC-06 – Gestione cartelle Materiale formativo e Linee guida su Google Drive**
* **SOP-DOC-07 – Gestione cartelle Contabilità & Amministrazione su Google Drive**
* **SOP-DOC-08 – Gestione cartelle Prodotti e Servizi su Google Drive**
* **SOP-DOC-09 – Gestione cartelle Template & Grafica su Google Drive**
* **SOP-DOC-10 – Gestione cartelle Marketing su Google Drive**
* **SOP-DOC-11 – Gestione cartelle Sicurezza & Compliance su Google Drive**

Eventuali **policy IT**, policy di **sicurezza** e **privacy** interne.

---

## 3. Definizioni, acronimi e abbreviazioni

* **Organizzazione** – Società, marchio, BU o linea di business per cui viene mantenuta una struttura documentale autonoma nel Drive (es. “ACME S.r.l.”, “Brand X”, “Business Unit Y”).
* **Cartella-organizzazione** – Cartella di primo livello nella root del Drive, dedicata a una specifica organizzazione (es. `ORG-001_ACME_SRL`).
* **Macro-cartella** – Cartella di secondo livello all’interno di una cartella-organizzazione, che raccoglie documenti per ambito (Anagrafiche, Progetti, ecc.).
* **Root Drive** – Livello più alto della struttura di Google Drive (unità condivisa o spazio principale) da cui dipendono tutte le cartelle-organizzazione.
* **Anagrafiche** – Documentazione collegata a soggetti anagrafici (clienti, fornitori, partner, ecc.), coerente con anagrafiche in Odoo.
* **Progetti** – Documentazione collegata a progetti e commesse (interni/esterni).
* **Materiale formativo & Linee guida** – Documenti didattici, manuali operativi, istruzioni, linee guida interne.
* **Contabilità** – Documentazione amministrativo-contabile non gestita direttamente in Odoo.
* **Prodotti e Servizi** – Documenti che descrivono, definiscono e supportano l’offerta aziendale.
* **Template & Grafica** – Modelli di documenti, presentazioni, grafica istituzionale, elementi di brand.
* **Marketing** – Materiali marketing, piani editoriali, campagne, contenuti.
* **Sicurezza & Compliance** – Documentazione relativa a sicurezza informatica, compliance, privacy, policy di sicurezza.

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

Il presente SOP riguarda la **struttura “fisica” del Drive**:

* come vengono organizzate le cartelle a livello di root;
* come vengono create e gestite le **cartelle-organizzazione**;
* quali **macro-cartelle** devono essere presenti per ciascuna organizzazione.

Non disciplina:

* le modalità operative interne alle singole macro-cartelle (che sono demandate ai relativi SOP-DOC-04…11);
* il dettaglio dell’integrazione Odoo/Drive (SOP-DOC-01);
* la gestione della documentazione ufficiale su GitHub (SOP-DOC-02).

### 4.2 Ruoli e responsabilità (RACI di alto livello)

**Legenda:** R = Responsible, A = Accountable, C = Consulted, I = Informed

* **Direzione**

  * A: approvazione del modello generale di struttura Drive multi-organizzazione.
  * C/I: informata sulle modifiche rilevanti (nuove organizzazioni, ristrutturazioni).

* **Responsabile Qualità / Documentazione**

  * A: definizione e mantenimento del presente SOP-DOC-03.
  * R: governo del modello di struttura root e coerenza con i SOP di dettaglio (DOC-01, DOC-02, DOC-04…11).
  * C: consultato in caso di creazione/eliminazione di cartelle-organizzazione o macro-cartelle.

* **Responsabile IT / CTO**

  * A: configurazione tecnica del Drive, gestione permessi degli strati root / organizzazione.
  * R: creazione fisica delle cartelle-organizzazione e delle macro-cartelle “base” secondo questo SOP.
  * C: per valutare impatti di nuove organizzazioni o ristrutturazioni.

* **Responsabili di Area / Owner di SOP-DOC-04…11**

  * R: contenuti e regole operative all’interno delle macro-cartelle del proprio ambito (Anagrafiche, Progetti, Formazione, ecc.).
  * C: in caso di modifica del modello di struttura root che impatta la propria area.

* **Tutto il personale**

  * R/I: utilizzo delle cartelle in coerenza con la struttura definita e con i SOP specifici di area.

---

## 5. Descrizione del processo

### 5.1 Modello generale di root Drive

A livello di root, il Drive aziendale è organizzato secondo il seguente modello:

1. Per ogni **organizzazione** gestita, viene creata una **cartella-organizzazione**:

   * es. `ORG-001_ACME_SRL`, `ORG-002_BRAND_X`, `ORG-003_BUSINESS_UNIT_Y`.
   * regole di naming e gestione dettagliate in questo SOP (§5.3.1).

2. All’interno di ciascuna cartella-organizzazione sono presenti una serie di **macro-cartelle standard**, comuni a tutte le organizzazioni:

   * `ANAGRAFICHE` – clienti, fornitori, partner, contatti chiave;
   * `PROGETTI` – progetti e commesse (interne/esterne);
   * `FORMATIVO_LINEE_GUIDA` – materiale formativo interno, guide operative, procedure non formalizzate in SOP;
   * `CONTABILITA` – documenti amministrativi e contabili (in coerenza con SOP-ACC-01);
   * `PRODOTTI_SERVIZI` – documentazione relativa a prodotti, servizi, offerte standard;
   * `TEMPLATE_GRAFICA` – template di documenti, presentazioni, materiali grafici e branding;
   * `MARKETING` – contenuti, campagne, piani editoriali, asset marketing;
   * `SICUREZZA` – documentazione di sicurezza, compliance, privacy, audit.

3. Ogni macro-cartella è disciplinata da un **SOP specifico** (DOC-04…11) che definisce:

   * struttura interna (sottocartelle, convenzioni di naming specifiche);
   * modalità di collegamento con Odoo, GitHub, GitLab, eventuali altri sistemi;
   * ruoli, permessi e regole operative di dettaglio.

Il presente SOP **non entra nel dettaglio interno** delle singole macro-cartelle, ma definisce:

* **obbligatorietà** delle cartelle-organizzazione;
* **presenza minima** delle macro-cartelle standard;
* **criteri di creazione e manutenzione**.

### 5.2 Flusso operativo di alto livello

1. **Nuova organizzazione da gestire in Drive**

   * La Direzione o il Responsabile Qualità / Documentazione richiedono la creazione di una nuova **organizzazione** (nuova società, brand, BU).
   * Viene verificata la coerenza con SOP-ORG-01 (struttura organizzativa ufficiale).

2. **Creazione cartella-organizzazione**

   * Il Responsabile IT / CTO (o figura delegata):

     * crea la cartella-organizzazione nella root del Drive secondo le regole di naming (§5.3.1);
     * assegna i permessi di base (visibilità per Direzione, Responsabili di area, ecc.);
     * crea le **macro-cartelle standard** (§5.3.2).

3. **Configurazione delle macro-cartelle secondo SOP specifici**

   * I Responsabili di area/Owner dei SOP-DOC-04…11:

     * completano l’eventuale struttura interna (sottocartelle, naming specifico) secondo il proprio SOP;
     * definiscono/validano i permessi più fini (chi può vedere cosa) all’interno della propria macro-cartella.

4. **Utilizzo operativo**

   * Il personale usa le cartelle secondo le regole:

     * generali del presente SOP (cosa va in quale macro-cartella);
     * specifiche dei SOP target (DOC-04…11).
   * L’integrazione con Odoo (link a cartelle clienti, progetti, etc.) è gestita secondo SOP-DOC-01.

5. **Manutenzione e ristrutturazione**

   * Eventuali modifiche strutturali (rinomina dell’organizzazione, chiusura, merge, split) sono gestite:

     * a livello di root dal Responsabile IT / CTO,
     * a livello operativo di contenuto dai Responsabili di area,
     * con aggiornamento dei relativi SOP e della KB, se necessario.

6. **Revisione periodica**

   * Con frequenza definita (es. annuale), Responsabile Qualità / Documentazione e Responsabile IT / CTO:

     * verificano che per ogni organizzazione esista la cartella-organizzazione con tutte le macro-cartelle standard;
     * rilevano anomalie (macro-cartelle mancanti, rename “creativi”, duplicazioni parallele).

### 5.3 Istruzioni operative / Dettaglio per fasi

#### 5.3.1 Regole per le cartelle-organizzazione

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

#### 5.3.2 Macro-cartelle standard per ogni organizzazione

All’interno di ciascuna `ORG-XXX_NomeOrganizzazione` devono essere presenti **almeno** le seguenti macro-cartelle:

* `ANAGRAFICHE`

  * Documentazione collegata a **clienti, fornitori, partner, altri contatti**.
  * Collegate alle anagrafiche Odoo secondo SOP-DOC-04 e SOP-CRM-01.

* `PROGETTI`

  * Documentazione dei **progetti e commesse** (interne o verso clienti).
  * Collegate ai progetti Odoo secondo SOP-DOC-05 e SOP-PRJ-01.

* `FORMATIVO_LINEE_GUIDA`

  * Materiale formativo interno, linee guida operative, “how-to”, check list operative.
  * Coerente con la strategia documentale definita in SOP-DOC-04 e con SOP-DOC-02 (per eventuale pubblicazione ufficiale su GitHub Pages).

* `CONTABILITA`

  * Documentazione amministrativo-contabile non gestita interamente in Odoo (es. prospetti di lavoro, fogli di controllo, report di sintesi).
  * Coerente con SOP-DOC-07 e SOP-ACC-01.

* `PRODOTTI_SERVIZI`

  * Documentazione relativa a prodotti, servizi, soluzioni (schede, configurazioni, listini operativi…).
  * Coerente con SOP-DOC-08 e con l’eventuale documentazione ufficiale su GitHub.

* `TEMPLATE_GRAFICA`

  * Template di documenti (Word, PowerPoint, Excel, ecc.), modelli di offerte, contratti, e materiali di identità visiva (loghi, palette, layout).
  * Coerente con SOP-DOC-09 e con SOP-MKT-01 per gli aspetti di branding.

* `MARKETING`

  * Materiali marketing (bozze post, creatività, piani editoriali, report campagne, materiali promozionali).
  * Coerente con SOP-DOC-10 e i SOP di macro-area Marketing (SOP-MKT-01…06).

* `SICUREZZA`

  * Documenti relativi a sicurezza informatica, policy, compliance, audit, privacy interni per l’organizzazione.
  * Coerente con SOP-DOC-11 e con eventuali SOP/policy IT.

**Nota:**
Questo elenco definisce il **set minimo obbligatorio**. Ogni organizzazione può avere, in accordo con Responsabile Qualità / IT, macro-cartelle aggiuntive, purché documentate e coerenti con la struttura complessiva.

#### 5.3.3 Ruoli e rimandi ai SOP specifici

Per evitare duplicazioni, il presente SOP **non descrive**:

* la struttura interna di `ANAGRAFICHE` (es. cartelle clienti vs fornitori, naming clienti…);
* la struttura interna di `PROGETTI` (cartelle per progetto, anno, ecc.);
* i dettagli di `FORMATIVO_LINEE_GUIDA`, `CONTABILITA`, `PRODOTTI_SERVIZI`, `TEMPLATE_GRAFICA`, `MARKETING`, `SICUREZZA`.

Tali aspetti sono disciplinati nei SOP:

* **SOP-DOC-04 – Gestione cartelle Anagrafiche su Google Drive**
* **SOP-DOC-05 – Gestione cartelle Progetti su Google Drive**
* **SOP-DOC-06 – Gestione cartelle Materiale formativo e Linee guida su Google Drive**
* **SOP-DOC-07 – Gestione cartelle Contabilità & Amministrazione su Google Drive**
* **SOP-DOC-08 – Gestione cartelle Prodotti e Servizi su Google Drive**
* **SOP-DOC-09 – Gestione cartelle Template & Grafica su Google Drive**
* **SOP-DOC-10 – Gestione cartelle Marketing su Google Drive**
* **SOP-DOC-11 – Gestione cartelle Sicurezza & Compliance su Google Drive**

---

## 6. Strumenti e sistemi utilizzati

* **Google Drive**

  * Contiene la struttura root multi-organizzazione descritta nel presente SOP.
  * È gestito tecnicamente dal Responsabile IT / CTO per quanto riguarda permessi e struttura di alto livello.

* **Odoo**

  * Le cartelle `ANAGRAFICHE` e `PROGETTI` sono integrate con Odoo (contatti, progetti) secondo SOP-DOC-01, SOP-CRM-01, SOP-PRJ-01.
  * La KB Odoo può referenziare sotto-cartelle specifiche di `FORMATIVO_LINEE_GUIDA`, `TEMPLATE_GRAFICA`, ecc.

* **GitHub / GitHub Pages**

  * Ospita i SOP e la documentazione ufficiale (fonte di verità) secondo SOP-DOC-02.
  * La struttura root Drive deve essere coerente con quanto dichiarato nella documentazione ufficiale.

* **GitLab**

  * Gestisce codice sorgente e documentazione integrata al codice (non direttamente oggetto del presente SOP), ma può referenziare cartelle `PROGETTI`, `PRODOTTI_SERVIZI`, ecc.

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

### 7.2 Controlli e misure di mitigazione

* **Audit periodici (almeno annuali)**:

  * Verifica che per ogni organizzazione esista una cartella-organizzazione correttamente nominata.
  * Verifica della presenza di tutte le macro-cartelle standard.

* **Checklist di creazione organizzazione**:

  * Ogni nuova organizzazione non è considerata “attiva” finché non sono create cartella-organizzazione e macro-cartelle.

* **Allineamento con SOP-DOC-01**:

  * Ogni revisione importante di SOP-DOC-01 o di SOP-ORG-01 comporta una verifica di coerenza con la struttura root Drive.

### 7.3 KPI / Indicatori (se applicabili)

Esempi:

* **% organizzazioni con struttura di macro-cartelle completa e conforme** (target ≥ 95%).
* **Numero di cartelle di primo livello non conformi** rilevate per audit.
* **Numero di segnalazioni interne** relative a difficoltà nel reperimento documenti dovute a struttura non conforme.

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
* modifiche a SOP-ORG-01, SOP-DOC-01 o SOP-DOC-02 che impattino la struttura root.

Ogni revisione comporta:

* aggiornamento della versione e della data di emissione;
* aggiornamento della sezione 10 – Storico revisioni;
* eventuale comunicazione interna.

### 8.3 Obbligatorietà e formazione

* Il **Responsabile IT / CTO** e il **Responsabile Qualità / Documentazione** devono conoscere e applicare il presente SOP per qualsiasi intervento sulla root del Drive.
* I **Responsabili di area** devono conoscere almeno:

  * collocazione della propria macro-cartella;
  * regole di base per non alterare la struttura root.
* Il personale deve essere informato che:

  * le cartelle di primo livello si creano **solo** per nuove organizzazioni e **solo** secondo questo SOP;
  * per qualsiasi nuova esigenza di macro-cartella si deve passare tramite Responsabile Qualità / IT.

---

## 9. Allegati (opzionale)

Possibili allegati:

* **Allegato 1 – Esempio grafico di struttura root multi-organizzazione**
* **Allegato 2 – Checklist per la creazione di una nuova organizzazione in Drive**

Gli allegati, se ufficiali, hanno fonte di verità nel repository GitHub documentazione e possono essere pubblicati su GitHub Pages.

---

## 10. Storico revisioni

| Versione | Data         | Descrizione modifica           | Redatto da                   | Verificato da  | Approvato da  |
| -------- | ------------ | ------------------------------ | ---------------------------- | -------------- | ------------- |
| 1.0      | *[da comp.]* | Prima emissione del SOP-DOC-03 | *[Responsabile Qualità/Doc]* | *[Ruolo/Nome]* | *[Direzione]* |