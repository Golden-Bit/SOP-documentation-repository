# Documento di Progetto – Progetto Esterno (Cliente)

---

## 0. Metadati di progetto

- **Codice progetto:** {{CODICE_PROGETTO}}
- **Titolo progetto:** {{TITOLO_PROGETTO}}
- **Cliente:** {{NOME_CLIENTE}}
- **Tipo progetto:** Esterno (Cliente)
- **Stato progetto:** {{Iniziato / In corso / Chiuso / In attesa}}
- **Project Manager / Product Owner:** {{NOME_PM_PO}}
- **Scrum Master:** {{NOME_SCRUM_MASTER}}
- **Versione documento:** {{VERSIONE_DOC}}
- **Data:** {{DATA}}
- **Confidenzialità:** {{Confidenziale / Uso interno / Condivisibile con cliente}}

> **Esempio di compilazione**  
> - Codice progetto: PRJ-EXT-2025-001  
> - Titolo progetto: Piattaforma Web per Gestione Ordini B2B  
> - Cliente: ACME S.p.A.

---

## 1. Contesto e obiettivi

### 1.1 Contesto

_Descrivere il contesto del cliente, le esigenze principali e il motivo per cui nasce il progetto._

**Esempi di contenuti:**

- Settore del cliente (es. manifatturiero, logistica, retail, ecc.).
- Sistemi già esistenti e loro limiti.
- Problemi riscontrati (es. processi manuali, mancanza di tracciabilità, errori frequenti).
- Eventuali vincoli (normativi, tecnologici, organizzativi).

### 1.2 Obiettivi di alto livello

_Elencare gli obiettivi principali del progetto (es. migliorare, automatizzare, integrare, ridurre tempi/costi, ecc.)._

**Esempi di obiettivi:**

- Ridurre del 30% il tempo medio di gestione di un ordine.
- Centralizzare tutte le richieste cliente in un’unica piattaforma.
- Integrare la soluzione con il gestionale ERP già presente in azienda.
- Migliorare la visibilità dello stato ordine per i referenti commerciali.

---

## 2. Ambito (Scope) del progetto

### 2.1 In scope

_Elencare ciò che è incluso nel perimetro del progetto (funzionalità, processi, moduli, sistemi)._

**Esempi di contenuti:**

- Implementazione modulo Odoo Vendite e CRM.
- Realizzazione portale web B2B per inserimento autonomo ordini da parte del cliente.
- Integrazione con sistema ERP interno tramite API.
- Configurazione reportistica base (report ordini mensili, performance, ecc.).

### 2.2 Out of scope

_Elencare esplicitamente ciò che non rientra nel perimetro._

**Esempi di esclusioni:**

- Sviluppo app mobile nativa.
- Migrazione storica completa di tutti gli ordini degli ultimi 10 anni.
- Localizzazione in lingue diverse da italiano e inglese.
- Integrazioni con sistemi futuri non ancora definiti.

---

## 3. Stakeholder e ruoli

**Cliente**

- **Sponsor cliente:** {{NOME_SPONSOR_CLIENTE}}  
  _Esempio: Direttore Operations._
- **Referente operativo:** {{NOME_REFERENTE_CLIENTE}}  
  _Esempio: Responsabile IT / Key User._

**Interni**

- **Project Manager / Product Owner:** {{NOME_PM_PO}}
- **Scrum Master:** {{NOME_SCRUM_MASTER}}
- **Team di sviluppo:** {{NOMI_RISORSE}}  
  _Esempio: 2 backend dev, 1 frontend dev, 1 devops._
- **Altri stakeholder interni:** {{ELENCO}}  
  _Esempio: referente QA, referente commerciale, amministrazione._

---

## 4. Setup Scrum e modalità di lavoro

### 4.1 Durata e calendario degli Sprint

- **Durata Sprint:** {{Durata Sprint, es. 2 settimane}}
- **Periodo previsto progetto:** {{Data inizio – Data fine (stimate)}}

**Esempio:**

- Durata Sprint: 2 settimane (lun–ven).
- Periodo previsto: 2025-01-15 → 2025-06-30.

### 4.2 Cerimonie Scrum

- **Daily:** {{frequenza e orario, es. ogni giorno lavorativo h 9:30}}  
  _Esempio: Daily online 15 minuti, ogni giorno h 9:30._
- **Sprint Planning:** {{modalità e durata}}  
  _Esempio: 2 ore, all’inizio dello Sprint, con PM, SM, team dev._
- **Sprint Review:** {{modalità e durata}}  
  _Esempio: 1,5 ore con demo al cliente al termine di ogni Sprint._
- **Retrospective:** {{modalità e durata}}  
  _Esempio: 1 ora interna al team, subito dopo la Review._

### 4.3 Modalità di comunicazione

_Descrivere canali e frequenza di comunicazione._

**Esempio di contenuti:**

- Canali ufficiali:  
  - Email per comunicazioni formali e verbali di riunioni.  
  - Videocall (es. Meet/Teams) per cerimonie Scrum e workshop.  
  - Eventuale canale chat condiviso (se concordato con il cliente).
- Report verso il cliente:  
  - Report di avanzamento a fine Sprint (slide o breve documento).  
  - Aggiornamento stato attività su Odoo/GitLab per trasparenza.

---

## 5. Requisiti e backlog di alto livello

_Descrivere brevemente le principali EPIC / macro-user story collegate al progetto._

**Esempi di EPIC:**

- EPIC-01 – Gestione anagrafiche clienti e utenti portale.
- EPIC-02 – Inserimento e tracciamento ordini online.
- EPIC-03 – Integrazione con ERP per sincronizzazione ordini.
- EPIC-04 – Reportistica base per il management.

