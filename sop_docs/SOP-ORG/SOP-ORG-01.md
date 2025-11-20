# SOP-ORG-01 – STRUTTURA ORGANIZZATIVA E SISTEMA INFORMATIVO AZIENDALE

---

### 0. Metadati del documento

- **Codice SOP:** SOP-ORG-01
- **Titolo:** Struttura organizzativa e sistema informativo aziendale
- **Versione:** 1.0
- **Data di emissione:** *[da compilare]*
- **Redatto da:** *[Ruolo/Funzionale]*
- **Verificato da (se applicabile):** *[Ruolo/Funzionale]*
- **Approvato da:** *[Direzione]*
- **Revisione successiva prevista:** *[da compilare]*
- **Stato:** Bozza
- **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

Il presente SOP ha lo scopo di descrivere:

- la **struttura organizzativa generale** dell’azienda in quanto software house;
- il **modello operativo di riferimento**, basato sull’utilizzo integrato del gestionale **Odoo** e degli altri strumenti aziendali;
- l’insieme dei **rimandi formali** ai SOP specifici di processo (gestione progetti, sviluppo software, lead generation, contabilità, documentazione, comunicazione, knowledge management, ecc.).

**Campo di applicazione**

Il SOP si applica a **tutto il personale** aziendale, interno ed esterno (collaboratori, consulenti) che interagisce, anche solo in parte, con:

- Odoo (CRM, Progetti, Documenti, Contabilità, Knowledge Base);
- Google Drive;
- GitLab;
- GitHub e GitHub Pages;
- altri sistemi esplicitamente richiamati nei SOP di dettaglio.

Sono esclusi da questo documento i dettagli operativi dei singoli processi, che sono disciplinati nei rispettivi SOP dedicati.

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabili)

*Da compilare qualora vengano identificati riferimenti normativi, regolamentari o standard (es. ISO 9001, GDPR, norme di settore) rilevanti per la struttura organizzativa o per la gestione del sistema informativo.*

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

I seguenti documenti interni sono direttamente collegati al presente SOP:

- **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo**
- **SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo**
- **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
- **SOP-ACC-01 – Gestione contabile e tesoreria su Odoo**
- **SOP-KB-01 – Knowledge Base Odoo e collegamento alla documentazione esterna**
- **SOP-MKT-01 – Immagine, comunicazione e gestione dei canali marketing**
- **SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo**
- **SOP-DEV-02 – Gestione repository pubblici e rilascio pacchetti su GitHub**
- **SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages**

---

## 3. Definizioni, acronimi e abbreviazioni

- **SOP (Standard Operating Procedure)** – Procedura Operativa Standard, documento che descrive in modo strutturato come svolgere un processo/attività.
- **Odoo** – Gestionale ERP utilizzato come sistema centrale per CRM, progetti, contabilità, documenti, knowledge base.
- **CRM (Customer Relationship Management)** – Modulo/funzione per la gestione di lead, opportunità commerciali e relazioni con i clienti.
- **Knowledge Base (KB)** – Base di conoscenza centralizzata, costituita da articoli, guide e riferimenti a documentazione interna/esterna.
- **GitLab** – Piattaforma per gestione repository Git, sviluppo collaborativo del codice, issue tracking e CI/CD.
- **GitHub** – Piattaforma per repository Git, utilizzata in particolare per la pubblicazione di pacchetti e codice verso l’esterno.
- **GitHub Pages** – Servizio di hosting di siti statici utilizzato per pubblicare la documentazione aziendale e l’archivio dei SOP.
- **Lead** – Contatto potenzialmente interessato ai prodotti/servizi aziendali, da qualificare nel processo commerciale.
- **Scrum multi-progetto** – Adattamento interno della metodologia Scrum per la gestione contemporanea di più progetti e backlog.

*Ulteriori definizioni specifiche possono essere aggiunte in funzione dell’evoluzione dell’organizzazione e dei sistemi.*

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

L’azienda è una **software house** che sviluppa:

