# Imports
import pygame
import random


# Window settings
GRID_SIZE = 64
WIDTH = 16 * GRID_SIZE
HEIGHT = 9 * GRID_SIZE
TITLE = "Game Title"
FPS = 60


# Create window
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (0, 150, 255)


# Load fonts


# Load images
hero_img = pygame.image.load('assets/images/characters/player_idle.png').convert_alpha()
grass_dirt_img = pygame.image.load('assets/images/tiles/grass_dirt.png').convert_alpha()
platform_img = pygame.image.load('assets/images/tiles/block.png').convert_alpha()
bush_img = pygame.image.load('assets/images/tiles/bush.png').convert_alpha()
gem_img = pygame.image.load('assets/images/items/gem.png').convert_alpha()
doorway_img = pygame.image.load('assets/images/tiles/open_door.png').convert_alpha()
enemy_img = pygame.image.load('assets/images/characters/enemy1a.png').convert_alpha()

# Load sounds

# Settings
gravity = 1.0
terminal_velocity =  24

# Game classes
class Hero(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE

        self.speed = 5
        self.jump_power = 15
        self.vx = 0
        self.vy = 0

        self.hurt_timer = 0
        self.health = 3
        self.gems = 0
        
    def move_right(self):
    	self.vx = self.speed
    	
    def move_left(self):
    	self.vx = -self.speed

    def stop(self):
        self.vx = 0
    
    def jump(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2

        if len(hits) > 0:
            self.vy -= self.jump_power

    def apply_gravity(self):
        self.vy += gravity

        if self.vy > terminal_velocity:
            self.vy = terminal_velocity

    def move_and_check_platforms(self):
        self.rect.x += self.vx

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vx > 0:
                self.rect.right = hit.rect.left
            elif self.vx < 0:
                self.rect.left = hit.rect.right

        self.rect.y += self.vy

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vy > 0:
                self.rect.bottom = hit.rect.top
            elif self.vy < 0:
                self.rect.top = hit.rect.bottom

            self.vy = 0


    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def check_enemies (self):
        if self.hurt_timer == 0 :
            hits = pygame.sprite.spritecollide(self, enemies, False)

            for enemy in hits:
                self.health -= 1
                self.hurt_timer = 1.0 * FPS
                print(self.health)
                print("oof")#playsound

        else:
            self.hurt_timer -= 1
            
            if self.hurt_timer < 0:
                self.hurt_timer = 0
            
    def check_items (self):
        hits = pygame.sprite.spritecollide(self, items, True)

        for item in hits:
            item.apply(self)
            
    
    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.check_items()
        self.check_enemies()

            
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE

        self.speed = 2
        self.vx = -1 * self.speed
        self.vy = 0
        

    def move_and_check_platforms(self):
        self.rect.x += self.vx

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vx > 0:
                self.rect.right = hit.rect.left
                self.vx = -1 * self.speed
            elif self.vx < 0:
                self.rect.left = hit.rect.right
                self.vx = self.speed

        self.rect.y += self.vy

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vy > 0:
                self.rect.bottom = hit.rect.top
            elif self.vy < 0:
                self.rect.top = hit.rect.bottom

            self.vy = 0


    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = self.speed
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vx = -1 * self.speed

    def update(self):
        self.move_and_check_platforms()
        self.check_world_edges()

class Gem(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE

    def apply(self, character):
        character.gems += 1
        print(character.gems)


            

# Helper functoins

# Setup
platforms = pygame.sprite.Group()

block_locs = [[0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8]
              ,[7,8],[8,8],[9,8],[10,8],[11,8],[12,8],[13,8],
              [14,8],[15,8],[16,8]]

for loc in block_locs:
    x = loc[0]
    y = loc[1]
    p = Platform(x, y, grass_dirt_img)
    platforms.add(p)

platform_locs = [[6,6],[7,6],[8,6],[11,4],[12,4],[13,4],[14,4]
                 ,[15,4], [7,7], [0,7]]

for loc in platform_locs:
    x = loc[0]
    y = loc[1]
    p = Platform(x, y, platform_img)
    platforms.add(p)

foreground = pygame.sprite.Group()

bush_locs = [[0,7],[7,7],[11,7],[16,7]]

for loc in bush_locs:
    x = loc[0]
    y = loc[1]
    b = Platform(x, y, bush_img)
    foreground.add(b)

items = pygame.sprite.Group()

gem_locs = [[12,3],[10,7]]

for loc in gem_locs:
    x = loc[0]
    y = loc[1]
    g = Gem(x, y, gem_img)
    items.add(g)

enemies = pygame.sprite.Group()

enemy_locs = [[9,7]]

for loc in enemy_locs:
    x = loc[0]
    y = loc[1]
    e = Enemy(x, y, enemy_img)
    enemies.add(e)

player = pygame.sprite.GroupSingle()

start_x = 3
start_y = 7
hero = Hero(start_x, start_y, hero_img)
player.add(hero)

# Physics settings
gravity = 0.5
terminal_velocity = 48

# Game loop
running = True

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.jump()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        hero.move_left()
    elif pressed[pygame.K_d]:
        hero.move_right()
    else:
        hero.stop()

    
    # Game logic
    player.update()
    enemies.update()
        
    # Drawing code
    screen.fill(SKY_BLUE)
    player.draw(screen)
    platforms.draw(screen)
    items.draw(screen)
    enemies.draw(screen)
    foreground.draw(screen)
        
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()

