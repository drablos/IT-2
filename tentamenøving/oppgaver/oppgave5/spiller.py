import pygame as pg
from objekt import Objekt

class Spiller(Objekt):
    def __init__(self, x_kord, spiller) -> None:
        self.surface: pg.Surface = pg.Surface((20, 150))
        self.rect = self.surface.get_rect()
        if spiller == 1:
            self.surface.fill("blue")
        else:
            self.surface.fill("red")
        self.rect.centerx = x_kord
        self.rect.centery = 300
        self.spiller = spiller
        super().__init__(self.rect, self.surface)
    
    def beveg(self, KEY):
        if KEY[pg.K_w] and self.spiller ==  1 and self.rect.centery > 75:
            self.rect.centery -= 3
        if KEY[pg.K_s] and self.spiller ==  1 and self.rect.centery < 525:
            self.rect.centery += 3
        if KEY[pg.K_UP] and self.spiller ==  2 and self.rect.centery > 75:
            self.rect.centery -= 3
        if KEY[pg.K_DOWN] and self.spiller ==  2 and self.rect.centery < 525:
            self.rect.centery += 3
