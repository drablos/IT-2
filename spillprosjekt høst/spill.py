import pygame, random, sys
from sprites import *
from config import *

class Spill:
    def __init__(self) -> None:
        pygame.init()
        self.vindu = pygame.display.set_mode((BREDDE, HOYDE))
        pygame.display.set_caption("The Legend of Zelda") # Gir tittel på vinduet
        self.clock= pygame.time.Clock()
        self.running = True

        self.karakter_spritesheet = Spritesheet("bilder/character.png")
        self.terrain_spritesheet = Spritesheet("bilder/terrain.png")

    
    def lag_tilemap(self):
        for i, row in enumerate(tilemap): #Har 2 verdier: i og row. i blir satt til posisjonen i listen, row blir satt til verdien av objektet i listen
            for j, column in enumerate(row):
                Gress(self, j, i)
                if column == "B":
                    Block(self, j, i) # j = x posisjonen i = y posisjonen
                if column == "S":
                    Spiller(self, j, i)
                    


    def ny(self):
        # nytt spill starter
        self.playing = True

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


    
    def update(self):
        self.alle_sprites.update()



    
    def tegn(self):
        # game loop tegn
        self.vindu.fill(BLACK)
        self.alle_sprites.draw(self.vindu)
        self.clock.tick(FPS)
        pygame.display.update()


    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.tegn()
        self.running = False
    
    
    def game_over(self):
        pass
    
    def intro_skjerm(self):
        pass
s = Spill()
s.intro_skjerm()
s.ny()
while s.running:
    s.main()
    s.game_over()
pygame.quit()
sys.exit()
