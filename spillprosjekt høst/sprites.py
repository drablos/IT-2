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


        self.down_animations = [self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(118, 128, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(206, 128, 25, self.hoyde)]

        self.up_animations = [self.spill.karakter_spritesheet.get_sprite(0, 192, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(59, 192, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(207, 192, 25, self.hoyde)]

        self.left_animations = [self.spill.karakter_spritesheet.get_sprite(0, 161, 30, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(30, 161, 25, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(148, 161, 25, self.hoyde)]

        self.right_animations = [self.spill.karakter_spritesheet.get_sprite(119, 223, 30, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(149, 223, 28, self.hoyde),
                           self.spill.karakter_spritesheet.get_sprite(211, 223, 26, self.hoyde)]
        

    def update(self):
        self.bevegelse()
        self.animer()
        self.kollisjon_fiende()

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
    
    def kollisjon_fiende(self):
        hits = pygame.sprite.spritecollide(self, self.spill.fiender, False)
        if hits:
                self.kill()
                self.spill.playing = False
    
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
        
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.spill.karakter_spritesheet.get_sprite(0, 0, 25, self.hoyde)
            else: 
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

class Fiende(pygame.sprite.Sprite):
    def __init__(self, spill, x, y) -> None:
        self.spill = spill
        self._layer = FIENDE_LAG
        self.grupper = self.spill.alle_sprites, self.spill.fiender
        pygame.sprite.Sprite.__init__(self, self.grupper)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.bredde = TILESIZE 
        self.hoyde = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(["left", "right"])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)
        self.image = self.spill.fiende_spritesheet.get_sprite(3, 2, self.bredde, self.hoyde)

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.left_animations = [self.spill.fiende_spritesheet.get_sprite(3, 98, self.bredde, self.hoyde),
                           self.spill.fiende_spritesheet.get_sprite(35, 98, self.bredde, self.hoyde),
                           self.spill.fiende_spritesheet.get_sprite(68, 98, self.bredde, self.hoyde)]

        self.right_animations = [self.spill.fiende_spritesheet.get_sprite(3, 66, self.bredde, self.hoyde),
                           self.spill.fiende_spritesheet.get_sprite(35, 66, self.bredde, self.hoyde),
                           self.spill.fiende_spritesheet.get_sprite(68, 66, self.bredde, self.hoyde)]

    def update(self):
        self.bevegelse()
        self.animer()

        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0

    def bevegelse(self):
        if self.facing == "left":
            self.x_change -= FIENDE_FART
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = "right"
        if self.facing == "right":
            self.x_change += FIENDE_FART
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = "left"
    
    def animer(self):
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.spill.fiende_spritesheet.get_sprite(3, 98, self.bredde, self.hoyde)
            else: 
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.spill.fiende_spritesheet.get_sprite(3, 66, self.bredde, self.hoyde)
            else: 
                self.image = self.right_animations[math.floor(self.animation_loop)]
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

class Button:
    def __init__(self, x, y, bredde, hoyde, fg, bg, innhold, fontsize) -> None:
        self.font = pygame.font.SysFont('Helvetica', fontsize)
        self.innhold = innhold

        self.x = x
        self.y = y
        self.bredde = bredde
        self.hoyde = hoyde

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.bredde, self.hoyde))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.innhold, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.bredde/2, self.hoyde/2))
        self.image.blit(self.text, self.text_rect)
    
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Angrep(pygame.sprite.Sprite):
    def __init__(self, spill, x, y) -> None:
        self.spill = spill
        self._layer = SPILLER_LAG
        self.grupper = self.spill.alle_sprites, self.spill.angrep
        pygame.sprite.Sprite.__init__(self, self.grupper)

        self.x = x
        self.y = y
        self.bredde = TILESIZE
        self.hoyde = TILESIZE

        self.animation_loop = 0
        self.image = self.spill.angrep_spritesheet.get_sprite(0, 0, self.bredde, self.hoyde)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.right_animations = [self.spill.angrep_spritesheet.get_sprite(0, 64, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(32, 64, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(64, 64, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(96, 64, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(128, 64, self.bredde, self.hoyde)]

        self.down_animations = [self.spill.angrep_spritesheet.get_sprite(0, 32, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(32, 32, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(64, 32, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(96, 32, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(128, 32, self.bredde, self.hoyde)]

        self.left_animations = [self.spill.angrep_spritesheet.get_sprite(0, 96, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(32, 96, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(64, 96, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(96, 96, self.bredde, self.hoyde),
                           self.spill.angrep_spritesheet.get_sprite(128, 96, self.bredde, self.hoyde)]

        self.up_animations = [self.spill.angrep_spritesheet.get_sprite(0, 0, self.bredde, self.hoyde),
                         self.spill.angrep_spritesheet.get_sprite(32, 0, self.bredde, self.hoyde),
                         self.spill.angrep_spritesheet.get_sprite(64, 0, self.bredde, self.hoyde),
                         self.spill.angrep_spritesheet.get_sprite(96, 0, self.bredde, self.hoyde),
                         self.spill.angrep_spritesheet.get_sprite(128, 0, self.bredde, self.hoyde)]
    
    def update(self):
        self.animer()
        self.kollisjon()
    
    def kollisjon(self):
        hits = pygame.sprite.spritecollide(self, self.spill.fiender, True)
    
    def animer(self):
        retning = self.spill.spiller.facing
        
        if retning == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        
        if retning == "down":
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        
        if retning == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if retning == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()








        

    





        


    




        

        

        







