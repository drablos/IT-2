while True:
    navn = input("Hva heter du?").split(" ")
    if len(navn) >= 2:
        break
    else:
        print("Ugyldig navn. Navnet må minst inneholde to navn")

fornavn = navn[0].lower()
etternavn = navn[-1].lower()
etternavn_bokstav = etternavn[0]
brukernavn = fornavn + etternavn_bokstav + "@afk.no"
print(brukernavn)