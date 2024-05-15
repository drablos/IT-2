import pygame, random

class Figur:
    def __init__(self, x:int, y:int, farge:str):
        self.surface = pygame.Surface((40, 10))
        self.rect = self.surface.get_rect()

        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface:pygame.Surface):
        surface.blit(self.surface, self.rect)

class Spiller(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "white")
        self.fart = 5


    def håndter_input(self):
        taster = pygame.key.get_pressed()
        if taster[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.fart
        elif taster[pygame.K_d] and self.rect.right < BREDDE:
            self.rect.x += self.fart

class Hindring(Figur):
    def __init__(self):
        tilfeldig_x = random.randint(0, BREDDE)
        tilfeldig_y = random.randint(50, 300)
        super().__init__(tilfeldig_x, tilfeldig_y, "white")

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 5
        self.color = "white"
        self.speed = 5
        self.reset()

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.direction_x = 1
        self.direction_y = 1
    
    def move(self):
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y


        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen_width:
            self.direction_x *= -1
        
        if self.y - self.radius <= 0:
            self.direction_y *= -1

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def check_player_collision(self, player_rect):
        if player_rect.colliderect(pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)):
            self.direction_y *= -1

    

        

# Oppsett av pygame
pygame.init()
BREDDE = 400 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
poeng = 0
runde = 1

# OPPSETT AV SPILL HER:
spiller = Spiller(BREDDE/2, HOYDE/1.1)
ball = Ball(BREDDE, HOYDE)



hindre = []
for i in range(30):
    hindre.append(Hindring())





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
    spiller.håndter_input()
    ball.move()
    ball.check_player_collision(spiller.rect)

    hindre_fjern = 0
    
    for hindring in hindre:
        if hindring.rect.colliderect(pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)):
            hindre.remove(hindring)
            poeng += 1
            hindre_fjern += 1

    
    if hindre_fjern == 5:
        runde += 1
        ball.speed *= 1.5
    
    if hindre_fjern == 10:
        runde += 1
        ball.speed *= 1.5

    if hindre_fjern == 15:
        runde += 1
        ball.speed *= 1.5

    if hindre_fjern == 20:
        runde += 1
        ball.speed *= 1.5
    
    if hindre_fjern == 25:
        runde += 1
        ball.speed *= 1.5
        
        
        
        if  len(hindre) == 0:
            pygame.quit() # avslutt spill
            raise SystemExit # avslutt python-programmet
    

    if ball.y >= HOYDE:
            pygame.quit() # avslutt spill
            raise SystemExit # avslutt python-programmet
    
    
    
    

    
    # Tegning:
    spiller.tegn(vindu)
    ball.draw(vindu)
    for hindring in hindre:
        hindring.tegn(vindu)

    # Vis poeng
    poeng_tekst = font.render(f"Poeng: {poeng}", True, (255, 255, 255))
    runde_tekst = font.render(f"Runde: {runde}", True, (255, 255, 255))
    vindu.blit(poeng_tekst, (280, 10))
    vindu.blit(runde_tekst, (0, 10))

    pygame.display.flip()
    klokke.tick(60) 