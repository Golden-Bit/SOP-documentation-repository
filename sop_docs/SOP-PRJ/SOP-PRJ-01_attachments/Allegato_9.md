# Allegato 9 — Template “Descrizione Card [TASK]” (Odoo > Card > Campo “Descrizione”)

## Scopo
La card **[TASK]** rappresenta un’attività operativa eseguibile (tecnica o non tecnica).  
Serve per:
- tracciare un’unità di lavoro con output chiaro;
- definire prerequisiti, checklist, evidenze e link;
- garantire che DONE significhi “verificato” (DoD).

## Utilizzo (come si usa)
- Applica la label **[TASK]** alla card.
- Compila obbligatoriamente: **Descrizione breve/dettagliata**, **Checklist** e **DoD**.
- Se la task è tecnica: GitLab va collegato sulla TASK (come regola di tracciabilità).
- Se la task è ferma: spostala in **BLOCKED** (se presente) e aggiorna “Dipendenze” + “Note/rischi”.

---

## TEMPLATE (da incollare nella descrizione della card)

~~~text
[TASK] — Attività operativa

Descrizione

Descrizione breve:
{{SINTESI_FUNZIONALE}}

Descrizione dettagliata: 
{{CONTESTO_REQUISITI_INPUT_DESTINATARI_VINCOLI}}

Contesto e prerequisiti
{{INFO_UTILI_PRECONDIZIONI_MATERIALI_ACCESSI_NECESSARI}}

Obiettivo, Output e Scope

Obiettivo / Valore: 
{{RISULTATO_ATTESO_PERCHÉ_SERVE}}

Output / Deliverable attesi:
    {{Deliverable 1 (file/link/decisione/config/report)}}
    {{Deliverable 2}}

Scope (se utile):

Scope IN:
    {{Elemento 1}} 
    {{Elemento 2}} 

Scope OUT:
    {{Elemento escluso 1}} 
    {{Elemento escluso 2}} 

Checklist operativa
    {{Step 1}}
    {{Step 2}}
    {{Step 3}}
    {{Step N}}

Soluzione / Approccio (alto livello)
{{COME_VERRÀ_SVOLTA_IN_3_6_PUNTI}}

Pianificazione e governance

Priorità: {{Alta/Media/Bassa}}

Owner: {{NOME}}

Sprint: {{Sprint YYYY-XX-A}}

Story Point: {{1/2/3/5/8/13}}

Dipendenze: {{ALTRE_CARD_TEAM_SISTEMI}}

Milestone / Target date:
{{DATE}}

Note / rischi:
{{PUNTI}}

Evidenze / Output

Nome evidenza | Contenuto evidenza
---|---
Evidenza 1 | www.evidenza-1.com
Evidenza 2 | www.evidenza-2.com

Collegamenti e Link rapidi (Drive/Repo/KB..)

Nome link | Contenuto link
---|---
Link 1 | www.link-1.com
Link 2 | www.link-2.com

(Se tecnico) GitLab: inserire GitLab sulle TASK tecniche collegate

DoD [TASK]
    Output consegnato / pubblicato
    Evidenze presenti (link/screenshot/note)
    Checklist completata
    Note finali aggiornate
    (Se tecnico) GitLab Issue chiusa + MR/commit collegati (se applicabile)
    Altro...
~~~
