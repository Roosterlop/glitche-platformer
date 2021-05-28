# Imports
import pygame
import random
import json

# Window settings
GRID_SIZE = 64
WIDTH = 24 * GRID_SIZE
HEIGHT = 15 * GRID_SIZE
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
GRAY = (175, 175, 175)

#Stages
START = 0
PLAYING = 1
LOSE = 2
LEVEL_COMPLETE = 3
WIN = 4

# Load fonts
font_xl = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 96)
font_lg = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 64)
font_md = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 32)
font_sm = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 24)
font_xs = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 12)
font_xs = pygame.font.Font(None, 14)

# Load images
bg1_img = pygame.image.load('assets/images/background/backgroundColorForest.png').convert_alpha()
bg2_img = pygame.image.load('assets/images/background/backgroundForest.png').convert_alpha()
bg3_img = pygame.image.load('assets/images/background/backgroundColorGrass.png').convert_alpha()
bg4_img = pygame.image.load('assets/images/background/backgroundcastles.png').convert_alpha()

bush_img = pygame.image.load('assets/images/tiles/bush.png').convert_alpha()
gem_img = pygame.image.load('assets/images/items/gem.png').convert_alpha()
heartf_img = pygame.image.load('assets/images/items/heart_full.png').convert_alpha()
hearte_img = pygame.image.load('assets/images/items/heart_empty.png').convert_alpha()

#knight images
knight_img = pygame.image.load('assets/images/characters/knight/knightidle1.png').convert_alpha()

# Blocks
wallbanner_img = pygame.image.load('assets/images/tiles/wallbanner.png').convert_alpha()
banner_img = pygame.image.load('assets/images/tiles/banner.png').convert_alpha()
bannerendl_img = pygame.image.load('assets/images/tiles/bannerendl.png').convert_alpha()
bannerendr_img = pygame.image.load('assets/images/tiles/bannerendr.png').convert_alpha()
backwalls_img = pygame.image.load('assets/images/tiles/stone.png').convert_alpha()
wall_img = pygame.image.load('assets/images/tiles/walls.png').convert_alpha()
castletl_img = pygame.image.load('assets/images/tiles/castletl.png').convert_alpha()
castlet_img = pygame.image.load('assets/images/tiles/castlet.png').convert_alpha()
castletr_img = pygame.image.load('assets/images/tiles/castletr.png').convert_alpha()

grass_dirt_img = pygame.image.load('assets/images/tiles/grass_dirt.png').convert_alpha()
platform_img = pygame.image.load('assets/images/tiles/block.png').convert_alpha()

doorwayt_img = pygame.image.load('assets/images/tiles/open_doort.png').convert_alpha()
doorwayl_img = pygame.image.load('assets/images/tiles/open_doorl.png').convert_alpha()

exits_img = pygame.image.load('assets/images/tiles/exits.png').convert_alpha()
exitt_img = pygame.image.load('assets/images/tiles/exitt.png').convert_alpha()
exitb_img = pygame.image.load('assets/images/tiles/exitb.png').convert_alpha()

#Enemy images
enemy_imgs = [pygame.image.load('assets/images/characters/enemy1a.png').convert_alpha(),
              pygame.image.load('assets/images/characters/enemy1b.png').convert_alpha()]

bee_imgs = [pygame.image.load('assets/images/characters/enemies/bee.png').convert_alpha(),
           pygame.image.load('assets/images/characters/enemies/bee_fly.png').convert_alpha()]

bee_imgs_rt = [pygame.image.load('assets/images/characters/enemies/bee.png').convert_alpha(),
           pygame.image.load('assets/images/characters/enemies/bee_fly.png').convert_alpha()]
bee_imgs_lt = [pygame.transform.flip(img, True, False) for img in bee_imgs_rt]