- soluzioni software custom;
- servizi digitali;
- prodotti tecnologici.

L’operatività è strutturata in ottica **multi-progetto** e orientata a metodologie **agili** (Scrum).  
Il presente SOP riguarda in modo trasversale tutte le aree aziendali, con particolare riferimento a:

- Direzione / Management;
- Area Commerciale & Marketing;
- Area Progetti & Delivery;
- Area Sviluppo Software;
- Area Amministrazione & Contabilità;
- Area Documentazione & Knowledge Management.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

Legenda: **R = Responsible**, **A = Accountable**, **C = Consulted**, **I = Informed**

- **Direzione**
  - A: definizione della strategia aziendale e delle priorità progettuali.
  - A: approvazione dei principali SOP (in particolare SOP-ORG-01, SOP-ACC-01, SOP-PRJ-01, ecc.).
  - C/I: informata sull’evoluzione del sistema informativo e sui principali cambiamenti organizzativi.

- **Responsabile Qualità / Documentazione** (se previsto)
  - R: mantenimento e aggiornamento del presente SOP e della struttura complessiva dei SOP.
  - R: coerenza tra documenti pubblicati su GitHub Pages, KB Odoo e riferimenti nei vari moduli.
  - C: consultato in caso di introduzione di nuovi strumenti o modifiche organizzative rilevanti.

- **Responsabile IT / CTO**
  - A: architettura complessiva degli strumenti (Odoo, GitLab, GitHub, Google Drive).
  - R: configurazioni tecniche critiche, policy di sicurezza e integrazioni tra sistemi.
  - C/I: consultato per la definizione e revisione dei SOP tecnici (SOP-DEV, SOP-DOC, ecc.).

- **Project Manager / Product Owner**
  - R: gestione dei progetti in Odoo (backlog, sprint, task) secondo SOP-PRJ-01.
  - R: allineamento tra storie Odoo e ticket GitLab, in collaborazione con i team di sviluppo.
  - C: coordinamento con Area Commerciale & Marketing per la corretta traduzione dei requisiti.

- **Sviluppatori**
  - R: utilizzo corretto di GitLab per sviluppo collaborativo e integrazione con le user story Odoo (SOP-DEV-01).
  - R: collaborazione nelle attività di pubblicazione su GitHub (SOP-DEV-02).
  - C/I: aggiornamento dello stato delle attività in Odoo in coerenza con l’avanzamento del codice.

- **Amministrazione**
  - R: gestione di contabilità e amministrazione tramite Odoo (SOP-ACC-01).
  - C: supporto alla Direzione per report economico-finanziari e controllo di gestione.
  - I: informata su cambiamenti che impattano su flussi contabili.

- **Marketing & Sales**
  - R: gestione lead e opportunità in Odoo CRM (SOP-CRM-01).
  - R: mantenimento dei materiali di comunicazione e immagine aziendale (SOP-MKT-01).
  - C/I: coordinamento con Progetti & Delivery per allineamento tra offerta commerciale e capacità operativa.

La declinazione completa delle responsabilità per ogni singolo processo è riportata nei rispettivi SOP dedicati.

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

Il presente SOP non descrive un singolo processo operativo “lineare”, ma definisce il **modello di riferimento** per:

- come è strutturata l’azienda dal punto di vista organizzativo;
- come viene configurato e utilizzato il **sistema informativo integrato** (Odoo, Google Drive, GitLab, GitHub, GitHub Pages);
- come vengono collegati tra loro i SOP di dettaglio relativi ai vari processi aziendali.

### 5.2 Flusso operativo di alto livello

In ottica di gestione e miglioramento continuo dell’assetto organizzativo e del sistema informativo, possono essere individuate le seguenti macro-fasi:

1. **Definizione e aggiornamento del modello organizzativo**
   - La Direzione definisce o aggiorna le aree funzionali, i ruoli chiave e le responsabilità.
   - Le modifiche sono recepite nel presente SOP e, se necessario, nei SOP di area.

