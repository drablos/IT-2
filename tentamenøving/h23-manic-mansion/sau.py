import random
from figur import Figur

class Sau(Figur):
    def __init__(self) -> None:
        tilfeldig_x = random.randint(500, 550)
        tilfeldig_y = random.randint(100, 500)
        super().__init__(tilfeldig_x, tilfeldig_y, "yellow")
        self.blir_loftet = False
