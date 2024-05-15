import pygame as pg
from objekt import Objekt
import random

class Ball(Objekt):
    def __init__(self) -> None:
        self.surface: pg.Surface = pg.Surface((15, 15))
        self.rect = self.surface.get_rect()
        self.surface.fill("white")
        self.rect.centerx = 450
        self.rect.centery = 300
        self.vel = 3
        startdir = random.randint(1, 2)
        if startdir == 1:
            self.dirx = 1
        else: 
            self.dirx = -1 
        self.diry = random.triangular(0,1)
    
        super().__init__(self.rect, self.surface)
    
    def beveg(self):
        if self.rect.centery > 595:
            self.diry =  random.triangular(0,1) * -1
        elif self.rect.centery < 5:
            self.diry =  random.triangular(0,1) * 1
        self.rect.centerx += self.vel * self.dirx
        self.rect.centery += self.vel * self.diry
        