> I dettagli (Story e Task) sono gestiti nel backlog operativo su **Odoo Progetti** e **GitLab**.

---

## 6. Architettura / Soluzione proposta (se applicabile)

_Descrivere la soluzione tecnica/funzionale ad alto livello._

**Esempi di contenuti:**

- Moduli Odoo utilizzati: CRM, Vendite, Progetti, Documenti, ecc.
- Componenti custom previsti.
- Architettura logica (es. front-end web → API → Odoo).
- Integrazioni con sistemi terzi (es. ERP, sistemi di pagamento, servizi esterni).
- Considerazioni su sicurezza e autenticazione (es. SSO, OAuth, ruoli e permessi).

---

## 7. Piano di lavoro e milestone

### 7.1 Roadmap e milestone principali

_Inserire una vista sintetica delle principali milestone._

**Esempio di tabella:**

| Milestone                        | Data stimata   | Descrizione                                               | Deliverable principale                         |
|----------------------------------|----------------|-----------------------------------------------------------|-----------------------------------------------|
| M1 – Kick-off progetto           | 2025-01-20     | Allineamento iniziale con cliente, definizione dettaglio | Verbale kick-off + piano di comunicazione     |
| M2 – Fine Sprint 1               | 2025-02-07     | Primo incremento funzionale (MVP anagrafiche)            | Demo + note funzionali                        |
| M3 – Fine Sprint 3               | 2025-03-21     | Funzionalità core ordini B2B pronte                      | Versione test in ambiente di pre-produzione   |
| M4 – Go-live                     | 2025-05-30     | Messa in produzione del sistema                          | Sistema in produzione + piano supporto        |
| M5 – Chiusura progetto           | 2025-06-30     | Retro finale + handover                                  | Report finale + documentazione aggiornata     |

### 7.2 Dipendenze critiche

_Elencare le principali dipendenze._

**Esempi:**

- Disponibilità ambiente di test del cliente entro data X.
- Consegna specifiche API ERP da parte del cliente entro data Y.
- Disponibilità referenti chiave per workshop di analisi.

---

## 8. Rischi, assunzioni e mitigazioni

### 8.1 Rischi principali

_Elencare rischi con impatto e probabilità._

**Esempi:**

- Rischio: ritardo nella disponibilità delle API ERP.  
  - Impatto: Alto – blocco integrazione.  
  - Probabilità: Media.
- Rischio: cambi frequenti dei requisiti in corso d’opera.  
  - Impatto: Alto – aumento effort.  
  - Probabilità: Alta.

### 8.2 Assunzioni

**Esempi:**

- Il cliente fornisce referenti disponibili per review a fine Sprint.
- L’ambiente di test del cliente è stabile e accessibile dal team di sviluppo.
- I dati di test forniti sono rappresentativi dei casi reali.

### 8.3 Strategie di mitigazione

**Esempi:**

- Pianificazione di Sprint iniziali orientati a funzionalità non dipendenti dall’ERP.
- Definizione chiara di una baseline di requisiti e processo di gestione change request.
- Meeting periodici di allineamento per ridurre incomprensioni.

---

## 9. Qualità, accettazione e criteri di completamento

_Definire criteri di accettazione e modalità di collaudo._

**Esempi di contenuti:**

- Criteri di accettazione per ogni funzionalità chiave (test di scenario).
- Test congiunti con utenti chiave del cliente (UAT).
- Definizione di eventuali SLA (tempi di risposta, disponibilità, gestione bug critici).
- Condizioni per considerare il progetto “completato” (tutti i requisiti must-have in DONE, bug critici chiusi, documentazione consegnata).

---

## 10. Riferimenti a sistemi, documenti e SOP

- Riferimento progetto Odoo: {{LINK_PROGETTO_ODOO}}
- Repository GitLab (se presente): {{LINK_GITLAB}}
- Repository GitHub (se presente): {{LINK_GITHUB}}
- Cartella Google Drive del progetto: {{LINK_CARTELLA_DRIVE}}
- Documentazione su GitHub Pages: {{LINK_GITHUB_PAGES}}
- Articolo Knowledge Base Odoo (se presente): {{LINK_KB_ODOO}}
- SOP-PRJ-01 – Gestione progetti e metodologia Scrum multi-progetto su Odoo
- SOP-DOC-01 – Modello integrato di gestione documentale (Odoo / Google Drive / GitHub)
- SOP-DOC-02 – Pubblicazione documentazione e SOP su GitHub Pages
- SOP-DEV-01 – Utilizzo di GitLab per lo sviluppo collaborativo

> **Esempio:**  
> - Cartella Drive: `https://drive.google.com/.../Progetti/PRJ-EXT-2025-001`  
> - Documentazione GitHub Pages: `https://azienda.github.io/docs/prj-ext-2025-001`

---

## 11. Allegati

_Elencare gli allegati effettivi e il loro contenuto._

**Esempi di allegati:**

- **Allegato A – Diagramma di architettura logica**  
  Contenuto: schema dei moduli, integrazioni, flussi di dati tra sistemi (Odoo, ERP, portale, ecc.).
- **Allegato B – Mockup interfaccia utente**  
  Contenuto: schermate principali del portale B2B (homepage, elenco ordini, dettaglio ordine, ecc.).
- **Allegato C – Specifica di integrazione con ERP**  
  Contenuto: formati dati, endpoint, protocolli, esempi di payload.
- **Allegato D – Piano di test (UAT)**  
  Contenuto: casi di test, criteri di accettazione, responsabili, esito test.
- **Allegato E – Manuale utente / quick start per il cliente**  
  Contenuto: guida rapida all’utilizzo principale del sistema.

> Indicare per ciascun allegato dove è archiviato (link Drive o GitHub Pages) se non è incorporato direttamente nel documento.
