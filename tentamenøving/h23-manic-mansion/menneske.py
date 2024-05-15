from figur import Figur

class Menneske(Figur):
    def __init__(self) -> None:
        super().__init__(25, 300, "green")
        self.x_fart = 0
        self.y_fart = 0
        self.bearer_sau = False

    def oppdater_posisjon(self):
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart
    
    def oppdater_farge(self):
        if self.bearer_sau:
            self.surface.fill("blue")
        else:
            self.surface.fill("green")