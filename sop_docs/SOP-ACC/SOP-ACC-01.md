# SOP-ACC-01 – Gestione contabile e tesoreria su Odoo

---

### 0. Metadati del documento

* **Codice SOP:** SOP-ACC-01
* **Titolo:** Gestione contabile e tesoreria su Odoo
* **Versione:** 1.0
* **Data di emissione:** *[da compilare]*
* **Redatto da:** *[Responsabile Operazioni / Amministrazione interna]*
* **Verificato da (se applicabile):** *[Responsabile Qualità / Direzione]*
* **Approvato da:** *[Direzione]*
* **Revisione successiva prevista:** *[da compilare]*
* **Stato:** Bozza
* **Distribuzione:** Interna

---

## 1. Scopo e campo di applicazione

### Scopo

Il presente SOP disciplina come utilizzare **Odoo (moduli Contabilità/Fatturazione)** per:

* importare e registrare **fatture attive e passive** (prevalentemente tramite **XML FatturaPA**) emesse/ricevute e gestite formalmente dal **Commercialista**;
* mantenere aggiornati **scadenzari**, **pagamenti/incassi** e **riconciliazione bancaria** a fini gestionali;
* garantire la tracciabilità e la consultabilità dei documenti (XML/PDF) e la loro associazione a **clienti/fornitori** e **progetti** (contabilità analitica);
* produrre controlli periodici di coerenza (IVA, completezza documentale, partite aperte) a supporto del coordinamento con il Commercialista.

### Campo di applicazione

Si applica a:

* **Amministrazione/Operations interna**: import documenti, tracciamento pagamenti, riconciliazione, controlli periodici.
* **Commerciale / Project Management**: corretta associazione di ricavi/costi ai progetti e supporto a incassi/solleciti.
* **Direzione**: supervisione e approvazione regole, priorità di tesoreria, controlli.
* **Commercialista esterno**: fonte di verità fiscale/civilistica e referente per allineamento periodico (non esegue attività operative su Odoo, salvo accordi).

### Esclusioni / limiti

* Questo SOP **non** sostituisce la contabilità ufficiale tenuta dal Commercialista (registri IVA, adempimenti, dichiarazioni, bilancio civilistico/fiscale).
* Gestione **cespiti, ammortamenti, scritture di assestamento** e adempimenti fiscali sono in capo al Commercialista; su Odoo possono essere riportati **solo in forma gestionale/sintetica** se deciso (vedi §5.2.8).

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabili)

* Obbligo di **fatturazione elettronica** (FatturaPA XML) e trasmissione tramite **SDI** – normativa vigente.
* Obblighi IVA e tenuta registri – normativa vigente.

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

* **SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)**
* **SOP-DOC-03 – Struttura generale Google Drive multi-organizzazione** (se adottato)
* **SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo** (quando la marginalità progetto è parte del controllo)
* **SOP-CRM-01 – Lead generation e gestione opportunità su Odoo** (relazione cliente → opportunità → progetto → fatturazione)

---

## 3. Definizioni, acronimi e abbreviazioni

* **SDI** – Sistema di Interscambio (Agenzia delle Entrate) per la fatturazione elettronica.
* **FatturaPA / XML** – formato XML della fattura elettronica italiana.
* **Fattura attiva** – fattura emessa al cliente.
* **Fattura passiva / Bill** – fattura fornitore ricevuta.
* **Posted (Pubblicata)** – stato Odoo “convalidato”, che produce scritture contabili e alimenta report/scadenzari.
* **Riconciliazione bancaria** – abbinamento righe banca ↔ fatture/pagamenti/scritture.
* **Outstanding Payments/Receipts** – conti transitori per pagamenti registrati prima dell’arrivo dell’estratto conto.
* **Contabilità analitica / Analytic** – tracciamento per centro di costo/progetto tramite distribuzione analitica sulle righe contabili.
* **Project Profitability** – dashboard di marginalità del progetto (ricavi/costi/ore).

---

## 4. Contesto organizzativo e ruoli

### 4.1 Contesto organizzativo / Area di applicazione

Nel nostro modello operativo:

