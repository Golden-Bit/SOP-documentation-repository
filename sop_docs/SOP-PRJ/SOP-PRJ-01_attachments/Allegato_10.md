# Allegato 10 — Template “Descrizione Card [BUG]” (Odoo > Card > Campo “Descrizione”)

## Scopo
La card **[BUG]** rappresenta un difetto (gap tra atteso e reale).  
Serve per:
- rendere il bug **riproducibile** e classificato (ambiente, severità, priorità);
- documentare evidenze e impatto;
- guidare la correzione e la verifica post-fix.

## Utilizzo (come si usa)
- Applica la label **[BUG]** alla card.
- Compila obbligatoriamente la sezione **Riproduzione** + **Atteso vs Attuale**.
- Se tecnico: la correzione va tracciata su GitLab (preferibilmente sulla TASK tecnica collegata o direttamente sul bug se usato come work item tecnico).
- Se il bug è bloccato da dipendenze: spostalo in **BLOCKED** (se presente) e valorizza “Dipendenze” + “Note/rischi”.

---

## TEMPLATE (da incollare nella descrizione della card)

~~~text
[BUG] — Difetto

Descrizione

Descrizione breve:
{{PROBLEMA + IMPATTO_IN_1_RIGA}}

Descrizione dettagliata: 
{{CONTESTO_CHI_IMPATTA_FREQUENZA_WORKAROUND_SE_ESISTE}}

Classificazione

Ambiente: {{prod/test/dev}}
Versione / build: {{versione}}
Severità: {{Bloccante/Alta/Media/Bassa}}
Priorità: {{Alta/Media/Bassa}}

Riproduzione (OBBLIGATORIA)
    {{Step 1}}
    {{Step 2}}
    {{Step 3}}

Atteso vs Attuale

Atteso:
{{COSA_DOVREBBE_SUCCEDERE}}
Attuale:
{{COSA_SUCCEDE_ORA}}

Impatto

Impatto su utenti/processo:
{{IMPATTO}}
Workaround (se esiste):
{{WORKAROUND}}

Analisi (consigliata)

Causa probabile / componente:
{{IPOTESI_CAUSA}}
Note tecniche:
{{NOTE}}

Soluzione / Approccio (da completare quando si lavora o a fine fix)
{{COSA_SI_CAMBIA_IN_3_6_PUNTI + eventuale rollback}}

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

DoD [BUG]
    Riproduzione chiara presente
    Bug NON riproducibile con gli stessi passi (post-fix)
    Evidenze di test aggiornate (screenshot/log/link)
    (Se tecnico) CI ok o motivazione documentata
    (Se tecnico) MR/commit collegati e Issue chiusa
    Workaround aggiornato/rimosso (se applicabile)
    Altro...
~~~