#Card images
card2_img = pygame.image.load('assets/images/items/card_hearts_02.png').convert_alpha()
card3_img = pygame.image.load('assets/images/items/card_hearts_03.png').convert_alpha()
card4_img = pygame.image.load('assets/images/items/card_hearts_04.png').convert_alpha()
card5_img = pygame.image.load('assets/images/items/card_hearts_05.png').convert_alpha()
card6_img = pygame.image.load('assets/images/items/card_hearts_06.png').convert_alpha()
card7_img = pygame.image.load('assets/images/items/card_hearts_07.png').convert_alpha()
card8_img = pygame.image.load('assets/images/items/card_hearts_08.png').convert_alpha()
card9_img = pygame.image.load('assets/images/items/card_hearts_09.png').convert_alpha()
card10_img = pygame.image.load('assets/images/items/card_hearts_10.png').convert_alpha()
cardj_img = pygame.image.load('assets/images/items/card_hearts_J.png').convert_alpha()
cardq_img = pygame.image.load('assets/images/items/card_hearts_Q.png').convert_alpha()
cardk_img = pygame.image.load('assets/images/items/card_hearts_K.png').convert_alpha()
carda_img = pygame.image.load('assets/images/items/card_hearts_A.png').convert_alpha()

# Load sounds

#levels
levels = ["assets/levels/world-1.json",
          "assets/levels/world-2.json"]

# Settings
gravity = 1.0
terminal_velocity =  24

# Game classes
class Entity(pygame.sprite.Sprite):


    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE //2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE //2

        self.vx = 0
        self.vy = 0
        
    def apply_gravity(self):
        self.vy += gravity

        if self.vy > terminal_velocity:
            self.vy = terminal_velocity

class AnimatedEntity(Entity):

    def __init__(self, x, y, images):
        super().__init__(x,y,images[0])

        self.images = images
        self.image_index = 0
        self.ticks = 0
        self.animation_speed = 10

    def set_image_list(self):
        self.images = self.images

    def animate(self):
        self.set_image_list()
        self.ticks +=1

        if self.ticks % self.animation_speed == 0:
            self.image_index += 1

            if self.image_index >= len(self.images):
                self.image_index = 0

            self.image = self.images[self.image_index]
