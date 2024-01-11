# Oppgaver - Algoritmer, pseudokode og flytdiagram

## Oppgave 1

Svar: C

## Oppgave 2

Svar: C

## Oppgave 3

Svar: C

## Oppgave 4

Svar:  C

## Oppgave 5

Svar: D

## Oppgave 6

Svar: Alternativ 3

## Oppgave 7
[Bilde](./Flytdiagramoppgave7.png)

## Oppgave 8
FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION

FUNCTION totalsumtrekanttall()
  SET total TO 0
  FOR i FROM 1 TO 10
    SET trekantTall TO trekanttall(i)
    SET total TO total + trekantTall
  ENDFOR
  OUTPUT "Totalsummen av de ti første trekanttallene er:" total
ENDFUNCTION

