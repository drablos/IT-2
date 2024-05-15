import pygame

class Figur:
    def __init__(self, x:int, y:int, farge:str):
        self.surface = pygame.Surface((50, 50))
        self.rect = self.surface.get_rect()

        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface:pygame.Surface):
        surface.blit(self.surface, self.rect)

class Troll(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "green")
        self.fart = 1
        self.retning = [0, 0]

    def oppdater_posisjon(self):
        self.rect.x += self.fart * self.retning[0]
        self.rect.y += self.fart * self.retning[1]

# Oppsett av pygame
pygame.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()


# OPPSETT AV SPILL HER:
troll = Troll(BREDDE/2, HOYDE/2)

while True:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
 
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        troll.retning = (0, -1)
    if taster[pygame.K_DOWN]:
        troll.retning = (0, 1)
    if taster[pygame.K_LEFT]:
        troll.retning = (-1, 0)
    if taster[pygame.K_RIGHT]:
        troll.retning = (1, 0)

    
    # Oppdater spill:
    troll.oppdater_posisjon()

    # Sjekker om troll er utenfor banen:
    if troll.rect.left < 0 or troll.rect.right > BREDDE or troll.rect.top < 0 or troll.rect.bottom > HOYDE:
        pygame.quit()
        raise SystemExit
    
    # Tegning:
    troll.tegn(vindu)

    pygame.display.flip()
    klokke.tick(60) 