2. **Definizione e aggiornamento dell’architettura degli strumenti**
   - Il Responsabile IT / CTO definisce come Odoo, Google Drive, GitLab, GitHub e GitHub Pages interagiscono tra loro.
   - Vengono definiti i collegamenti standard (es. link Drive nei Documenti Odoo, issue GitLab collegate alle user story, link a GitHub Pages nella KB Odoo).

3. **Utilizzo operativo dei sistemi secondo i SOP di dettaglio**
   - Le aree funzionali utilizzano i sistemi seguendo i rispettivi SOP (CRM, Progetti, DEV, Contabilità, Documentazione, ecc.).
   - Il presente SOP funge da “documento di cornice” per garantire coerenza tra i diversi processi.

4. **Manutenzione della documentazione e del sistema informativo**
   - Il Responsabile Qualità / Documentazione e il Responsabile IT / CTO curano l’aggiornamento del presente SOP e dei SOP correlati.
   - Eventuali criticità o non conformità rilevate nei processi portano a revisioni dell’assetto organizzativo o dei flussi tra sistemi.

### 5.3 Istruzioni operative / Dettaglio per fasi

*Il dettaglio operativo delle singole attività (es. come aprire un progetto in Odoo, come creare un repository GitLab, come configurare un collegamento a GitHub Pages) è descritto nei rispettivi SOP tecnici e di processo (SOP-PRJ-01, SOP-DEV-01, SOP-DOC-01, SOP-DOC-02, ecc.).*

---

## 6. Strumenti e sistemi utilizzati

### 6.1 Odoo – Gestionale centrale

Odoo rappresenta il **gestionale centrale** e il principale “punto di verità” per:

- anagrafiche di contatti, clienti e fornitori;
- progetti e attività operative;
- documenti collegati a processi e commesse;
- contabilità e movimenti economico-finanziari;
- knowledge base e riferimenti a SOP e documentazione esterna.

**Rimandi a SOP specifici:**

- **SOP-CRM-01** per gestione lead e opportunità su Odoo;
- **SOP-PRJ-01** per gestione progetti e metodologia Scrum multi-progetto;
- **SOP-DOC-01** per gestione documentale integrata con Google Drive;
- **SOP-ACC-01** per contabilità e tesoreria;
- **SOP-KB-01** per la Knowledge Base Odoo.

### 6.2 Google Drive – Archiviazione e condivisione file

- Utilizzato come sistema principale di **archiviazione e condivisione dei file** (documenti operativi, bozze, materiali di progetto, presentazioni, ecc.).
- Le cartelle di Drive sono collegate a Odoo tramite link inseriti nella sezione **Documenti** e/o negli articoli di KB.
- La struttura delle cartelle, i permessi di accesso e le naming convention sono definiti in **SOP-DOC-01**.

### 6.3 GitLab – Sviluppo collaborativo del codice

- Strumento principale per lo **sviluppo collaborativo del codice**.
- Per i progetti di sviluppo, le **issue GitLab** sono collegate alle **storie e task Odoo**, garantendo:
  - tracciabilità requisito → attività → codice;
  - allineamento tra pianificazione (Scrum) e delivery tecnica.
- Branching model, merge request, code review, CI/CD, convenzioni di naming e policy di gestione degli accessi sono definite in **SOP-DEV-01**.

### 6.4 GitHub – Pubblicazione pacchetti e codice

- Utilizzato per la **pubblicazione di pacchetti e/o codice** (open source, librerie condivise, componenti destinati all’esterno).
- La distinzione tra repository interni (GitLab) ed esterni (GitHub) è definita in **SOP-DEV-02**.
- In tale SOP sono disciplinati:
  - criteri di selezione dei repository da rendere pubblici;
  - gestione versioni e release;
  - licenze, README, documentazione tecnica associata.

### 6.5 GitHub Pages e documentazione aziendale

