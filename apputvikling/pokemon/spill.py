import os
import sys
import json

# Klasser
class Trener:
    def __init__(self, navn) -> None:
        self.navn = navn
        self.pokemon_liste = []

    def legg_til_pokemon(self, pokemon):
        self.pokemon_liste.append(pokemon)


    def fjern_pokemon(self, pokemon):
        if pokemon in self.pokemon_liste:
            self.pokemon_liste.remove(pokemon)
        else:
            print(f"{pokemon} er ikke i treners Pokémon-liste.")

    def __str__(self) -> str:
        return f"{self.navn} {len(self.pokemon_liste)}"
    
class Pokemon:
    def __init__(self, pokemon_ordbok) -> None:
        self.navn: str = pokemon_ordbok["name"]["english"]
        self.type: list[str] = pokemon_ordbok["type"]
        self.hp: int = pokemon_ordbok["base"]["HP"]
        self.attack: int = pokemon_ordbok["base"]["Attack"]
        self.defence: int = pokemon_ordbok["base"]["Defense"]
        self.speed: int = pokemon_ordbok["base"]["Speed"]
    
    def __str__(self) -> str:
        return f"{self.navn} {self.hp}"

# 1. Oppsett
def rens_terminal():
    if sys.platform == "Windows" or sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

with open("pokemon.json", "r", encoding="utf-8") as fil:
    pokemoner = json.load(fil)

pokemon_liste = []
for pokemon in pokemoner:
    ny_pokemon = Pokemon(pokemon)
    pokemon_liste.append(ny_pokemon)
trener_liste = []
# 2. Gameloop
while True:
    rens_terminal()
    print("1. Se pokemonoversikt")
    print("2. Se treneroversikt")
    print("3. Legg til trener")
    print("4. Avslutt")

    brukervalg = input("> ")


    if brukervalg == "1":
        rens_terminal()
        print("-- Pokemonoversikt --")
        for pokemon in pokemon_liste:
            print(pokemon)
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input() # pauser koden helt til bruker trykker på enter
    
    elif brukervalg == "3":
        rens_terminal()
        print("-- Legg til trener --")
        navn = input("Skriv inn navnet på treneren: ")
        ny_trener = Trener(navn)
        trener_liste.append(ny_trener)
        print(f"Trener {navn} ble lagt til!")
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input() # pauser koden helt til bruker trykker på enter
    
    # 2. Se treneroversikt
    elif brukervalg == "2":
        rens_terminal()
        print("-- Treneroversikt --")
        if not trener_liste:
            print("Ingen trenere registrert ennå.")
        else:
            for trener in trener_liste:
                print(trener.navn)
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input() # pauser koden helt til bruker trykker på enter


