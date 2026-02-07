# SOP-CRM-01 – LEAD GENERATION E GESTIONE OPPORTUNITÀ SU ODOO

---

### 0. Metadati del documento

- **Codice SOP:** SOP-CRM-01  
- **Titolo:** Lead generation e gestione opportunità su Odoo  
- **Versione:** 0.1  
- **Data di emissione:** 2026-02-07  
- **Redatto da:** Responsabile Commerciale / CRM Manager  
- **Verificato da (se applicabile):** PMO / Quality  
- **Approvato da:** Direzione  
- **Revisione successiva prevista:** 2026-08-07  
- **Stato:** Bozza  
- **Distribuzione:** Interna  

---

## 1. Scopo e campo di applicazione

Il presente SOP disciplina il processo **CRM (Customer Relationship Management)** in Odoo, dalla **generazione/acquisizione dei lead** fino alla **chiusura delle opportunità** e all’**analisi delle performance**, garantendo:

- tracciabilità end-to-end (dati, attività, comunicazioni, decisioni);
- coerenza operativa tra marketing, vendite, delivery e amministrazione;
- qualità del dato e conformità normativa (in particolare GDPR);
- affidabilità della pipeline e delle previsioni (forecast).

**Campo di applicazione**

Questo SOP si applica a:
- personale commerciale (inside/outside sales), pre-sales e direzione vendite;
- marketing (per i canali di acquisizione e il nurturing);
- amministrazione (per la formalizzazione ordine/fatturazione quando applicabile);
- delivery / project management (handover del cliente/opportunità vinta);
- amministratore Odoo / IT (configurazioni, integrazioni, sicurezza, governance).

---

## 2. Riferimenti normativi e documentali

### 2.1 Riferimenti normativi (se applicabili)

- **Regolamento (UE) 2016/679 (GDPR)** – principi di liceità, minimizzazione, conservazione, diritti dell’interessato.

### 2.2 Riferimenti interni (policy, procedure, altri SOP)

- **SOP-MKT-01** – Immagine, comunicazione e gestione dei canali marketing
- **SOP-PRJ-01** – Gestione progetti e metodologia Scrum multi-progetto su Odoo
- **SOP-ACC-01** – Gestione contabile e tesoreria su Odoo
- **SOP-DOC-01** – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)
- **SOP-KB-01** – Knowledge Base Odoo e collegamento alla documentazione esterna
- **SOP-DOC-02** – Pubblicazione documentazione e SOP su GitHub Pages

---

## 3. Definizioni, acronimi e abbreviazioni

- **CRM** – insieme di processi e strumenti per gestire relazioni commerciali, lead, opportunità e clienti.
- **Lead** – contatto potenzialmente interessato, non ancora qualificato/convertito in opportunità.
- **Opportunità** – trattativa commerciale attiva associata a un potenziale cliente e a un valore atteso.
- **Pipeline** – vista Kanban delle opportunità, organizzata per fasi del ciclo di vendita.
- **Chatter** – timeline del record (lead/opportunità) in cui vengono registrati messaggi, email, note e log attività.
- **Attività** – task pianificati (chiamata, email, meeting, follow-up) legati al record CRM.
- **Team di vendita** – unità organizzativa/commerciale in Odoo.
- **Addetto vendite (Responsabile)** – owner operativo del lead/opportunità.
- **Opt-Out** – flag di disiscrizione/limitazione comunicazioni commerciali.

---

## 4. Ruoli e responsabilità

- **Direzione / Direttore Vendite**
  - definisce strategia e KPI; approva convenzioni di pipeline e criteri di avanzamento;
  - conduce (o supervisiona) le pipeline review periodiche.
- **Responsabile Commerciale / CRM Manager**
  - owner del processo; garantisce adozione del SOP e qualità dei dati;
  - definisce SLA interni di presa in carico, regole di assegnazione e standard di compilazione campi.
- **Commerciale (Sales Rep / Account / Inside Sales)**
  - gestisce lead/opportunità assegnate: contatto, qualificazione, attività, preventivi, chiusura e aggiornamento continuo.
- **Marketing**
  - genera lead (campagne, sito, eventi), fornisce contesto (source/tag) e supporta nurturing;
  - collabora su materiali e contenuti richiesti dalle opportunità.
- **Amministrazione (se applicabile)**
  - supporta formalizzazione ordine/contratto/fatturazione e aggiornamento dati anagrafici cliente.
- **PM / Delivery**
  - riceve handover delle opportunità vinte e avvia la fase di delivery secondo SOP-PRJ-01.
