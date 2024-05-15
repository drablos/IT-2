# Type hinting er spesielle kommentarer 
# som sier hvilken datatype parameter
# skal ha og hvilken datatypen funksjoner returnerer
# fahrenheit: int sier at parameteren fahrenheit
# skal være et int (heltall)
# -> float sier at funksjonen returnerer et float (desimaltall)

def fahrenheit_til_celsius(fahrenheit: int) -> float:
    return (fahrenheit - 32) * (5/9)

print(fahrenheit_til_celsius())

# Docstrings er spesielle kommentarer som beskriver en
# klasse, en funksjon eller et prgoram
# De skrives mellom tre anførselstegn øverst i klassen/
# funksjonen/programmet.

# Docstrings til en funksjon:

def celsius_til_fahrenheit(celsius: float) -> float:
    """
        En funksjon som konverterer  celsius til fahrenheit

        parametere
            celsius (float): antall grader i celsius
    """
    return (9/5) * celsius + 32

celsius_til_fahrenheit()

# Docstrings til en klasse:

class Elev:
    """
    Klasse for en elev på VGS

    attributter
        navn (str): Navnet på eleven
        trinn (int): Klassetrinnet til eleven
        klasse (str): Bokstavklassen til eleven 
        fag (list[str]): En liste med fag eleven tar
    
    metoder
        meld_opp_til_fag(fagnavn: str): Melder eleven opp til et fag
        dropp_ut_av_fag(fagnavn: str): Fjerner fag fra elevens fagliste
    """
    def __init__(self, navn: str, trinn: int, klasse: str) -> None:
        self.navn = navn
        self.trinn = trinn
        self.klasse = klasse
        self.fag = []

    def meld_opp_til_fag(self, fagnavn):
        self.fag.append(fagnavn)
    
    def dropp_ut_av_fag(self, fagnavn):
        self.fag.remove(fagnavn)

thor = Elev("Thor", 3, "STG")
ravi = Elev("Ravi", 2, "STB")




