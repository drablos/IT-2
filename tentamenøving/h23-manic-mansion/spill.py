import pygame
from menneske import Menneske
from sau import Sau
from spokelse import Spokelse

# Oppsett av pygame
pygame.init() 
BREDDE = 600 
HOYDE = 600
BILDER_I_SEKUNDET = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
poeng_font = pygame.freetype.SysFont("Arial", 50)
poeng = 0

# Oppsett av spill, f.eks opprette spiller, hindere osv.
spiller = Menneske()
sauer = []
for i in range(3):
    sauer.append(Sau())

spokelser = []
for i in range(3):
    spokelser.append(Spokelse())


# Gameloop-en:
while True:
    # Hendelser
    hendelser = pygame.event.get() # en liste med alle hendelser som har skjedd siden forrige frame?
    for hendelse in hendelser:
        # Sjekker om spilleren trykker på kryss:
        if hendelse.type == pygame.QUIT:
            pygame.quit() # avslutt spill
            raise SystemExit # avslutt python-programmet

    # Input fra tastatur
    taster = pygame.key.get_pressed()
    
    if taster[pygame.K_UP]:
        spiller.y_fart = -1
        spiller.x_fart = 0

    if taster[pygame.K_DOWN]:
        spiller.y_fart = 1
        spiller.x_fart = 0

    if taster[pygame.K_LEFT]:
        spiller.x_fart = -1
        spiller.y_fart = 0

    if taster[pygame.K_RIGHT]:
        spiller.x_fart = 1
        spiller.y_fart = 0

    # Oppdater spillogikk her (oppdater fart, sjekk kollisjoner og så videre):
    spiller.oppdater_posisjon()
    for spokelse in spokelser:
        spokelse.oppdater_posisjon()
        if spiller.rect.colliderect(spokelse.rect):
            pygame.quit()
            raise SystemExit
    
    for sau in sauer:
        if spiller.rect.colliderect(sau.rect) and not spiller.bearer_sau and spiller.rect.left > 100:
            sau.blir_loftet = True
            spiller.bearer_sau = True
    
    if spiller.rect.left < 100: 
        for sau in sauer:
            if sau.blir_loftet:
                sau.rect.right = spiller.rect.left
                sau.rect.top = spiller.rect.top
                sau.blir_loftet = False
                spiller.bearer_sau = False
                poeng += 1
    
    spiller.oppdater_farge()

    # Tegn på vinduet:
    vindu.fill("black") # fyller vinduet med en bakgrunnsfarge, slik at vi fjerner alt fra forrige frame
    
    # Tegner røde frisoner på sidene av skjermen:
    pygame.draw.rect(vindu, "red", (0, 0, 100, HOYDE))
    pygame.draw.rect(vindu, "red", (BREDDE - 100, 0, 100, HOYDE))
    
    spiller.tegn(vindu)

    for sau in sauer:
        if not sau.blir_loftet:
            sau.tegn(vindu)
    
    for spokelse in spokelser:
        spokelse.tegn(vindu)

    poeng_font.render_to(vindu, (10, 10), f'Poeng: {poeng}', "white")

    
    pygame.display.flip()
    klokke.tick(BILDER_I_SEKUNDET)
