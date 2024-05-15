import pygame
from sys import exit
import math

from pygame.sprite import _Group
from innstillinger import *

pygame.init()

# Lage vindu
vindu = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Zombies")
klokke = pygame.time.Clock()

# laste inn bilder
bakgrunn = pygame.transform.scale(pygame.image.load("background/background.png").convert(), (BREDDE, HOYDE))

class Spiller(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pos = pygame.math.Vector2(SPILLER_START_X, SPILLER_START_Y)
        self.bilde = pygame.transform.rotozoom(pygame.image.load("player/0.png").convert_alpha(), 0, SPILLER_STORRELSE)
        self.grunnlag_bilde = self.bilde
        self.hitboks_rect = self.grunnlag_bilde.get_rect(center = self.pos)
        self.rect = self.hitboks_rect.copy()
        self.fart = SPILLER_FART
        self.skyt = False
        self.skyt_cooldown = 0

    def spiller_rotasjon(self):
        self.mus_kordinater = pygame.mouse.get_pos()
        self.x_endring_mus_spiller = (self.mus_kordinater[0] - self.hitboks_rect.centerx) 
        self.y_endring_mus_spiller = (self.mus_kordinater[1] - self.hitboks_rect.centery)
        self.vinkel = math.degrees(math.atan2(self.y_endring_mus_spiller, self.x_endring_mus_spiller)) # finner vinkel ved tangens
        self.bilde = pygame.transform.rotate(self.grunnlag_bilde, -self.vinkel)
        self.rect = self.bilde.get_rect(center = self.hitboks_rect.center)

    
    def bruker_input(self):
        self.hastighet_x = 0
        self.hastighet_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hastighet_y = -self.fart
        if keys[pygame.K_s]:
            self.hastighet_y = self.fart
        if keys[pygame.K_d]:
            self.hastighet_x = self.fart
        if keys[pygame.K_a]:
            self.hastighet_x = -self.fart

        if self.hastighet_x != 0 and self.hastighet_y != 0: # bevegelsen er diagonal
            self.hastighet_x /= math.sqrt(2)
            self.hastighet_y /= math.sqrt(2)

        if pygame.mouse.get_pressed() == (1, 0, 0) or keys[pygame.K_SPACE]:
            self.skyt = True
            self.skyting()
        else:
            self.skyt = False

    def skyting(self):
        if self.skyt_cooldown == 0:
            self.skyt_cooldown = SKYT_COOLDOWN
            self.skudd = 

    def beveg(self):
        self.pos += pygame.math.Vector2(self.hastighet_x, self.hastighet_y)
        self.hitboks_rect.center = self.pos
        self.rect.center = self.hitboks_rect.center

    
    def oppdater(self):
        self.bruker_input()
        self.beveg()
        self.spiller_rotasjon()

        if self.skyt_cooldown > 0:
            self.skyt_cooldown -= 1

class Skudd(pygame.sprite.Sprite):
    def __init__(self, x, y, vinkel) -> None:
        super().__init__()
        self.bilde = pygame.image.load("bullet/1.png").convert_alpha()
        self.bilde = pygame.transform.rotozoom(self.bilde, 0, 1.4, SKUDD_STR)
        self.rect = self.bilde.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.vinkel = vinkel
        self.fart = SKUDD_FART
        self.x_hastighet = math.cos(self.vinkel * (2 * math.pi / 360)) * self.fart
        self.y_hastighet = math.sin(self.vinkel * (2 * math.pi / 360)) * self.fart

    def skudd_bevegelse(self):
        self.x += self.x_hastighet
        self.y += self.y_hastighet

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def oppdater(self):
        self.skudd_bevegelse()

        
    
spiller = Spiller()

alle_sprites_grupper = pygame.sprite.Group()
skudd_gruppe = pygame.sprite.Group()

alle_sprites_grupper.add(spiller)


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    vindu.blit(bakgrunn, (0, 0))
    vindu.blit(spiller.bilde, spiller.rect)
    spiller.oppdater()
    # pygame.draw.rect(vindu, "red", spiller.hitboks_rect, width = 2)
    # pygame.draw.rect(vindu, "yellow", spiller.rect, width = 2)
    pygame.display.update()
    klokke.tick(FPS)

