import pygame
import random
import math
import sys

# Constants
WIDTH = 640
HEIGHT = 480
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 3
BLOCK_LAYER = 2
GRASS_LAYER = 1

PLAYER_SPEED = 3

BLACK = (0, 0, 0)

tilemap = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B..................B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B.......B..........B",
    "B.......BBB........B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B.................SB",
    "BBBBBBBBBBBBBBBBBBBB",
]

# Classes
class Spritesheet:
    def __init__(self, filename) -> None:
        self.sheet = pygame.image.load(filename).convert_alpha()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self.layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = "down"
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, 25, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.move()
        self.animate()

        self.rect.x += self.x_change
        self.check_collision("x")
        self.rect.y += self.y_change
        self.check_collision("y")

        self.x_change = 0
        self.y_change = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = "right"
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED

    def check_collision(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            if direction == "x":
                self.rect.x = hits[0].rect.left - self.rect.width if self.x_change > 0 else hits[0].rect.right
            if direction == "y":
                self.rect.y = hits[0].rect.top - self.rect.height if self.y_change > 0 else hits[0].rect.bottom

    def animate(self):
        animations = {
            "down": [self.game.character_spritesheet.get_sprite(0, 0, 25, self.height),
                     self.game.character_spritesheet.get_sprite(118, 128, 25, self.height),
                     self.game.character_spritesheet.get_sprite(206, 128, 25, self.height)],

            "up": [self.game.character_spritesheet.get_sprite(0, 192, 25, self.height),
                   self.game.character_spritesheet.get_sprite(59, 192, 25, self.height),
                   self.game.character_spritesheet.get_sprite(207, 192, 25, self.height)],

            "left": [self.game.character_spritesheet.get_sprite(0, 0, 25, self.height),
                     self.game.character_spritesheet.get_sprite(0, 0, 25, self.height),
                     self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)],

            "right": [self.game.character_spritesheet.get_sprite(0, 0, 25, self.height),
                      self.game.character_spritesheet.get_sprite(0, 0, 25, self.height),
                      self.game.character_spritesheet.get_sprite(0, 0, 25, self.height)]
        }

        if self.y_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 0, 25, self.height)
        else:
            direction_animations = animations.get(self.facing, [])
            if direction_animations:
                self.image = direction_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self.layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self.layer = GRASS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("The Legend of Zelda")
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet("bilder/character.png")
        self.terrain_spritesheet = Spritesheet("bilder/terrain.png")

    def create_tilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Grass(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "S":
                    Player(self, j, i)

    def new_game(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.players = pygame.sprite.LayeredUpdates()

        self.create_tilemap()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.window.fill(BLACK)
        self.all_sprites.draw(self.window)
        self.clock.tick(FPS)
        pygame.display.update()

    def main_loop(self):
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


if __name__ == "__main__":
    game_instance = Game()
    game_instance.intro_screen()
    game_instance.new_game()
    while game_instance.running:
        game_instance.main_loop()
        game_instance.game_over()
    pygame.quit()
    sys.exit()
