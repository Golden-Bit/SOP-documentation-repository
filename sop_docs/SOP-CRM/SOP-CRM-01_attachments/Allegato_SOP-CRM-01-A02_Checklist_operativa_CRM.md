# Allegato SOP-CRM-01-A02 – Checklist operativa CRM (Lead → Opportunità → Chiusura)

> Checklist sintetica per l’operatività quotidiana. I dettagli click-by-click sono in **Allegato A01**.

---

## 0) Prerequisiti (una tantum / periodici)

- [ ] App Odoo installate/attive: **CRM**, **Vendite**, **Calendario** (se meeting), opzionali **Email Marketing / Marketing Automation**
- [ ] Posta configurata (SMTP/IMAP) e firma utente impostata
- [ ] Team di vendita e utenti configurati (permessi e appartenenza)
- [ ] Fasi pipeline definite e approvate (vedi Allegato A03)
- [ ] Motivi di perdita configurati e obbligo in chiusura Lost
- [ ] Convenzioni: naming opportunità, tag, priorità (vedi Allegato A03)
- [ ] Standard import CSV definito e testato (vedi Allegato A04)

---

## 1) Acquisizione lead

### 1.1 Import (CSV/Excel)
- [ ] Usato il **template** (A04) o un export “modello” da Odoo
- [ ] Verificato mapping colonne → campi; nessun errore in “Verifica”
- [ ] Abilitato (se richiesto) “Traccia cronologia durante l’import”
- [ ] Creati in anticipo: venditori, tag, aziende/valori necessari (se richiesto)

### 1.2 Inserimento manuale
- [ ] Titolo lead/opportunità conforme al naming
- [ ] Compilati: contatto, azienda, email/telefono (se disponibili)
- [ ] Impostati: source/origine e tag

### 1.3 Canali automatici / integrazioni
- [ ] Form sito web collegati al modello Lead/Opportunità
- [ ] Alias email (inbound) configurato per team o canale
- [ ] (Se applicabile) Integrazione Helpdesk → Opportunità per upselling

---

## 2) Triage e presa in carico (SLA)

- [ ] Lead assegnato (Addetto vendite + Team)
- [ ] Controllo duplicati / “lead simili” e gestione (unione/archiviazione)
- [ ] Pianificata **prima attività** (entro SLA interno, es. 1 giorno lavorativo)
- [ ] Inserite note minime di contesto (senza dati sensibili non necessari)
- [ ] Verificato Opt-Out e base giuridica/consenso per contatto (GDPR)

---

## 3) Qualificazione

- [ ] Verificato fit (bisogno, target, budget/autorità/tempi se applicabile)
- [ ] Aggiornati campi: priorità, tag, ricavo previsto (se stimabile)
- [ ] Aggiornato Chatter con esito contatto e prossimi passi
- [ ] Decisione: **Convertire in opportunità** / **Archiviare** / **Perso**

---

## 4) Conversione in opportunità

- [ ] Convertito lead → opportunità (o creata opportunità direttamente in pipeline)
- [ ] Cliente creato/collegato correttamente (nuovo o esistente)
- [ ] Opportunità in pipeline con fase corretta
- [ ] Pianificata prossima attività (nessuna opportunità senza next step)

---

## 5) Gestione pipeline e attività

- [ ] Opportunità spostata tra fasi quando avviene un evento reale (no backlog)
- [ ] Ogni attività completata → registrata in Chatter e pianificato step successivo
- [ ] Email inviate dal record (così restano tracciate e le risposte vengono acquisite)
- [ ] Riunioni inserite in Calendario (con invito al cliente quando necessario)
- [ ] Follower/menzioni usati per coinvolgere stakeholder (Direzione/Marketing/Delivery)

---

## 6) Preventivo e trattativa

- [ ] Creato preventivo da opportunità (app Vendite attiva)
- [ ] Preventivo collegato all’opportunità e al cliente corretto
- [ ] Allegati commerciali caricati (offerta, presentazioni, specifiche)
- [ ] Follow-up pianificati e tracciati (call/email/meeting)

---

## 7) Chiusura

### 7.1 Vinto (Won)
- [ ] Opportunità marcata Vinta al ricevimento conferma
- [ ] Documenti commerciali finali allegati (ordine/contratto)
- [ ] Handover a PM/Delivery avviato (SOP-PRJ-01) con informazioni minime

### 7.2 Perso (Lost)
- [ ] Opportunità marcata Persa appena confermato
- [ ] Motivo di perdita selezionato (obbligatorio)
- [ ] (Se utile) Pianificato re-engagement / nurturing

---

## 8) Reporting e review

- [ ] Review pipeline settimanale/bi-settimanale eseguita
- [ ] Opportunità senza attività o “ferme” identificate e gestite
- [ ] KPI minimi controllati: conversioni, win rate, durata ciclo, forecast, SLA

