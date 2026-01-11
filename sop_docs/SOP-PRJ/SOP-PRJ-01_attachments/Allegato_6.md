# Allegato 6 — Template “Descrizione Card [PROJECT]” (Odoo > Card > Campo “Descrizione”)

## Scopo
La card **[PROJECT]** rappresenta un **riferimento a un altro progetto Odoo** (interno o cliente).  
Serve per:
- monitorare un progetto correlato dal board corrente (portfolio / dipendenze / coordinamento);
- rendere esplicito **il collegamento** (link) e **il motivo** della relazione;
- tracciare milestone, priorità e dipendenze tra progetti.

## Utilizzo (come si usa)
- Applica la label **[PROJECT]** alla card.
- Compila il campo **Progetto Odoo collegato (LINK)** (obbligatorio).
- Aggiorna milestone e dipendenze.
- Se la card/progetto è fermo, usa la colonna **BLOCKED** (se presente) e valorizza “Dipendenze principali” + “Rischi/Note”.

---

## TEMPLATE (da incollare nella descrizione della card)

~~~text
[PROJECT] — Riferimento a un altro progetto Odoo

Collegamento progetto (OBBLIGATORIO)

Progetto Odoo collegato (LINK): {{URL_PROGETTO_ODOO}}

Motivo collegamento: {{dipendenza / sotto-progetto / coordinamento / iniziativa correlata}}

Descrizione

Descrizione breve: 
{{...}}

Descrizione dettagliata:
{{...}}

Obiettivo e output

Obiettivo / Outcome: 
{{RISULTATO_ATTESO}}

Deliverable chiave: 
    {{Deliverable 1}} 
    {{Deliverable 2}} 

Milestone / Scadenze: 
{{DATE_EVENTI}}

Governance

Owner (PM/PO): {{NOME}}

Priorità: {{Alta/Media/Bassa}}

Dipendenze principali: 
{{COSA_BLOCCA_O_E_BLOCCATO}}

Rischi / Note:
    {{Rischio 1}} 
    {{Nota 1}} 

Collegamenti e Link rapidi (Drive/Repo/KB..)

Nome link | Contenuto link
---|---
Link 1 | www.link-1.com
Link 2 | www.link-2.com

DoD [PROJECT]
    Link al progetto Odoo presente
    Motivo del collegamento esplicitato
    Owner e priorità valorizzati
    Milestone/next step aggiornati
    Altro...
~~~