- Tutti i **SOP** e la documentazione aziendale di riferimento (manuali, linee guida, standard interni) sono raccolti e resi **visionabili/condivisibili** tramite **GitHub Pages** o piattaforme analoghe.
- I link alle pagine di documentazione sono:
  - inseriti nella **Knowledge Base Odoo** (SOP-KB-01);
  - referenziati, dove opportuno, nei record di progetto, nelle anagrafiche, nei documenti Odoo.
- Struttura del sito documentale e modalità di aggiornamento sono descritte in **SOP-DOC-02**.

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali del processo

Esempi di rischi associati alla struttura organizzativa e al sistema informativo:

- **Rischio di incoerenza tra sistemi**  
  (es. dati progetto diversi tra Odoo e GitLab, documenti non allineati tra Drive e Odoo Documenti).
- **Rischio di mancata tracciabilità**  
  (es. attività di sviluppo non collegate a storie Odoo, SOP non aggiornati o non collegati alla KB).
- **Rischio di utilizzo non uniforme degli strumenti**  
  (es. team che usano strumenti diversi o modalità non conformi ai SOP di dettaglio).

### 7.2 Controlli e misure di mitigazione

- Verifiche periodiche sulla corretta presenza dei collegamenti standard:
  - Odoo ↔ GitLab (storie/ticket);
  - Odoo Documenti ↔ Google Drive;
  - Odoo KB ↔ GitHub Pages.
- Revisione periodica dei SOP di dettaglio per garantire coerenza con l’evoluzione organizzativa e tecnologica.
- Eventuali audit interni sui progetti per verificare l’aderenza alla metodologia Scrum multi-progetto e all’uso dei sistemi.

### 7.3 KPI / Indicatori (se applicabili)

*Da definire in funzione delle esigenze di monitoraggio (es. % progetti con collegamenti completi Odoo–GitLab, % SOP aggiornati negli ultimi 12 mesi, ecc.).*

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

- Il presente SOP è archiviato e pubblicato su **GitHub Pages** all’interno del sito documentale aziendale.
- Un link diretto a questo documento è presente:
  - nella **Knowledge Base Odoo** (categoria “SOP – Organizzazione”);
  - ove rilevante, in eventuali moduli Odoo (es. Documenti aziendali generali).
- La versione accessibile agli utenti deve sempre corrispondere all’ultima versione **approvata**.

### 8.2 Revisione e aggiornamento

La revisione del presente SOP è attivata:

- in caso di modifiche organizzative rilevanti (es. creazione/eliminazione di aree funzionali);
- in caso di cambiamenti significativi negli strumenti (migrazioni di sistema, nuovi moduli Odoo, sostituzione di piattaforme, ecc.);
- a seguito di non conformità, audit interni o segnalazioni del personale;
- su richiesta della Direzione o del Responsabile Qualità / Documentazione.

Ogni revisione comporta:

- aggiornamento del numero di versione;
- aggiornamento della data di emissione;
- registrazione della modifica nella **sezione 10 – Storico revisioni**.

### 8.3 Obbligatorietà e formazione

- Tutto il personale interessato è tenuto a:
  - conoscere il presente SOP per quanto di pertinenza del proprio ruolo;
  - attenersi ai SOP di dettaglio richiamati.
- In caso di modifiche significative:
  - possono essere pianificate attività di **formazione** o comunicazione interna;
  - può essere richiesta la **presa visione** formale del documento aggiornato tramite i canali aziendali (es. KB Odoo, comunicazioni interne).

---

## 9. Allegati

*Al momento non sono previsti allegati specifici al presente SOP. Eventuali diagrammi di flusso, matrici RACI dettagliate o template operativi potranno essere aggiunti in futuro come Allegati 1, 2, ecc.*

---

## 10. Storico revisioni

| Versione | Data       | Descrizione modifica                   | Redatto da           | Verificato da        | Approvato da        |
|----------|------------|----------------------------------------|----------------------|----------------------|---------------------|
| 1.0      | *[da comp.]* | Prima emissione del SOP-ORG-01        | *[Ruolo/Nome]*       | *[Ruolo/Nome]*       | *[Direzione]*       |
