# lese "vanlige tekstfiler"


# Åpne og lese fil i Python
fil = open("tullefil.txt", encoding="utf-8") # Åpner fila tullefil.txt med utf8-enkoding (lar oss bruke æ, ø og å)
data = fil.read() # leser innholdet i fila
fil.close() # lukker fila -> frigjør minne

# Alternativt
with open("tullefil.txt", encoding="utf-8") as fil:
    data = fil.read()

linjer = data.split("\n") # splitter innholdet på newline (\n), linjer er nå en liste der hver linje er et element
print(linjer)


# lese json-filer
import json # importerer json-bibloteket

fil = open("sanger.json", encoding="utf-8") # åpner fila sanger.json
sanger = json.load(fil) # leser innholdet og tolker det i json-format (sanger er her en liste med ordbøker)
fil.close() 

print(sanger[0])

#Alternativt:
with open("sanger.json", encoding="utf-8") as fil:
    sanger = json.load(fil)
    

#--------------------
#Eksempeloppgave
#Hvor mange sanger av artisten The Weeknd er det på topplista?

# sett antall til 0
antall = 0
# for hver sang i sanger
for sang in sanger:
#   hvis sang sin artist er lik Taylor Swift
    if sang["artist"] == "The Weeknd":
#   øk antall med 2
        antall += 1
#print antall
print(antall)
#--------------------

# Hvilken artist har flest sanger på topplista
# Du må lage kode, det er ikke lov å telle

print(len(sanger))

## Tankegang: 
# Lag en tom ordbok
artister = {}
# For hver sang i sanger
for sang in sanger:
# Sjekk om artisten finnes i ordboka
    if sang["artist"] in sanger:
    # Hvis ja øk antall med 1
        artister[sang["artist"]] += 1
    # Hvis nei: opprett ny nøkkel for artisten med verdien 1
    else:
        artister[sang["artister"]] = 1

# Sorter osv...
høyeste_artist = ""
høyeste_antall = -1


print(artister)
for artist in artister:
    antall_sanger = artister[artist]
    if antall_sanger > høyeste_antall:
        høyeste_artist = artist
        høyeste_antall = antall_sanger

print(høyeste_artist, høyeste_antall)







