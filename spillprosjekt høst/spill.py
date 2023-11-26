import pygame, sys
from sprites import *
from config import *

class Spill:
    def __init__(self) -> None:
        pygame.init()
        self.vindu = pygame.display.set_mode((BREDDE, HOYDE))
        pygame.display.set_caption("The Legend of Zelda") # Gir tittel på vinduet
        self.clock= pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont('Helvetica', 32)
        self.points = 0
        self.karakter_spritesheet = Spritesheet("bilder/character.png")
        self.terrain_spritesheet = Spritesheet("bilder/terrain.png")
        self.fiende_spritesheet = Spritesheet("bilder/enemy.png")
        self.angrep_spritesheet = Spritesheet("bilder/attack.png")
        self.intro_background = pygame.image.load("bilder/introbackground.png")
        self.go_background = pygame.image.load("bilder/gameover.png")

    
    def lag_tilemap(self):
        for i, row in enumerate(tilemap): #Har 2 verdier: i og row. i blir satt til posisjonen i listen, row blir satt til verdien av objektet i listen
            for j, column in enumerate(row):
                Gress(self, j, i)
                if column == "B":
                    Block(self, j, i) # j = x posisjonen i = y posisjonen
                if column == "F":
                    Fiende(self, j, i)
                if column == "S":
                    self.spiller = Spiller(self, j, i)
    
    def display_points(self):
        points_text = self.font.render(f"Poeng: {self.points}", True, WHITE, BLACK)
        points_rect = points_text.get_rect(topright=(BREDDE - 10, 10))
        self.vindu.blit(points_text, points_rect)


    def ny(self):
        # nytt spill starter
        self.playing = True

        self.points = 0 # sette poeng tilbake til 0 etter man har dødd
        self.alle_sprites = pygame.sprite.LayeredUpdates() # Objekt som inneholder alle sprites til spillet, en gruppe gjør at mnan kan oppdatere alle på en gang
        self.blokker = pygame.sprite.LayeredUpdates()
        self.fiender = pygame.sprite.LayeredUpdates()
        self.angrep = pygame.sprite.LayeredUpdates()

        self.lag_tilemap()
    

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.spiller.facing == "up":
                        Angrep(self, self.spiller.rect.x, self.spiller.rect.y - TILESIZE)
                    if self.spiller.facing == "down":
                        Angrep(self, self.spiller.rect.x, self.spiller.rect.y + TILESIZE)
                    if self.spiller.facing == "left":
                        Angrep(self, self.spiller.rect.x - TILESIZE, self.spiller.rect.y)
                    if self.spiller.facing == "right":
                        Angrep(self, self.spiller.rect.x + TILESIZE, self.spiller.rect.y)

    
    def update(self):
        self.alle_sprites.update()


    def tegn(self):
        # game loop tegn
        self.vindu.fill(BLACK)
        self.alle_sprites.draw(self.vindu)
        self.display_points()
        self.clock.tick(FPS)
        pygame.display.update()


    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.tegn()
    
    
    def game_over(self):
        text = self.font.render("Game over", True, WHITE)
        text_rect = text.get_rect(center = (BREDDE/2, HOYDE/2))
        restart_button = Button(10, HOYDE - 60, 120, 50, WHITE, BLACK, "Restart", 32)

        for sprite in self.alle_sprites:
            sprite.kill()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.ny()
                self.main()
            
            self.vindu.blit(self.go_background, (0,0))
            self.vindu.blit(text, text_rect)
            self.vindu.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    
    def intro_skjerm(self):
        intro = True

        tittel = self.font.render("The Legend of Zelda", True, BLACK)
        tittel_rect = tittel.get_rect(x = 10, y = 10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, "Play", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.vindu.blit(self.intro_background, (0,0))
            self.vindu.blit(tittel, tittel_rect)
            self.vindu.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

s = Spill()
s.intro_skjerm()
s.ny()
while s.running:
    s.main()
    s.game_over()
pygame.quit()
sys.exit()