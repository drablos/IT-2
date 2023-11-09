import pygame, random
from spiller import Spiller

# Klasser
class Spiller:
    def __init__(self, x: int, y: int, bildesti: str) -> None:
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y
        pass
class Fiende:
    def __init__(self) -> None:
        pass
class Tre:
    def __init__(self) -> None:
        self.SPRITE = pygame.transform.scale(pygame.image.load("./bilder/tre.png"), (125,125))
        self.X_POS = random.randint(50, 300)
        self.Y_POS = random.randint(50, 450)
class Gress:
    def __init__(self) -> None:
        pass


# 1. Oppsett
pygame.init()
BREDDE = 1000
HOYDE = 600
FPS = 60
pygame.display.set_caption("The Legend of Zelda") # Gir tittel på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
spiller_bilde = pygame.image.load("bilder/").convert_alpha()
spiller_x = 50
spiller_y = 50
spiller_bredde = 50
spiller_høyde = 50
spiller_vel = 5


while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        # bevegelse av spiller
        taster = pygame.key.get_pressed()
        if taster[pygame.K_LEFT]:
            spiller_x -= spiller_vel

        if taster[pygame.K_RIGHT]:
            spiller_x += spiller_vel

        if taster[pygame.K_UP]:
            spiller_y -= spiller_vel

        if taster[pygame.K_DOWN]:
            spiller_y += spiller_vel

    # 3. Oppdater spill

    # 4. Tegn
    vindu.fill("white")

    
    





    pygame.display.flip()
    klokke.tick(FPS)