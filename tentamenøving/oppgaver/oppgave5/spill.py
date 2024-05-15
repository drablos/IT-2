import pygame as pg
from spiller import Spiller
from ball import Ball
from hinder import Hinder
# Oppsett av pg
pg.init()
BREDDE = 900 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pg.display.set_mode((BREDDE, HOYDE))
klokke = pg.time.Clock()
kjorer = True
spillere = []
baller = []
hindere = []
spillere.append(Spiller(100, 1))
spillere.append(Spiller(800, 2))
baller.append(Ball())
for i in range(3):
    hindere.append(Hinder())
poeng_rod = 0
poeng_bla = 0
overskrift_font = pg.font.SysFont("Arial", 26)
pg.display.set_caption("Pong 2.0")

# oppsett:
while kjorer:
    overskrift_surface = overskrift_font.render(f"{poeng_bla} - {poeng_rod}", True, "white") 
    
    # Hendelser
    for hendelse in pg.event.get():
        # pg.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pg.QUIT:
            kjorer = False
 
 
    # Input fra tastatur:
    taster = pg.key.get_pressed()
    for spiller in spillere:
        spiller.beveg(taster)
    for ball in baller:
        ball.beveg()

    for ball in baller:
        for spiller in spillere:
            if ball.rect.colliderect(spiller):
                ball.dirx = ball.dirx * -1
                if len(baller) < 5:
                    baller.append(Ball())
        for hinder in hindere: 
            if ball.rect.colliderect(hinder):
                ball.dirx = ball.dirx * -1


    for ball in baller: 
        if ball.rect.centerx > 900: 
            baller.remove(ball)
            poeng_bla += 1
        elif ball.rect.centerx < 0:
            baller.remove(ball)
            poeng_rod += 1
    
    if len(baller) == 0:
        baller.append(Ball())

    # Oppdater spill her:
 
 
    # Tegn på skjermen her:
    vindu.fill("black")
    for spiller in spillere:
        spiller.tegn(vindu)
    for ball in baller:
        ball.tegn(vindu)
    for hinder in hindere:
        hinder.tegn(vindu)

    vindu.blit(overskrift_surface, (420, 10))
    # flip() oppdater vinduet med alle endringer
    pg.display.flip()
 
    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60) 
 
pg.quit()

