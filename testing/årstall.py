# Et program som tar inn alder og printer fødselsår

while True: # En evig-løkke
    try:
        alder = int(input("Hvor gammel blir du i år? ")) # hent inn brukerens alder og konverter alderen til et heltall
        if alder >= 0: # hvis brukerens alder er større eller lik 0
            break # bryt ut av løkka (avslutt løkka og gå videre i koden)
        print("Ugyldig tall. Prøv igjen.")
    except:
        print("Ugyldig input. Prøv igjen")

år_nå = 2024
fødselsår = 2024 - alder
print(f"Du r født i {fødselsår}")

