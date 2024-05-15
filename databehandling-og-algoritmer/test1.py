def bytt_plass(liste, i, j):
    midlertidig = liste[i]
    liste[i] = liste[j]
    liste[j] = midlertidig

min_liste = [8, 5, 2, 6, 12]
n = len(min_liste)
bytta = True
while bytta:
    bytta = False
    for i in range(n-1):
        if min_liste[i] > min_liste[i+1]:
            bytt_plass(min_liste, i, i + 1)
            bytta = True

print(min_liste)
