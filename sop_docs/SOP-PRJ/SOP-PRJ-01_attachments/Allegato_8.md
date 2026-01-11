# Allegato 8 — Template “Descrizione Card [STORY]” (Odoo > Card > Campo “Descrizione”)

## Scopo
La card **[STORY]** rappresenta un requisito di valore (utente/business) e definisce:
- cosa deve ottenere l’utente (User Story);
- come si valida (AC = criteri di accettazione testabili);
- outcome, scope e deliverable attesi.

## Utilizzo (come si usa)
- Applica la label **[STORY]** alla card.
- Compila obbligatoriamente:
  - **Descrizione breve** e **Descrizione dettagliata**;
  - **User Story**;
  - **Criteri di accettazione (AC)**.
- Pianifica con Sprint e Story Point quando pronta.
- GitLab non va sulla STORY: se tecnico, inserirlo sulle **TASK tecniche collegate**.
- Se la lavorazione è ferma, sposta la card in **BLOCKED** (se presente) e aggiorna “Dipendenze” + “Note/rischi”.

---

## TEMPLATE (da incollare nella descrizione della card)

~~~text
[STORY] — User Story

Descrizione

Descrizione breve:
{{SINTESI_FUNZIONALE}}

Descrizione dettagliata: 
{{SCENARIO_REGOLE_VINCOLI_EDGE_CASES}}

User Story
Come **{{utente/ruolo}}**, voglio **{{funzionalità}}**, per **{{beneficio}}**.

Contesto
{{INFORMAZIONI_UTILI_PER_CAPIRE_LA_RICHIESTA}}

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

Criteri di accettazione (AC)

Checklist testabile (no frasi vaghe).
    {{AC1}}
    {{AC2}}
    {{AC3}}

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

DoD [STORY]
    AC soddisfatti e validati
    Evidenze presenti (link/screenshot/note)
    Documentazione aggiornata se necessaria
    (Se tecnico) attività tracciate su GitLab e chiuse dove applicabile
    Altro...
~~~
