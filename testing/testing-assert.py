def partall(tall: int):
    # En funksjon som tar inn et heltall (int)
    # og returner True hvis tallet er et partall
    # og False hvis tallet er et oddetall
    if tall % 2 == 0:
        return True
    else:
        return False


# -- Tester --
assert partall(2) == True, "2 er et partall"
assert partall(3) == False, "3 er IKKE et partall"
assert partall(-5) == False, "-5 er IKKE et partall"
assert partall(-2) == True, "-2 er et partall"

print("Alle tester: OK!")

print(partall(2)) # -> True
print(partall(3)) # -> False