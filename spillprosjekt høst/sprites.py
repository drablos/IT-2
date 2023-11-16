import pygame, random, math, sys
from config import *

class Spritesheet:
    def __init__(self, fil) -> None:
        self.sheet = pygame.image.load(fil).convert_alpha()

    def get_sprite(self, x, y, bredde, hoyde):
        sprite = pygame.Surface([bredde, hoyde])
        sprite.blit(self.sheet, (0,0), (x, y, bredde, hoyde))
        sprite.set_colorkey(BLACK)
        return sprite


    
class Spiller(pygame.sprite.Sprite): # Klasse i pygame modulen som gjør det enklere å lage sprites
    def __init__(self, spill, x, y) -> None:
        self.spill = spill
        self._lag = SPILLER_LAG
        self.grupper = self.spill.alle_sprites
        pygame.sprite.Sprite.__init__(self, self.grupper)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.bredde = TILESIZE 
        self.hoyde = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = "down"
        self.animation_loop = 1

        self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
        
    

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.bevegelse()
        self.animer()

        self.rect.x += self.x_change
        self.kollisjon_blocks("x")
        self.rect.y += self.y_change
        self.kollisjon_blocks("y")

        self.x_change = 0
        self.y_change = 0


    def bevegelse(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= SPILLER_FART
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.x_change += SPILLER_FART
            self.facing = "right"
        if keys[pygame.K_UP]:
            self.y_change -= SPILLER_FART
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.y_change += SPILLER_FART
            self.facing = "down"
    
    def kollisjon_blocks(self, retning):
        if retning == "x":
            hits = pygame.sprite.spritecollide(self, self.spill.blokker, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if retning == "y":
            hits = pygame.sprite.spritecollide(self, self.spill.blokker, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom 


    def animer(self):
        down_animations = [self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(118, 128, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(206, 128, 25, self.hoyde)]

        up_animations = [self.spill.karakter_spritesheet.get_sprite(0, 192, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(59, 192, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(207, 192, 25, self.hoyde)]

        left_animations = [self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(0, 0, self.bredde, self.hoyde)]

        right_animations = [self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)]
        
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1







class Block(pygame.sprite.Sprite):
    def __init__(self, spill, x, y) -> None:

        self.spill = spill
        self._lag = BLOCK_LAG
        self.grupper = self.spill.alle_sprites, self.spill.blokker
        pygame.sprite.Sprite.__init__(self, self.grupper)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.bredde = TILESIZE 
        self.hoyde = TILESIZE

        self.image = self.spill.terrain_spritesheet.get_sprite(960, 448, self.bredde, self.hoyde)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Gress(pygame.sprite.Sprite):
    def __init__(self, spill, x, y) -> None:
        self.spill = spill
        self._lag = GRESS_LAG
        self.grupper = self.spill.alle_sprites
        pygame.sprite.Sprite.__init__(self, self.grupper)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.bredde = TILESIZE 
        self.hoyde = TILESIZE

        self.image = self.spill.terrain_spritesheet.get_sprite(64, 352, self.bredde, self.hoyde)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    




        

        

        







