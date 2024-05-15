print("Skriv poengsummen din:")
poengsum = int(input(">"))

if poengsum < 50:
    print("ikke bestått")
elif poengsum > 50 and poengsum < 69:
    print("Bestått")
elif poengsum > 70 and poengsum < 89:
    print("Godt bestått")
elif poengsum > 90 and poengsum < 100:
    print("Mykje godt bestått")
else:
    print("Ikkje gyldig poengsum")