- **Amministratore Odoo / IT**
  - configura moduli, integrazioni email/calendario, permessi e automazioni; gestisce audit e sicurezza.

---

## 5. Descrizione del processo

### 5.1 Prerequisiti e configurazioni minime

**Prerequisiti applicativi**
- Odoo con app **CRM**; app **Vendite** per preventivi/ordini; app **Calendario** per meeting; opzionali **Email Marketing** / **Marketing Automation** per nurturing e follow-up automatici.
- Configurazione email (SMTP/IMAP) e/o Discuss per centralizzare comunicazioni sul Chatter.
- Configurazione Team di vendita, utenti e permessi.

**Configurazioni di governance (minime)**
- Definizione fasi pipeline e criteri di avanzamento (vedi Allegato A03).
- Definizione convenzioni di naming opportunità e tag (vedi Allegato A03).
- Definizione SLA di presa in carico (es. *entro 1 giorno lavorativo*).
- Definizione motivi di perdita (lost reasons) e obbligatorietà di compilazione in chiusura.
- Regole per gestione duplicati/archiviazioni e richieste GDPR.

> Nota: i passaggi tecnici di configurazione e utilizzo in Odoo sono descritti in dettaglio nell’**Allegato A01**.

---

### 5.2 Acquisizione lead (inbound/outbound)

**Input principali**
- richieste da sito web (form contatto, “richiedi preventivo”);
- importazioni massiva (CSV/Excel);
- inserimento manuale da parte del team;
- integrazioni e canali (email inbound, campagne, eventi, referral, ticket helpdesk per upselling).

**Regole operative**
1. Ogni lead deve essere registrato in Odoo con:
   - titolo descrittivo (standard naming, vedi Allegato A03),
   - contatto e azienda (se disponibili),
   - canale/origine (source) e tag utili,
   - consenso/base giuridica e Opt-Out quando applicabile.
2. Le importazioni devono seguire un modello colonne standard (vedi Allegato A04) e prevedere un controllo qualità post-import.

**Output**
- Lead creato in Odoo, tracciabile e pronto per la fase di triage.

---

### 5.3 Triage e presa in carico

**Obiettivo**: assicurare che nessun lead resti “orfano” e che ci sia un primo contatto tempestivo.

**Attività**
- Assegnazione di **Addetto vendite** e **Team di vendita** (manuale o automatica) secondo regole interne.
- Verifica duplicati:
  - se il lead è duplicato o già in pipeline, gestire unione/archiviazione secondo governance.
- Pianificazione della **prima attività** (chiamata/email/meeting) rispettando SLA.

**Controlli minimi**
- **Nessun lead senza prossima attività pianificata**.
- Monitoraggio periodico dei lead “Non assegnati” e/o senza attività.

**Output**
- Lead preso in carico, con owner e prossimo passo definito.

---

### 5.4 Qualificazione e conversione in opportunità

**Obiettivo**: trasformare lead idonei in opportunità gestibili in pipeline e scartare/archiviare lead non qualificati.

**Criteri di qualificazione (minimi)**
- Interesse e bisogno espliciti, o segnale qualificante (es. richiesta demo/offerta);
- adeguatezza del target (settore, dimensione, localizzazione, fit con offerta);
- disponibilità di interlocutore e contatti minimi.

**Azioni**
- Aggiornamento campi: valore atteso/ricavo previsto (se noto), priorità, contesto e note.
- Conversione del lead in opportunità, con creazione/collegamento del cliente (anagrafica) quando applicabile.
- Pianificazione del follow-up e aggiornamento continuo del Chatter (log chiamate, email, note).

**Output**
- Opportunità creata in pipeline e assegnata al venditore/team.

---

### 5.5 Gestione pipeline e follow-up

**Principi**
- La pipeline deve riflettere lo **stato reale** della trattativa: aggiornamenti **in real time**.
- Ogni opportunità aperta deve avere una **prossima attività**.
- Tutta la comunicazione rilevante deve rimanere nel **Chatter** del record.

**Attività ricorrenti**
- Spostamento opportunità tra fasi secondo i criteri definiti (Allegato A03).
- Registrazione attività completate e pianificazione prossimo passo.
- Coinvolgimento stakeholder interni tramite follower e menzioni (es. marketing o direzione).
- Per opportunità ad alto valore: escalation e revisione con Direzione / Responsabile Commerciale.

