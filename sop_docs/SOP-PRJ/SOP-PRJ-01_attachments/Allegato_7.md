# Allegato 7 — Template “Descrizione Card [EPIC]” (Odoo > Card > Campo “Descrizione”)

## Scopo
La card **[EPIC]** rappresenta un’iniziativa di alto livello che:
- aggrega **STORY** e **TASK**;
- definisce outcome, scope e deliverable principali;
- consente pianificazione e governance su orizzonti più ampi.

## Utilizzo (come si usa)
- Applica la label **[EPIC]** alla card.
- Compila obbligatoriamente **Descrizione breve** e **Descrizione dettagliata**.
- Definisci **Obiettivo/Valore**, **Output/Deliverable** e (se utile) **Scope IN/OUT**.
- Se un EPIC è fermo per dipendenze, spostalo in **BLOCKED** (se presente) e aggiorna “Dipendenze” + “Note/rischi”.
- GitLab non va qui: se tecnico, mettere GitLab sulle **TASK tecniche collegate**.

---

## TEMPLATE (da incollare nella descrizione della card)

~~~text
[EPIC] — Iniziativa di alto livello

Descrizione

Descrizione breve:
{{SINTESI_OUTCOME}}

Descrizione dettagliata:
{{CONTESTO_OBIETTIVO_VINCOLI}}

Contesto
{{PERCHÉ_ESISTE_EPIC_SCENARIO_ATTUALE}}

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

Soluzione / Approccio (alto livello)

Macro-strategia (non dettaglio tecnico): componenti, flusso generale, assunzioni principali.
    {{Punto 1}}
    {{Punto 2}}
    {{Punto 3}}

Pianificazione e governance

Priorità: {{Alta/Media/Bassa}}

Owner: {{NOME}}

Sprint: {{Sprint YYYY-XX-A}}

Story Point: {{1/2/3/5/8/13}}

Dipendenze:
{{TEAM_SISTEMI_DECISIONI_FORNITORI}}

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

DoD [EPIC]
    Tutte le STORY/TASK collegate sono in DONE (o motivate se escluse)
    Deliverable consegnati o dimostrabili (link/evidenze presenti)
    Documentazione aggiornata (se applicabile)
    Altro...
~~~
