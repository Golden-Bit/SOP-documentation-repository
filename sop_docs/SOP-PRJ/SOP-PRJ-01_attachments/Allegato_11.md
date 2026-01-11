# Allegato 11 — Template “Descrizione Card [FIX]” (Odoo > Card > Campo “Descrizione”)

## Scopo
La card **[FIX]** rappresenta una correzione/miglioria tecnica mirata (debito tecnico, hardening, performance, refactor).  
Serve per:
- esplicitare **problema tecnico**, obiettivo misurabile e scope;
- descrivere approccio, test/verifica ed evidenze;
- garantire tracciabilità (GitLab) e qualità (DoD).

## Utilizzo (come si usa)
- Applica la label **[FIX]** alla card.
- Compila obbligatoriamente: **Contesto tecnico**, **Obiettivo**, **Scope IN/OUT**, **Test/Verifica**, **DoD**.
- Se tecnico: la lavorazione deve essere tracciata su GitLab (preferibilmente sulla TASK/FIX stessa).
- Se bloccata: spostala in **BLOCKED** (se presente) e aggiorna “Dipendenze” + “Note/rischi”.

---

## TEMPLATE (da incollare nella descrizione della card)

~~~text
[FIX] — Correzione / Miglioria tecnica

Descrizione

Descrizione breve:
{{COSA_CAMBIA + BENEFICIO_IN_1_RIGA}}

Descrizione dettagliata: 
{{CONTESTO_MOTIVAZIONE_IMPATTO_RISCHI_METRICHE_SE_ESISTONO}}

Contesto tecnico

Problema / Debito tecnico:
{{SINTOMO + IMPATTO (manutenibilità/performance/stabilità/sicurezza)}}

Area / componente:
{{COMPONENTE}}

Obiettivo, Output e Scope

Obiettivo:
{{RISULTATO_TECNICO_MISURABILE}}

Output / Deliverable attesi:
    {{MR/Refactor completato}}
    {{Documento/ADR/README aggiornato (se serve)}}
    {{Metriche/benchmark prima-dopo (se applicabile)}}

Scope IN:
    {{Cosa tocco / moduli / endpoint / job / pipeline}}

Scope OUT:
    {{Cosa NON tocco per evitare regressioni}}

Compatibilità / migrazioni:
{{NOTE_COMPATIBILITÀ_O_MIGRATION}}

Rollback (se necessario):
{{PIANO_ROLLBACK}}

Soluzione / Approccio
{{COSA_SI_CAMBIA_IN_3_6_PUNTI + eventuale rollback}}

Test / Verifica

Cosa verifico:
{{CHECKLIST_TEST}}
Ambienti:
{{dev/test/prod}}
Note:
{{NOTE}}

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

DoD [FIX]
    Implementazione completata
    Test eseguiti e/o CI ok (o motivazione documentata)
    Nessuna regressione nota (note su coverage/limiti test)
    Evidenze/metriche aggiornate (se applicabile)
    Doc/README/ADR aggiornati se necessario
    Issue chiusa e MR/commit collegati
    Altro...
~~~
