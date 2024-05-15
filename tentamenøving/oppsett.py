import pygame

# Oppsett av pygame
pygame.init() 
BREDDE = 600 
HOYDE = 600
BILDER_I_SEKUNDET = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

# Oppsett av spill, f.eks opprette spiller, hindere osv.


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
        print("Du trykker på 'Pil opp' ")
    if taster[pygame.K_s]:
        print("Du trykket på 's' ")

    # Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()

    if mus_klikk[0]:
        x_pos = mus_posisjon[0]
        y_pos = mus_posisjon[1]
        print(f"Venstreklikk (en-finger) i posisjon x: {x_pos}, y: {y_pos}")

    if mus_klikk[2]:
        x_pos = mus_posisjon[0]
        y_pos = mus_posisjon[1]
        print(f"Høyreklikk (to-fingre) i posisjon x: {x_pos}, y: {y_pos}")

    
    # Oppdater spillogikk her (oppdater fart, sjekk kollisjoner og så videre):


    # Tegn på vinduet:
    vindu.fill("white") # fyller vinduet med en bakgrunnsfarge, slik at vi fjerner alt fra forrige frame

    
    pygame.display.flip()
    klokke.tick(BILDER_I_SEKUNDET)
