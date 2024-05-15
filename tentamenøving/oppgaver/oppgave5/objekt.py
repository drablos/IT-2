import pygame as pg

class Objekt():
    def __init__(self, rect, surface) -> None:
        self.surface: pg.Surface = surface
        self.rect = rect

    def tegn(self, surface: pg.Surface):
        surface.blit(self.surface, self.rect)