* **il Commercialista** gestisce emissione/ricezione fatture elettroniche e contabilità ufficiale;
* **l’azienda** mantiene in Odoo una contabilità gestionale aggiornata tramite importazione XML e riconciliazione pagamenti, con particolare attenzione alla **tracciabilità per progetto**.

### 4.2 Ruoli e responsabilità (RACI di alto livello)

* **Referente Amministrazione/Operations (interno)**
  * **R:** import XML (attive/passive), pubblicazione documenti, allegati, riconciliazione bancaria, controlli mensili.
  * **A:** correttezza e completezza del dato gestionale su Odoo.
  * **C/I:** collabora con PM e Sales per associazione a progetti e per solleciti incassi.

* **Commercialista (esterno)**
  * **A:** contabilità ufficiale, adempimenti (SDI, IVA, bilancio, cespiti, ecc.).
  * **C:** allineamento periodico (elenchi fatture, IVA, partite aperte), gestione eccezioni.

* **Sales / Account**
  * **R:** fornisce input per fatturazione (quando richiesto), supporta recupero info cliente, verifica coerenza “cosa è stato fatturato”.
  * **C:** solleciti e gestione incassi con il cliente.

* **Project Manager / Delivery**
  * **R (perimetro progetto):** attribuzione corretta a progetto (analitica), verifica marginalità e coerenza ricavi/costi.
  * **C:** supporto su eccezioni (note di credito, split tra progetti, costi promiscui).

* **Direzione**
  * **A:** policy, priorità di tesoreria, approvazione eccezioni significative e impostazione controlli/KPI.

---

## 5. Descrizione del processo

### 5.1 Descrizione sintetica

**Trigger principali:**
* emissione fatture (da Commercialista),
* ricezione fatture fornitori,
* movimenti bancari (incassi/pagamenti),
* chiusure mensili/trimestrali (IVA / allineamenti).

**Output principali:**
* fatture/bills registrate in Odoo con **XML/PDF allegati**,
* pagamenti e riconciliazioni aggiornate,
* report: scadenzari, partite aperte, cash/bank, marginalità progetti (se applicabile),
* evidenze di allineamento con Commercialista.

### 5.2 Flusso operativo di alto livello

1. **Setup iniziale e prerequisiti (una tantum)**
   * Abilitare moduli necessari (Contabilità, Fatturazione, eventualmente Documenti, Progetti, Vendite, Timesheet).
   * Attivare **Contabilità Analitica** se si traccia per progetto.
   * Configurare registri (journal) di Banca/Cassa e, se applicabile, sincronizzazione bancaria o import estratti conto.
   * Definire canale di scambio con Commercialista (cartella condivisa per XML, regole naming).
   * Dettagli operativi: vedi Allegati A01, A03, A05.

2. **Gestione anagrafiche (continuativa)**
   * Mantenere **Partner** (clienti/fornitori) coerenti con P.IVA/CF e dati fiscali (PEC/Codice SDI se presenti), evitando duplicazioni in import XML.
   * Per progetti: assicurare che il progetto abbia un **conto analitico** e che le dashboard di marginalità siano abilitate (se utilizzate).
   * Dettagli operativi: vedi Allegati A03, A04.

3. **Import e registrazione fatture attive (clienti)**
   * Recuperare l’**XML ufficiale** dal Commercialista (o cassetto fiscale) e importarlo in Odoo (singolo o batch ZIP).
   * Verificare: partner, imponibili/IVA, totale, date, termini di pagamento.
* Allineare il **numero fattura** in Odoo al numero ufficiale (sequenza dedicata o modifica numero prima della pubblicazione, se previsto dai permessi/configurazione).
   * Completare i campi gestionali necessari (progetto/analitica, tag, collegamento a ordine/commessa se presente).
   * Allegare XML/PDF (se non già presenti) al record fattura.
   * Pubblicare (Posted) per alimentare scadenzari/report.
   * Dettagli operativi: vedi Allegato A01.