class Hero(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.speed = 5
        self.jump_power = 13
        self.vx = 0
        self.vy = 0

        self.hurt_timer = 0
        self.health = 3
        self.max_hearts = 3
        self.gems = 0
        self.cards = 0
        self.score = 0
        
    def move_to(self,x,y):
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE // 2

        
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
        elif self.rect.right > world_width:
            self.rect.right = world_width

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

    def reached_exit(self):
        return pygame.sprite.spritecollideany(self, goal)

    
    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.check_items()
        self.check_enemies()

            
class Platform(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Exit(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        

class Enemy(AnimatedEntity):
    
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.speed = 2
        self.vx = -1 * self.speed
        self.vy = 0

    def reverse(self):
        self.vx *= -1


    def move_and_check_platforms(self):
        self.rect.x += self.vx

        must_reverse = True

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vx > 0:
                self.rect.right = hit.rect.left
                self.reverse()
            elif self.vx < 0:
                self.rect.left = hit.rect.right
                self.reverse()

        self.rect.y += self.vy

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vy > 0:
                self.rect.bottom = hit.rect.top
            elif self.vy < 0:
                self.rect.top = hit.rect.bottom

            self.vy = 0

        self.rect.y += self.vy
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vy > 5:
                self.rect.bottom = platform.rect.top
            elif self.vy == 5:
                self.rect.top = platform.rect.bottom

            self.vy = 5

    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse()
        elif self.rect.right > world_width:
            self.rect.right = world_width
            self.reverse()

    def check_boxes(self):
        hits = pygame.sprite.spritecollide(self, boxes, True)

        for box in hits:
            if self.vx > 0:
                box.rect.left = self.rect.right
                self.vx = -1 * self.speed
            elif self.vx > 0:
                box.rect.left = self.rect.left
                self.vx = self.speed

    def check_boxes2(self):
        hits = pygame.sprite.spritecollide(self, boxes, True)

        for box in hits:
            if self.vx > 0:
                box.rect.left = self.rect.right
                self.vx = -1 * self.speed
            elif self.vx > 0:
                box.rect.left = self.rect.left
                self.vx = self.speed

    def check_enemies(self):
        hits = pygame.sprite.spritecollide(self, enemies, False)
        hits.remove(self)

        for enemy in hits:
            if self.vx > 0:
                self.rect.right = enemy.rect.left
                self.vx = -1 * self.speed
            elif self.vx < 0:
                self.rect.right = enemy.rect.right
                self.vx = self.speed                

    def check_platform_edges(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2

        must_reverse = True

        for platform in hits:
            if self.vx < 0 and platform.rect.left <= self.rect.left:
                must_reverse = False
            elif self.vx > 0 and platform.rect.right >= self.rect.right:
                must_reverse = False

        if must_reverse:
            self.reverse()
                        
        
class Blade(Enemy):

    def __init__(self, x, y, images): 
        super().__init__(x, y, images)

    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()

class Bee(Enemy):

    def __init__(self, x, y, images):
        super().__init__(x, y, images)
        self.animation_speed = 8

    def set_image_list(self):
        if self.vx > 0:
            self.images = bee_imgs_lt
        else:
            self.images = bee_imgs_rt

    def update(self):
        self.move_and_check_platforms()
        self.check_world_edges()
        self.animate()


class Gem(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        

    def apply(self, character):
        character.gems += 1
        character.score += 10
        print(character.gems)
        print(character.score)

class Card(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        

    def apply(self, character):
        character.cards += 1
        character.score += 1000
        print(str(character.cards) + ' Card get!')
        print(character.score)


            

# Helper functoins

def show_start_screen():
    text = font_xl.render(TITLE, True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('press any key to start', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2 + 50
    screen.blit(text, rect)

def show_lose_screen():
    text = font_xl.render('GAME OVER', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('press \'r\' to restart', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2 + 50
    screen.blit(text, rect)

def show_win_screen():
    text = font_xl.render('YOU WIN', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('press \'r\' to restart', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2 + 50
    screen.blit(text, rect)

def show_level_complete_screen():
    text = font_xl.render('Level Complete', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('press any key to continue', True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2 + 50
    screen.blit(text, rect)
    

def show_hud():
    text = font_md.render(str(hero.score), True, WHITE)
    rect = text.get_rect()
    rect.topright = WIDTH // 2, HEIGHT - 44
    screen.blit(text, rect)

    screen.blit(gem_img, (WIDTH - 2 * GRID_SIZE - 48, HEIGHT - 1 * GRID_SIZE))
    text = font_sm.render('x' + str(hero.gems), True, WHITE)
    rect.topleft = WIDTH - 120, HEIGHT - 44
    screen.blit(text, rect)

    for i in range(hero.max_hearts):
        x = i * 36
        y = HEIGHT - 1 * GRID_SIZE
        if i < hero.health:
            screen.blit(heartf_img,(x, y))
        else:
            screen.blit(hearte_img,(x, y))
    
def draw_grid(offset_x=0, offset_y=0):
    for x in range(0, WIDTH + GRID_SIZE, GRID_SIZE):
        adj_x = x - offset_x % GRID_SIZE
        pygame.draw.line(screen, GRAY, [adj_x, 0], [adj_x, HEIGHT], 1)

    for y in range(0, HEIGHT + GRID_SIZE, GRID_SIZE):
        adj_y = y - offset_y % GRID_SIZE
        pygame.draw.line(screen, GRAY, [0, adj_y], [WIDTH, adj_y], 1)

    for x in range(0, WIDTH + GRID_SIZE, GRID_SIZE):
        for y in range(0, HEIGHT + GRID_SIZE, GRID_SIZE):
            adj_x = x - offset_x % GRID_SIZE + 4
            adj_y = y - offset_y % GRID_SIZE + 4
            disp_x = x // GRID_SIZE + offset_x // GRID_SIZE
            disp_y = y // GRID_SIZE + offset_y // GRID_SIZE
            
            point = '(' + str(disp_x) + ',' + str(disp_y) + ')'
            text = font_xs.render(point, True, GRAY)
            screen.blit(text, [adj_x, adj_y])


# Setup

def start_game():
    global hero,stage,current_level
    
    hero = Hero(0,0, knight_img)
    stage = START
    current_level = 0


def start_level():
    global player,platforms,foreground,items,enemies,hero,goal,all_sprites,background
    global world_width,world_height

    
    player = pygame.sprite.GroupSingle()
    platforms = pygame.sprite.Group()
    background = pygame.sprite.Group()
    foreground = pygame.sprite.Group()
    items = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    goal = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    with open (levels[current_level]) as f:
        data = json.load(f)

    world_width = data['width'] * GRID_SIZE
    world_height = data['height'] * GRID_SIZE

    hero.move_to(data['start'][0],data['start'][1])
    player.add(hero)


    goal.add(Exit(data['exitsingle_loc'][0], data['exitsingle_loc'][1], exits_img))
    
    for i, loc in enumerate(data['exitdouble_locs']):
        if i == 0:
            goal.add(Exit(loc[0], loc[1], exitb_img))
        else:
            goal.add(Exit(loc[0], loc[1], exitt_img))
            

    for loc in data['card_locs']:
        items.add(Card(loc[0], loc[1], card2_img))

    for loc in data['grass_locs']:
        platforms.add(Platform(loc[0], loc[1], grass_dirt_img))

    for loc in data['platform_locs']:
        platforms.add(Platform(loc[0], loc[1], platform_img))
        
    for loc in data['wall_locs']:
        platforms.add(Platform(loc[0], loc[1], wall_img))

    for loc in data['backwall_locs']:
        background.add(Platform(loc[0], loc[1], backwalls_img))
        
    for loc in data['bannerendr_locs']:
        background.add(Platform(loc[0], loc[1], bannerendr_img))

    for loc in data['bannerendl_locs']:
        background.add(Platform(loc[0], loc[1], bannerendl_img))

    for loc in data['banner_locs']:
        background.add(Platform(loc[0], loc[1], banner_img))

    for loc in data['wallbanner_locs']:
        background.add(Platform(loc[0], loc[1], wallbanner_img))
     
    for loc in data['castletop_locs']:
        platforms.add(Platform(loc[0], loc[1], castlet_img))
        
    for loc in data['castletl_locs']:
        platforms.add(Platform(loc[0], loc[1], castletl_img))
        
    for loc in data['castletr_locs']:
        platforms.add(Platform(loc[0], loc[1], castletr_img))

    for loc in data['bush_locs']:
        foreground.add(Platform(loc[0], loc[1], bush_img))

    for loc in data['fakep_locs']:
        foreground.add(Platform(loc[0], loc[1], platform_img))

    for loc in data['gem_locs']:
        items.add(Gem(loc[0], loc[1], gem_img))

    for loc in data['bee_locs']:
        enemies.add(Bee(loc[0], loc[1], bee_imgs_lt))

    for loc in data['blade_locs']:
        enemies.add(Blade(loc[0], loc[1], enemy_imgs))

    all_sprites.add(background,player,items,enemies,platforms,foreground,goal)

# Physics settings
gravity = 0.5
terminal_velocity = 63

# Game loop
grid_on = False
running = True

start_game()
start_level()

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                grid_on = not grid_on
                
            elif stage == START:
                stage = PLAYING

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    hero.jump()

            elif stage == LOSE or stage == WIN:
                if event.key == pygame.K_r:
                    start_game()
                    start_level()

                

    pressed = pygame.key.get_pressed()

    if stage == PLAYING:
        if pressed[pygame.K_a]:
            hero.move_left()
        elif pressed[pygame.K_d]:
            hero.move_right()
        else:
            hero.stop()

    
    # Game logic
    if stage == PLAYING:
        all_sprites.update()

        if hero.health == 0:
            stage = LOSE
        elif hero.reached_exit():
            stage = LEVEL_COMPLETE
            countdown = 2 * FPS
    elif stage == LEVEL_COMPLETE:
        countdown -= 1
        if countdown <= 0:
            current_level += 1

            if current_level < len(levels):  
                start_level()
                stage = PLAYING
            else:
                stage = WIN

        
    if hero.rect.centerx < WIDTH - 14 * GRID_SIZE:
        offset_x = 0
    elif hero.rect.centerx > world_width - 14 * GRID_SIZE:
        offset_x = world_width - WIDTH
    else:
        offset_x = hero.rect.centerx - 10 * GRID_SIZE
            
    # Drawing code
    screen.fill(SKY_BLUE)

    for sprite in all_sprites:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y])

    show_hud()

    if stage == START:
        show_start_screen()
    elif stage == LOSE:
        show_lose_screen()
    elif stage == LEVEL_COMPLETE:
        show_level_complete_screen()
    elif stage == WIN:
        show_win_screen()
        
    if grid_on:
        draw_grid(offset_x)
        
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()

