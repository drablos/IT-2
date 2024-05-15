2.1
- 3
2.2
- 4
2.3
- 1 og 2
2.4
    FUNCTION trekanttall (n)
    SET tn TO n * (n+1)/2
    RETURN tn
    ENDFUNCTION
2.6
- 4
2.7
- 3
2.8
- 3
2.9/10/11
- [2.9/10/11](../tentamenøving/div-oppgaver.ipynb)
2.12
    1-F
    2-H
    3-A
    4-B
    5-C
    6-G
    7-E
    8-D
2.13
- 2 og 4
2.14
- 1.
  - 3
- 2.
FUNCTION byttPlass(liste, i, j)
  SET midlertidig TO a[i]
  SET a[i] TO a[j]
  set a[j] TO midlertidig 
ENDFUNCTION
SET bytta TO TRUE
WHILE bytta
  SET bytta TO FALSE
  SET i TO 0
  FOR hver i LESSER THAN n - 1
    IF a[i] GREATER THAN a[i+1]    
      CALL byttPlass(a, i, i + 1)
      SET bytta TO TRUE
    ENDIF
  ENDFOR
ENDWHILE
- 3
```py
def bytt_plass(liste, i, j):
    midlertidig = liste[i]
    liste[i] = liste[j]
    liste[j] = midlertidig
 
bytta = True
while bytta:
    bytta = False
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            bytt_plass(a, i, i + 1)
            bytta  = True
 
print(a)
``` 
2.15
```py
print("-- Huskelista --")
 

with open("huskeliste.txt", "r" encoding="utf-8") as fil:
    huskelisten = fil.readlines()
 
 
brukervalg = ""
while brukervalg != "avslutt":
    for gjøremål in huskelisten:
        print(f"- {gjøremål}")
    print("Skriv nytt gjøremål for å legge til i huskelista, avslutt asvlutter programmer")
    brukervalg = input("> ")
    if brukervalg != "avslutt":
        huskelisten.append(brukervalg)
 
print("Avslutter")    
 
with open("huskeliste.txt", "w" encoding="utf-8") as fil:
    fil.writelines(huskelisten)

```
2.16
- [spotify](../tentamenøving/div-oppgaver.ipynb)
2.17
- [imdb](../tentamenøving/div-oppgaver.ipynb)