4. **Import e registrazione fatture passive (fornitori)**
   * Importare XML fatture fornitori (batch consigliato); se fatture non elettroniche (PDF/estero), valutare OCR o inserimento manuale.
   * Verificare: fornitore, conti/IVA, date, scadenze.
   * Attribuire **Analytic Distribution** alle righe di costo quando il costo è di progetto o di centro di costo.
   * Pubblicare (Posted) e allegare giustificativi (XML/PDF/scontrino).
   * Dettagli operativi: vedi Allegati A01, A02.

5. **Associazione ricavi/costi ai progetti (contabilità analitica)**
   * Regola: ogni ricavo/costo “di progetto” deve avere distribuzione analitica coerente (100% progetto o split).
   * Casi tipici:
     * ricavi: fatture cliente importate → righe con analitica sul progetto;
     * costi: bills fornitore, spese, note spese → righe con analitica sul progetto.
   * Verifica: controllo su **Project Profitability** (o report analitici) che la fattura compaia sul progetto.
   * Dettagli operativi: vedi Allegati A03, A04.

6. **Registrazione pagamenti e riconciliazione bancaria**
   * Metodo preferito: import/sincronizzare estratto conto e riconciliare le righe banca con fatture aperte.
   * In alternativa: registrare pagamento sulla fattura (outstanding) e poi riconciliare con la transazione bancaria.
   * Gestire: pagamenti parziali, commissioni bancarie, pagamenti cumulativi, storni/annulli.
   * Dettagli operativi: vedi Allegati A05, A02.

7. **Monitoraggio scadenzari e azioni di tesoreria**
   * Settimanale: analisi fatture clienti scadute/prossime alla scadenza, pianificazione incassi; analisi fatture fornitori in scadenza, pianificazione pagamenti.
   * Produzione di report per Direzione/PM (se necessario) e condivisione con Commercialista in caso di divergenze.
   * Dettagli operativi: vedi Allegato A06.

8. **Chiusure periodiche e allineamento con Commercialista**
   * Mensile/trimestrale: confronto IVA vendite/acquisti (Odoo vs liquidazione Commercialista) e completezza fatture.
   * Allineamento partite aperte (Aging receivable/payable) e pagamenti.
   * Annuale: ricezione riepilogo assestamenti/cespiti; decisione se riportare su Odoo in modo sintetico per reportistica interna.
* A fine periodo, valutare l’uso delle **date di blocco** per impedire modifiche retroattive sui periodi chiusi (con regole diverse per utenti interni vs consulenti, se applicabile).
   * Dettagli operativi: vedi Allegato A06 e Template A07.

### 5.3 Istruzioni operative / Dettaglio per fasi

Per mantenere il SOP “alto livello”, tutte le istruzioni step-by-step sono nei seguenti allegati:

* Import XML e gestione scenari (con Commercialista): **Allegato A01**
* Casi contabili (spese senza fattura, note di credito, cespiti, ratei/risconti, ecc.): **Allegato A02**
* Fatturazione ↔ Progetti / Timesheet / Milestone: **Allegato A03**
* Collegamento fatture a progetti esistenti (analitica, regole d’oro): **Allegato A04**
* Riconciliazione bancaria e abbinamento fatture ↔ transazioni: **Allegato A05**
* Checklist e controlli periodici: **Allegato A06** (+ template registro: **A07**)

---

## 6. Strumenti e sistemi utilizzati

* **Odoo 18/19**
  * Moduli: Contabilità/Accounting, Fatturazione/Invoicing, (opz.) Documenti, Progetti, Vendite, Timesheet, Note spese.
  * Funzioni chiave: import XML, pubblicazione documenti, scadenzari, riconciliazione bancaria, contabilità analitica, report.
* **Home Banking / PSD2 / Estratti conto**
  * Fonte delle transazioni bancarie (sincronizzazione o import).
* **Google Drive (o storage equivalente)**
  * Cartella condivisa con Commercialista per deposito XML/PDF e per archiviazione evidenze (in coerenza con SOP-DOC).
* **Commercialista (sistema esterno)**
  * Emissione/registrazione ufficiale e adempimenti fiscali.

---

## 7. Rischi, controlli e indicatori di prestazione

### 7.1 Rischi principali del processo

