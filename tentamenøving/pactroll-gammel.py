import pygame
import random

pygame.init()

# Spillets dimensjoner og FPS
BREDDE = 600
HOYDE = 600
FPS = 60

# Farger
SVART = (0, 0, 0)
GRØNN = (0, 255, 0)
GUL = (255, 255, 0)
GRÅ = (128, 128, 128)

# Konstanter for objektstørrelse
OBJ_SIZE = 30  # Størrelse på alle objekter (mat, hindring, troll)
COOLDOWN_TIME = 2000  # 2 sekunders cooldown i millisekunder

# Klasser

class Troll:
    def __init__(self):
        self.rect = pygame.Rect(BREDDE // 2 - OBJ_SIZE // 2, HOYDE // 2 - OBJ_SIZE // 2, OBJ_SIZE, OBJ_SIZE)  # Sentrum av spillbrettet
        self.speed = 5
        self.symbol = 'T'
        self.font = pygame.font.Font(None, int(OBJ_SIZE * 0.8))  # Skalerbar tekststørrelse
        self.last_hindrance_collision = None  # Hindringen som sist ble berørt
        self.hindrance_collision_count = {}  # Antall kollisjoner med hver hindring

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed

        # Begrens trollets bevegelse til spillbrettet
        self.rect.clamp_ip(pygame.Rect(0, 0, BREDDE - OBJ_SIZE, HOYDE - OBJ_SIZE))

    def draw(self, surface):
        pygame.draw.rect(surface, GRØNN, self.rect)
        symbol_render = self.font.render(self.symbol, True, SVART)
        symbol_rect = symbol_render.get_rect(center=self.rect.center)
        surface.blit(symbol_render, symbol_rect)

    def handle_hindrance_collision(self, hindrance):
        if hindrance != self.last_hindrance_collision:
            self.last_hindrance_collision = hindrance
            if hindrance in self.hindrance_collision_count:
                self.hindrance_collision_count[hindrance] += 1
            else:
                self.hindrance_collision_count[hindrance] = 1

    def should_end_game(self, hindrance):
        if hindrance in self.hindrance_collision_count:
            return self.hindrance_collision_count[hindrance] >= 2
        return False

class Matobjekt:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, OBJ_SIZE, OBJ_SIZE)
        self.symbol = 'M'
        self.font = pygame.font.Font(None, int(OBJ_SIZE * 0.6))  # Skalerbar tekststørrelse
        self.is_hindrance = False

    def draw(self, surface):
        pygame.draw.rect(surface, GUL, self.rect)
        symbol_render = self.font.render(self.symbol, True, SVART)
        symbol_rect = symbol_render.get_rect(center=self.rect.center)
        surface.blit(symbol_render, symbol_rect)


class Hindring:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, OBJ_SIZE, OBJ_SIZE)
        self.symbol = 'H'
        self.font = pygame.font.Font(None, int(OBJ_SIZE * 0.6))  # Skalerbar tekststørrelse

    def draw(self, surface):
        pygame.draw.rect(surface, GRÅ, self.rect)
        symbol_render = self.font.render(self.symbol, True, SVART)
        symbol_rect = symbol_render.get_rect(center=self.rect.center)
        surface.blit(symbol_render, symbol_rect)

# Hjelpefunksjoner

def place_objects(num_objects, obj_type, existing_positions):
    objects = []
    for _ in range(num_objects):
        while True:
            x = random.randint(0, BREDDE - OBJ_SIZE)
            y = random.randint(0, HOYDE - OBJ_SIZE)
            rect = pygame.Rect(x, y, OBJ_SIZE, OBJ_SIZE)
            if rect.collidelist(existing_positions) == -1:
                objects.append(obj_type(x, y))
                existing_positions.append(rect)
                break
    return objects

def random_position(exclude_rects):
    while True:
        x = random.randint(0, BREDDE - OBJ_SIZE)
        y = random.randint(0, HOYDE - OBJ_SIZE)
        rect = pygame.Rect(x, y, OBJ_SIZE, OBJ_SIZE)
        if rect.collidelist(exclude_rects) == -1:
            return x, y

# Initialisering av spill
vindu = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("PacTroll")

troll = Troll()
matobjekter = place_objects(3, Matobjekt, [troll.rect])
hindringer = []

score = 0
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Håndter input og oppdater spilltilstand
    troll.handle_input()

    # Sjekk kollisjon mellom troll og matobjekter
    for mat in matobjekter[:]:
        if troll.rect.colliderect(mat.rect):
            if not mat.is_hindrance:
                score += 1
                mat.is_hindrance = True
                hindringer.append(Hindring(mat.rect.x, mat.rect.y))
                matobjekter.remove(mat)
                # Legg til et nytt matobjekt
                matobjekter.append(Matobjekt(*random_position(matobjekter + hindringer + [troll.rect])))

    # Sjekk kollisjon mellom troll og hindringer
    for hindring in hindringer:
        if troll.rect.colliderect(hindring.rect):
            troll.handle_hindrance_collision(hindring)
            if troll.should_end_game(hindring):
                game_running = False

    # Tegn spilltilstand
    vindu.fill(SVART)
    troll.draw(vindu)
    for mat in matobjekter:
        mat.draw(vindu)
    for hindring in hindringer:
        hindring.draw(vindu)

    # Vis poengsum
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Poeng: {score}", True, GUL)
    vindu.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
