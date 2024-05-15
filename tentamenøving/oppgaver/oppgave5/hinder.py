import pygame as pg 
import random
from objekt import Objekt


class Hinder(Objekt):
    def __init__(self) -> None:
        self.surface: pg.Surface = pg.Surface((10, 75))
        self.rect = self.surface.get_rect()
        self.surface.fill("white")
        self.rect.centerx = 450
        self.rect.centery = random.randint(100, 500)
        super().__init__(self.rect, self.surface)
    