**Riunioni di governance**
- **Pipeline review** settimanale/bi-settimanale:
  - pulizia opportunità ferme,
  - verifica coerenza probabilità/ricavi previsti,
  - decisioni su next steps e priorità.

---

### 5.6 Preventivo, trattativa e chiusura (Won/Lost)

**Creazione preventivo**
- Per opportunità qualificate, generare preventivo da Odoo (richiede app Vendite) e mantenerlo collegato all’opportunità.
- Assicurare collegamento corretto del cliente (nuovo/esistente) e aggiornamento dati anagrafici.

**Chiusura opportunità**
- **Vinto (Won)**: appena ricevuta conferma d’ordine/contratto.
  - assicurare documentazione commerciale essenziale (preventivo, ordine, eventuali allegati);
  - avviare handover a delivery/progetti (SOP-PRJ-01).
- **Perso (Lost)**: appena confermata perdita.
  - registrare sempre il **motivo di perdita**;
  - se opportuno, archiviare e pianificare eventuale re-engagement.

**Output**
- Opportunità chiusa correttamente con motivazione e tracciabilità completa.

---

### 5.7 Handover a delivery / amministrazione

Per opportunità **Vinte**:
- consegna informazioni minime a PM/Delivery:
  - scope concordato, requisiti, vincoli, timeline;
  - documenti commerciali e contatti chiave;
  - note operative dal Chatter.
- eventuale apertura progetto/commessa secondo SOP-PRJ-01.
- coordinamento con amministrazione per ordine, fatturazione e gestione anagrafica.

---

### 5.8 Reporting e miglioramento continuo

**Report minimi da mantenere**
- Pipeline per fase/team/venditore (valore e forecast).
- Conversione lead → opportunità → vendite.
- Durata ciclo di vendita e tasso win/loss.
- SLA di presa in carico e opportunità senza attività/ferme.

**Cadenza**
- Report operativo: settimanale.
- Report direzionale: mensile (trend, conversioni, forecast, azioni correttive).

---

## 6. Registrazioni e output attesi (evidenze)

- Record Odoo: lead, opportunità, attività, log nel Chatter, preventivi/ordini.
- Report Odoo (pipeline, KPI, pivot) esportati se necessari.
- Verbali/decisioni pipeline review (se formalizzati).
- Documentazione commerciale allegata ai record (preventivi, presentazioni, contratti).

---

## 7. Controlli, KPI e criteri di qualità

**Controlli minimi**
- Lead presi in carico entro SLA.
- Nessuna opportunità aperta senza prossima attività.
- Pipeline aggiornata (no opportunità ferme senza motivazione).
- Motivo perdita obbligatorio in chiusura Lost.
- Gestione duplicati e rispetto Opt-Out/GDPR.

**KPI suggeriti**
- tempo medio di prima risposta (TTR) su lead inbound;
- tasso di conversione lead→opportunità e opportunità→vinto;
- win rate e valore medio deal;
- durata media ciclo di vendita;
- valore pipeline e forecast ponderato;
- % opportunità senza attività o con attività in ritardo.

---

## 8. Note di conformità (GDPR e data hygiene)

- Raccogliere solo dati necessari e con base giuridica appropriata; rispettare Opt-Out e richieste di cancellazione/anonimizzazione.
- Evitare note con dati sensibili non necessari nel Chatter.
- Eseguire deduplicazione periodica e standardizzare campi/tag per mantenere report affidabili.

---

## 9. Allegati

- **A01** – [Guida completa al processo CRM in Odoo 18 (DOCX)](./SOP-CRM-01_attachments/Allegato_SOP-CRM-01-A01_Guida_completa_al_processo_CRM_in_Odoo_18.docx)  
- **A02** – [Checklist operativa CRM (Lead → Opportunità → Chiusura)](./SOP-CRM-01_attachments/Allegato_SOP-CRM-01-A02_Checklist_operativa_CRM.md)  
- **A03** – [Convenzioni e criteri (naming, tag, fasi pipeline)](./SOP-CRM-01_attachments/Allegato_SOP-CRM-01-A03_Convenzioni_pipeline_tag_naming.md)  
- **A04** – [Template import Lead/Opportunità (CSV)](./SOP-CRM-01_attachments/Allegato_SOP-CRM-01-A04_Template_import_lead_odoo.csv)  

---

## 10. Storico revisioni

| Versione | Data | Modifiche | Autore |
|---|---:|---|---|
| 0.1 | 2026-02-07 | Prima emissione (strutturazione processo CRM + allegati) | Responsabile Commerciale / CRM Manager |

