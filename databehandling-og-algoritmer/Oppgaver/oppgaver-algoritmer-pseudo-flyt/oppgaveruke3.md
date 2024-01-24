# Oppgaver - Algoritmer, pseudokode og flytdiagram uke 3

## Oppgave 9
Svar D

## Oppgave 10
A - 3
B - 4
C - 5
D - 8
E - 7
F - 1
G - 6
H - 2

## Oppgave 11
Svar 1

```python
listen = [32, 10, -5, 99, 1]
# 1.
størst = float("-inf")
for tall in listen:
    if tall > størst:
        størst = tall
print(størst)
listen.remove(størst)
nestStørst = float("-inf")
for tall in listen:
    if tall > nest_størst:
print(nestStørst)

#2.
listen = [32, 10, -5, 99, 1]
størst = listen[0]
nest_størst = listen[1]

if nest_størst > størst:
    størst, nest_størst = nest_størst, størst # bytter verdier på variablene
for tall in listen[2:]:
    if tall > størst:
        nest_størst = størst
        størst = tall
    elif tall > nest_størst and tall != størst:
print(nest_størst)









```


