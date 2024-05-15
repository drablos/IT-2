import pygame, random

class Figur:
    def __init__(self, x:int, y:int, farge:str):
        self.surface = pygame.Surface((10, 50))
        self.rect = self.surface.get_rect()

        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface:pygame.Surface):
        surface.blit(self.surface, self.rect)

class Spiller_1(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "green")
        self.fart = 5
        self.poeng = 0


    def håndter_input(self):
        taster = pygame.key.get_pressed()
        if taster[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.fart
        elif taster[pygame.K_s] and self.rect.bottom < HOYDE:
            self.rect.y += self.fart

        

class Spiller_2(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "red")
        self.fart = 5
        self.poeng = 0


    def håndter_input(self):
        taster = pygame.key.get_pressed()
        if taster[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.fart
        elif taster[pygame.K_DOWN] and self.rect.bottom < HOYDE:
            self.rect.y += self.fart

class Hindring(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "blue") 

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 10
        self.color = (255, 255, 255)
        self.speed = 3
        self.reset()

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.direction_x = random.choice([-1, 1])  # Random start direction (left or right)
        self.direction_y = random.choice([-1, 1])  # Random start direction (up or down)
    
    def move(self):
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y

        # Check collisions with top and bottom boundaries
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.direction_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_player_collision(self, player_rect):
        if player_rect.colliderect(pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)):
            self.direction_x *= -1

    def check_boundary_collision(self):
        if self.x - self.radius <= 0:
            spiller_2.poeng += 1  # Ballen treffer venstresiden, Spiller 2 får ett poeng
            self.reset()
        elif self.x + self.radius >= self.screen_width:
            spiller_1.poeng += 1  # Ballen treffer høyresiden, Spiller 1 får ett poeng
            self.reset()
    
    def check_hindring_collision(self, hindring_rects):
        for hindring in hindring_rects:
            if hindring.colliderect(pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)):
                # Kollisjon med hindring: endre ballens retning
                self.direction_x *= -1
                self.direction_y *= -1  # Kan tilpasses basert på ønsket atferd

    

# Oppsett av pygame
pygame.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()


# OPPSETT AV SPILL HER:
spiller_1 = Spiller_1(BREDDE/8, HOYDE/2)
spiller_2 = Spiller_2(BREDDE/1.2, HOYDE/2)
ball = Ball(BREDDE, HOYDE)

hindre = [
    Hindring(BREDDE/2, HOYDE/5),   
    Hindring(BREDDE/2, 2*HOYDE/5),
    Hindring(BREDDE/2, 3*HOYDE/5)  

]



font = pygame.font.Font(None, 36)

while True:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
 

    
    # Oppdater spill:
    spiller_1.håndter_input()
    spiller_2.håndter_input()
    ball.move()
    ball.check_player_collision(spiller_1.rect)
    ball.check_player_collision(spiller_2.rect)
    ball.check_boundary_collision()
    ball.check_hindring_collision([hindring.rect for hindring in hindre])

    
    # Tegning:
    spiller_1.tegn(vindu)
    spiller_2.tegn(vindu)
    ball.draw(vindu)
    for hindring in hindre:
        hindring.tegn(vindu)
    


    # Vis poeng
    poeng_tekst_1 = font.render(f"Poeng: {spiller_1.poeng}", True, (255, 255, 255))
    poeng_tekst_2 = font.render(f"Poeng: {spiller_2.poeng}", True, (255, 255, 255))
    vindu.blit(poeng_tekst_1, (10, 10))  # Tegner poengsummen for spiller 1 øverst til venstre
    vindu.blit(poeng_tekst_2, (BREDDE - poeng_tekst_2.get_width() - 10, 10))  # Tegner poengsummen for spiller 2 øverst til høyre

    pygame.display.flip()
    klokke.tick(60) 