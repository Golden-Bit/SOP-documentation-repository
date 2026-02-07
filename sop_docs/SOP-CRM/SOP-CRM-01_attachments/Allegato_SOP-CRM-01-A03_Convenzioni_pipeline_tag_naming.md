# Allegato SOP-CRM-01-A03 – Convenzioni e criteri (naming, tag, fasi pipeline)

> Obiettivo: standardizzare l’uso di campi e fasi per migliorare collaborazione e reportistica.

---

## 1) Naming standard (Titolo Lead/Opportunità)

**Formato consigliato**
- `NOME AZIENDA – SERVIZIO/PRODOTTO – ESIGENZA`  
  Esempi:
  - `XYZ S.p.A. – Digital Twin – Impianto Linea A`
  - `Comune di … – Software gestionale – Gara 2026`
  - `Mario Rossi (Privato) – Consulenza – Assessment iniziale`

**Regole**
- Evitare titoli generici (“Richiesta info”, “Preventivo”) senza contesto.
- Inserire la fonte solo se utile: `… – (Fiera Milano 2025)`.

---

## 2) Tag (etichette) e dizionario minimo

**Obiettivi**
- Segmentare per canale, settore, prodotto, priorità commerciale.

**Categorie suggerite**
- **Canale**: `SitoWeb`, `Evento`, `Referral`, `Outbound`, `Partner`
- **Temperatura**: `Hot`, `Warm`, `Cold`
- **Linea/Prodotto**: `Odoo`, `AI`, `DigitalTwin`, `FleetTracking`, …
- **Settore**: `Energy`, `PA`, `Manufacturing`, `Logistica`, …

**Regole**
- Evitare duplicati semantici (es. `Fiera` vs `Fiera2025` senza criterio).
- Mantenere coerenza (singolare/plurale, maiuscole, separatori).

---

## 3) Priorità (stelle ⭐)

- Vuoto = normale  
- ⭐ = media  
- ⭐⭐ = alta  
- ⭐⭐⭐ = massima  

**Criteri suggeriti**
- ⭐⭐⭐: opportunità strategiche / alto valore / scadenze ravvicinate.
- ⭐⭐: opportunità qualificate con next step pianificato e buona probabilità.
- ⭐: lead/opportunità in qualificazione o nurturing.

---

## 4) Fasi pipeline (standard) e criteri di avanzamento

> Le fasi possono essere personalizzate e, se necessario, rese specifiche per team.

### 4.1 Fasi standard (baseline)
1. **Nuovo**
   - Opportunità appena creata/convertita, primo contatto da effettuare.
2. **Qualificato**
   - Bisogno e interlocutore identificati; confermato interesse; next step definito.
3. **Proposta inviata**
   - Preventivo/offerta inviati (documento tracciato e allegato).
4. **Negoziazione**
   - Discussione attiva su prezzo/scope/tempi; possibili revisioni offerta.
5. **Vinto**
   - Conferma ordine/contratto ricevuta.
6. **Perso**
   - Perdita confermata e motivo registrato.

### 4.2 Criteri minimi (gate) per passare di fase
- **Nuovo → Qualificato**: primo contatto effettuato + raccolta informazioni minime (bisogno/fit).
- **Qualificato → Proposta inviata**: definito scope minimo + creato e inviato preventivo.
- **Proposta inviata → Negoziazione**: avviata trattativa (call/meeting) o richiesta revisione.
- **Negoziazione → Vinto/Perso**: decisione finale formalizzata.

### 4.3 Policy “Pipeline sana”
- Ogni opportunità aperta deve avere una **prossima attività** pianificata.
- Nessuna opportunità resta nella stessa fase senza attività > X giorni (definire soglia interna).
- Aggiornare fasi **quando accade l’evento**, non “a fine mese”.

---

## 5) Assegnazione e ownership

**Regola base**
- Ogni record deve avere:
  - **Addetto vendite** (owner operativo)
  - **Team di vendita**

**Condivisione e collaborazione**
- Aggiungere follower a opportunità sopra una soglia valore (es. Direzione).
- Usare menzioni @ nel Chatter per richieste interfunzionali (Marketing/Delivery/IT).

---

## 6) Lost reasons (motivi di perdita)

Definire un set minimo e mantenerlo stabile nel tempo per analisi coerenti, ad esempio:
- `Prezzo`
- `Competitor`
- `Non in target`
- `Timing / Priorità cliente`
- `Nessuna risposta`
- `Altro (specificare)`  

**Regola**: motivo sempre selezionato in chiusura Lost; se “Altro”, aggiungere nota.

