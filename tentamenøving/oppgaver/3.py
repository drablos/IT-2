def er_primtall(tall:int):
    for i in range(tall - 1, 1, -1): #går gjennom hvert tall fra tall - 1 til 1
        if tall % i == 0: # sjekker hvor mye man får i rest etter å ha delt tallet på følgene tall
            return True # Sier at den er deleleig og ender løkka
    return False #sier at den er udeleleig

# Porgrammet går gjennom hvert tall under taller og sjekker hva det blir i rest ved deling
# hvis dette blir 0, så vil det si tallet er delelig og derfor ikke et primtall

print(er_primtall(7))
