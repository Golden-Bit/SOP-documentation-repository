# Allegato SOP-ACC-01-A06 – Checklist operativa e controlli (Scenario Commercialista + Import XML)

---

## 1. Principio guida (da non perdere di vista)

Nel nostro assetto **il Commercialista è la fonte di verità fiscale e civilistica** (registri IVA, adempimenti, chiusure, cespiti, ecc.).
**Odoo** viene usato come **specchio gestionale interno** per:
* tracciabilità documentale (XML/PDF allegati ai record),
* monitoraggio di **scadenzari** e **pagamenti**,
* analisi per **cliente / fornitore / progetto** tramite **Contabilità Analitica**.

---

## 2. Routine settimanale (operativa)

### 2.1 Import e completamento documenti
- [ ] Recuperare dal Commercialista (o cartella condivisa) gli **XML** nuove fatture attive/passive.
- [ ] Importare in Odoo (singolo XML o ZIP batch) e verificare che:
  - [ ] partner corretto (cliente/fornitore),
  - [ ] importi/IVA corretti,
  - [ ] allegati presenti (XML + eventuale PDF),
  - [ ] stato documento coerente (Bozza → Pubblicato/Posted).
- [ ] Per i documenti “rilevanti” a progetto:
  - [ ] impostare **Analytic Distribution** sulle righe (100% sul progetto oppure split).

### 2.2 Scadenzario & solleciti
- [ ] Controllare **Aging Receivable** (clienti) e **Aging Payable** (fornitori).
- [ ] Evidenziare:
  - [ ] fatture clienti prossime alla scadenza / scadute,
  - [ ] fatture fornitori prossime alla scadenza.
- [ ] Condividere internamente la lista (Sales/PM/Direzione) con priorità di incasso/pagamento.

### 2.3 Riconciliazione bancaria
- [ ] Importare/sincronizzare transazioni bancarie (se attivo).
- [ ] Eseguire riconciliazione:
  - [ ] abbinare fatture aperte (Metodo “diretto”) **oppure**
  - [ ] abbinare pagamenti “outstanding” registrati in precedenza.
- [ ] Gestire eccezioni (commissioni, interessi, pagamenti cumulativi, pagamenti parziali).

---

## 3. Routine mensile (controllo di coerenza con Commercialista)

### 3.1 Completezza documentale
- [ ] Verificare che nel mese siano stati importati:
  - [ ] tutte le fatture attive emesse dal Commercialista,
  - [ ] tutte le fatture passive ricevute (XML o OCR/registrazioni manuali dove necessario).
- [ ] Confronto rapido con elenco del Commercialista (numero/data/totale).

### 3.2 Controllo IVA (coerenza gestionale)
- [ ] Eseguire report interni Odoo (totali IVA vendite/acquisti del mese/trimestre).
- [ ] Confrontare con liquidazione predisposta dal Commercialista.
- [ ] Se differenze:
  - [ ] cercare fatture mancanti/duplicate,
  - [ ] verificare aliquote o conti non coerenti.

### 3.3 Report pagamenti
- [ ] Estrarre lista pagamenti del mese:
  - [ ] incassi clienti (fatture segnate Paid),
  - [ ] pagamenti fornitori (bills segnate Paid).
- [ ] Inviare al Commercialista (se richiesto) un riepilogo o l’estratto conto bancario.

### 3.4 Controllo marginalità progetti (se usato)
- [ ] Per i progetti “fatturabili”:
  - [ ] verificare che **fatture** e **costi** compaiano in **Project Profitability**,
  - [ ] controllare che la distribuzione analitica sia corretta.

---

## 4. Routine annuale / chiusure (in coordinamento col Commercialista)

- [ ] Richiedere al Commercialista il riepilogo delle **scritture di assestamento** (ammortamenti, ratei/risconti, imposte, ecc.).
- [ ] Decisione interna: riportare o meno in Odoo tali scritture (anche **in forma sintetica**) per allineare i report direzionali.
- [ ] Archiviare in Drive (SOP-DOC) bilancio, dichiarazioni, F24 e evidenze.

---

## 5. Modello di comunicazione (email / messaggio ricorrente)

**Oggetto:** Allineamento contabilità Odoo – Periodo AAAA-MM

Corpo:
1) Batch XML importati in Odoo (attive/passive) + eventuali eccezioni/mancanze.
2) Differenze rilevate su IVA vendite/acquisti (se presenti).
3) Pagamenti eseguiti / incassi ricevuti con riferimenti (partner, importo, data valuta).
4) Note: fatture estere/PDF, note di credito, compensazioni, ecc.

---

## 6. Errori tipici da prevenire (quick check)

- [ ] Fattura importata ma **non pubblicata (Posted)** → non entra nei report.
- [ ] Documento a progetto senza **Analytic Distribution** → non entra in Project Profitability.
- [ ] Pagamento registrato senza riconciliazione bancaria → rischio doppioni/pendenze.
- [ ] Fatture pro-forma confuse con fatture ufficiali → rischio duplicazione ricavi.
- [ ] Periodo contabile bloccato → usare scritture correttive (saldo zero analitico) invece di modifiche dirette.

