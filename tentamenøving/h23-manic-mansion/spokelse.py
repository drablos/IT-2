import random
from figur import Figur

class Spokelse(Figur):
    def __init__(self) -> None:
        tilfeldig_x = random.randint(150, 450)
        tilfeldig_y = random.randint(100, 500)
        super().__init__(tilfeldig_x, tilfeldig_y, "gray")
        self.fart = 1
        
    def oppdater_posisjon(self):
        if self.rect.bottom > 600:
            self.fart = -1
        elif self.rect.top < 0:
            self.fart = 1
        self.rect.y += self.fart