* **Dati incompleti su Odoo** (fatture non importate o non pubblicate) → report interni fuorvianti, scadenzari errati.
* **Associazione errata ai progetti** (assenza/errore analitica) → marginalità progetto falsata.
* **Riconciliazione bancaria incompleta** → pagamenti duplicati o fatture che risultano aperte erroneamente.
* **Disallineamento con Commercialista** (IVA/partite aperte) → perdita di controllo e rischio di decisioni basate su dati non coerenti.

### 7.2 Controlli e misure di mitigazione

* **Controllo completezza mensile**: elenco fatture Commercialista vs Odoo (A06/A07).
* **Controllo IVA**: confronto IVA vendite/acquisti (A06/A07).
* **Controllo scadenzario**: revisione settimanale partite aperte + follow-up (A06).
* **Controllo progetti**: verifica a campione su progetti attivi che ricavi/costi compaiano su profitability (A03/A04).
* **Controllo riconciliazione**: saldo banca Odoo vs saldo banca reale (A05).

### 7.3 KPI / Indicatori (se applicabili)

* % fatture importate entro X giorni dalla data documento (target: definire).
* % transazioni bancarie riconciliate entro X giorni (target: definire).
* Scaduto clienti (valore e numero fatture scadute).
* Marginalità progetto (se adottata) e variazioni mese su mese.

---

## 8. Gestione, revisione e pubblicazione del SOP

### 8.1 Archiviazione e pubblicazione

* Il SOP è archiviato nel **SOP repository** e pubblicato su GitHub Pages (se adottato), con allegati nella cartella dedicata.
* Gli XML/PDF operativi e le evidenze di confronto con Commercialista sono archiviati su Drive secondo SOP-DOC.

### 8.2 Revisione e aggiornamento

* Aggiornare il SOP quando cambia:
  * versione Odoo o moduli utilizzati,
  * modalità di scambio con Commercialista,
  * struttura contabile/analitica o report richiesti.
* Le modifiche devono essere proposte dal Referente Amministrazione/Operations e approvate dalla Direzione.

### 8.3 Obbligatorietà e formazione

* Obbligatorio per chi opera su Odoo in area contabile/tesoreria e per i ruoli che attribuiscono costi/ricavi ai progetti.
* Formazione minima: import XML, stato Posted, contabilità analitica, riconciliazione bancaria (vedi Allegati).

---

## 9. Allegati

### Guide operative (fornite)

* **Allegato A01** – Gestione contabilità, pagamenti e fatture in Odoo (guida scenari; include scenario Commercialista + import XML)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A01_Gestione_contabilita_pagamenti_fatture_Odoo_Guida_scenari.docx`
* **Allegato A02** – Gestione di casi contabili in Odoo 18 (spese senza fattura, note di credito, cespiti, ratei/risconti, ecc.)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A02_Gestione_casi_contabili_Odoo18.docx`
* **Allegato A03** – Associare la fatturazione ai progetti in Odoo 18/19 (timesheet, milestone, costi/ricavi)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A03_Associare_fatturazione_ai_progetti_Odoo18_19.docx`
* **Allegato A04** – Collegare le fatture a un progetto esistente (regole d’oro + verifica in marginalità progetto)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A04_Collegare_fatture_a_progetto_esistente_Odoo18.docx`
* **Allegato A05** – Associare fatture a transazioni bancarie (riconciliazione, metodi e best practice)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A05_Associare_fatture_a_transazioni_bancarie_Odoo18.docx`
* **Allegato A06** – Checklist operativa e controlli periodici (settimanale/mensile/annuale + modello comunicazione)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A06_Checklist_operativa_e_controlli.md`
* **Allegato A07** – Template registri (import XML, allineamento IVA, pagamenti-progetti)  
  `./SOP-ACC-01_attachments/Allegato_SOP-ACC-01-A07_Template_registri_import_allineamento_pagamenti.xlsx`

---

## 10. Storico revisioni

| Versione | Data      | Descrizione modifica | Redatto da | Verificato da | Approvato da |
|----------|-----------|----------------------|------------|---------------|--------------|
| 1.0      | 2026-02-07| Prima emissione (Bozza) | *[da compilare]* | *[da compilare]* | *[da compilare]* |

