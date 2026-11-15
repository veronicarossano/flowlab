# FlowLab — diagrammi a blocchi per studenti

Sviluppato da **Prof.ssa Veronica Rossano** (Gruppo di ricerca TELL) — Dipartimento di Informatica, Università degli Studi di Bari — con il supporto di Claude Code.
Licenza **CC BY-NC-SA 4.0** (vedi [LICENZA.md](LICENZA.md)).

**Per usarla:** fai doppio clic su `FlowLab.html`. Funziona in qualsiasi browser recente (Chrome, Edge, Firefox, Safari) e anche senza internet: i font sono già inclusi nel file.

## Cosa fa
- **Progetto con più diagrammi**: il programma principale più tutti i sottoprogrammi che servono.
- **Passaggio di parametri**: ogni sottoprogramma dichiara i suoi parametri formali, in ordine, per valore o per riferimento. Nella chiamata, ad esempio `calcolaMedia(classe, media)`, si scrivono i parametri attuali, che possono avere nomi diversi dai formali.
- **Solo i costrutti fondamentali**: sequenza, selezione, ciclo precondizionale e ciclo postcondizionale. Le forme ammesse sono ovale, rettangolo, rombo e parallelogramma.
- **Frecce automatiche**: trascini un blocco dalla barra in basso su una freccia, oppure clicchi il `+` su una freccia e scegli dal menu circolare.
- **Variabili**: globali (programma principale), locali e parametri (sottoprogrammi). Per ognuna scegli tipo, ruolo (input / output / di lavoro) e vincolo di integrità.
- **Array e record**: array a una dimensione e matrici (`v[i]`, `m[i, j]`), tipi record definiti nel pannello Progetto (`s.nome`), anche annidati (`classe[i].voto`). Il primo indice degli array (0 o 1) si sceglie per ogni progetto.
- **Trace**: esecuzione passo passo, passo indietro, punti di interruzione (Alt+clic), tabella di traccia (esportabile in CSV) con gli elementi cambiati evidenziati, pila delle chiamate, valori di prova. Array e record si vedono come tabelline nel pannello Variabili.
- **Verifica in tempo reale**: errori di sintassi e di tipo, indici e campi sbagliati, parametri mancanti o del tipo sbagliato, variabili non dichiarate (con la correzione "Dichiara").
- **Leggibilità**: font OpenDyslexic, Lexend o Atkinson Hyperlegible; dimensione, spaziatura e interlinea regolabili; temi chiaro, crema e scuro.
- **Pseudocodice** generato dai diagrammi; esportazione SVG/PNG; stampa / PDF dell'intero progetto.

Nel menu File ci sono due esempi: «Media dei voti» e «Classe» (array di record e parametri).

I progetti si salvano come file `.flowlab` (menu File). Il browser tiene anche una copia automatica dell'ultimo lavoro. I progetti creati con la versione precedente si aprono senza modifiche.

## Per modificare l'app
I sorgenti sono in `src/`. Dopo una modifica, rigenera il file unico con:

```bash
python3 build.py
```
