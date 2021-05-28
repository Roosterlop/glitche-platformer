# Imports
import pygame
import random
import json

# Window settings
GRID_SIZE = 64
WIDTH = 24 * GRID_SIZE
HEIGHT = 15 * GRID_SIZE
TITLE = "Glitche"
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
knight_idle_imgs_rt = [pygame.image.load('assets/images/characters/knight/knightidle1.png').convert_alpha(),
                       pygame.image.load('assets/images/characters/knight/knightidle2.png').convert_alpha()]

knight_walk_imgs_rt = [pygame.image.load('assets/images/characters/knight/knightwf1.png').convert_alpha(),
                       pygame.image.load('assets/images/characters/knight/knightwf2.png').convert_alpha()]

knight_jump_imgs_rt = [pygame.image.load('assets/images/characters/knight/knightjumpf.png').convert_alpha()]

knight_idle_imgs_lt = [pygame.transform.flip(img, True, False) for img in knight_idle_imgs_rt]

knight_walk_imgs_lt = [pygame.transform.flip(img, True, False) for img in knight_walk_imgs_rt]

knight_jump_imgs_lt = [pygame.transform.flip(img, True, False) for img in knight_jump_imgs_rt]
# Blocks
    #castle
wallbanner_img = pygame.image.load('assets/images/tiles/wallbanner.png').convert_alpha()
banner_img = pygame.image.load('assets/images/tiles/banner.png').convert_alpha()
bannerendl_img = pygame.image.load('assets/images/tiles/bannerendl.png').convert_alpha()
bannerendr_img = pygame.image.load('assets/images/tiles/bannerendr.png').convert_alpha()
backwall_img = pygame.image.load('assets/images/tiles/castleback.png').convert_alpha()
wall_img = pygame.image.load('assets/images/tiles/walls.png').convert_alpha()
castletl_img = pygame.image.load('assets/images/tiles/castletl.png').convert_alpha()
castlet_img = pygame.image.load('assets/images/tiles/castlet.png').convert_alpha()
castletr_img = pygame.image.load('assets/images/tiles/castletr.png').convert_alpha()
casin_img = pygame.image.load('assets/images/tiles/casin.png').convert_alpha()
casinl_img = pygame.image.load('assets/images/tiles/casinl.png').convert_alpha()
casinr_img = pygame.image.load('assets/images/tiles/casinr.png').convert_alpha()
casf_img = pygame.image.load('assets/images/tiles/castleflooring.png').convert_alpha()
casfl_img = pygame.image.load('assets/images/tiles/castleflooringl.png').convert_alpha()
casfr_img = pygame.image.load('assets/images/tiles/castleflooringr.png').convert_alpha()

grass_dirt_img = pygame.image.load('assets/images/tiles/grass_dirt.png').convert_alpha()
stone_img = pygame.image.load('assets/images/tiles/stone.png').convert_alpha()
platform_img = pygame.image.load('assets/images/tiles/block.png').convert_alpha()

doorwayt_img = pygame.image.load('assets/images/tiles/open_doort.png').convert_alpha()
doorwayl_img = pygame.image.load('assets/images/tiles/open_doorl.png').convert_alpha()

exits_img = pygame.image.load('assets/images/tiles/exits.png').convert_alpha()
exitt_img = pygame.image.load('assets/images/tiles/exitt.png').convert_alpha()
exitb_img = pygame.image.load('assets/images/tiles/exitb.png').convert_alpha()

#Enemy images
enemy_imgs = [pygame.image.load('assets/images/characters/enemy1a.png').convert_alpha(),
              pygame.image.load('assets/images/characters/enemy1b.png').convert_alpha()]


slime_imgs_rt = [pygame.image.load('assets/images/characters/enemies/slimeGreen.png').convert_alpha(),
              pygame.image.load('assets/images/characters/enemies/slimeGreen_walk.png').convert_alpha()]
slime_imgs_lt = [pygame.transform.flip(img, True, False) for img in slime_imgs_rt]


ghost_imgs_rt = [pygame.image.load('assets/images/characters/enemies/ghost.png').convert_alpha()]
ghost_imgs_lt = [pygame.transform.flip(img, True, False) for img in ghost_imgs_rt]

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
jump_snd = pygame.mixer.Sound('assets/sounds/jump.ogg')
hit_snd = pygame.mixer.Sound('assets/sounds/hit.ogg')
collectg_snd = pygame.mixer.Sound('assets/sounds/collect.ogg')
collectc_snd = pygame.mixer.Sound('assets/sounds/card_collect.ogg')
win_snd = pygame.mixer.Sound('assets/sounds/win.ogg')
level_end_snd = pygame.mixer.Sound('assets/sounds/level_complete.ogg')

#music
start_music = ['assets/music/titlemusic1.ogg', 'assets/music/titlemusic2.ogg']
play_music = ['assets/music/thememusic1.ogg','assets/music/thememusic2.ogg',
              'assets/music/thememusic3.ogg','assets/music/thememusic4.ogg',
              'assets/music/thememusic5.ogg','assets/music/thememusic6.ogg']

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
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE // 2

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
class Hero(AnimatedEntity):
    
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.speed = 5
        self.jump_power = 13
        self.vx = 0
        self.vy = 0
        self.facing_right = True
        self.jumping = False

        self.hurt_timer = 0
        self.health = 50
        self.max_hearts = 50
        self.gems = 0
        self.cards = 0
        self.score = 0
        
    def move_to(self,x,y):
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE // 2

        
    def move_right(self):
    	self.vx = self.speed
    	self.facing_right = True
    	
    def move_left(self):
    	self.vx = -self.speed
    	self.facing_right = False

    def stop(self):
        self.vx = 0
    
    def jump(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2

        if len(hits) > 0:
            self.vy -= self.jump_power
            self.jumping = True
            jump_snd.play()


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
                self.jumping = False
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
                hit_snd.play()
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

    def set_image_list(self):
        if self.facing_right:
            if self.jumping:
                self.images = knight_jump_imgs_rt
            elif self.vx == 0:
                self.images = knight_idle_imgs_rt
            else:
                self.images = knight_walk_imgs_rt
        else:
            if self.jumping:
                self.images = knight_jump_imgs_lt
            elif self.vx == 0:
                self.images = knight_idle_imgs_lt
            else:
                self.images = knight_walk_imgs_lt

    
    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.check_items()
        self.check_enemies()
        self.animate()

            
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

    def move(self):
        self.rect.x += self.vx
        
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
        self.speed = 4
        self.vx = -1 * self.speed

    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()

class Slime(Enemy):

    def __init__(self, x, y, images): 
        super().__init__(x, y, images)
        self.animation_speed = 15
        self.speed = 1
        self.vx = 1 * self.speed


    def set_image_list(self):
        if self.vx > 0:
            self.images = slime_imgs_lt
        else:
            self.images = slime_imgs_rt

    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.animate()

class Ghost(Enemy):

    def __init__(self, x, y, images): 
        super().__init__(x, y, images)
        self.speed = 3
        self.vx = -1 * self.speed

    def set_image_list(self):
        if self.vx > 0:
            self.images = ghost_imgs_lt
        else:
            self.images = ghost_imgs_rt

    def update(self):
        self.check_world_edges()
        self.move()
        
class Bee(Enemy):

    def __init__(self, x, y, images):
        super().__init__(x, y, images)
        self.animation_speed = 8
        self.speed = 6
        self.vx = -1 * self.speed

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
        collectg_snd.play()
        print(character.gems)
        print(character.score)

class Card(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        

    def apply(self, character):
        character.cards += 1
        character.score += 1000
        collectc_snd.play()
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

    text = font_sm.render('card collection ' + str(hero.cards) + "/5", True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2 + 100
    screen.blit(text, rect)
    
    text = font_sm.render('score ' + str(hero.score), True, WHITE)
    rect = text.get_rect()
    rect.center = WIDTH // 2, HEIGHT // 2 + 150
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
    
    hero = Hero(0,0, knight_idle_imgs_rt)
    stage = START
    current_level = 0

def play_random_track(tracks):
    song = random.choice(tracks)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)

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
        items.add(Card(loc[0], loc[1], carda_img))

    for loc in data['grass_locs']:
        platforms.add(Platform(loc[0], loc[1], grass_dirt_img))

    for loc in data['stone_locs']:
        platforms.add(Platform(loc[0], loc[1], stone_img))

    for loc in data['platform_locs']:
        platforms.add(Platform(loc[0], loc[1], platform_img))
        
    for loc in data['wall_locs']:
        platforms.add(Platform(loc[0], loc[1], wall_img))

    for loc in data['backwall_locs']:
        background.add(Platform(loc[0], loc[1], backwall_img))

    for loc in data['casf_locs']:
        platforms.add(Platform(loc[0], loc[1], casf_img))

    for loc in data['casfl_locs']:
        platforms.add(Platform(loc[0], loc[1], casfl_img))

    for loc in data['casfr_locs']:
        platforms.add(Platform(loc[0], loc[1], casfr_img))

    for loc in data['casin_locs']:
        background.add(Platform(loc[0], loc[1], casin_img))
        
    for loc in data['casinl_locs']:
        background.add(Platform(loc[0], loc[1], casinl_img))

    for loc in data['casinr_locs']:
        background.add(Platform(loc[0], loc[1], casinr_img))
        
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

    for loc in data['fakes_locs']:
        foreground.add(Platform(loc[0], loc[1], stone_img))

    for loc in data['gem_locs']:
        items.add(Gem(loc[0], loc[1], gem_img))

    for loc in data['bee_locs']:
        enemies.add(Bee(loc[0], loc[1], bee_imgs_lt))

    for loc in data['blade_locs']:
        enemies.add(Blade(loc[0], loc[1], enemy_imgs))

    for loc in data['slime_locs']:
        enemies.add(Slime(loc[0], loc[1], slime_imgs_lt))

    for loc in data['ghost_locs']:
        enemies.add(Ghost(loc[0], loc[1], ghost_imgs_lt))



    all_sprites.add(background,player,items,platforms,enemies,foreground,goal)

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
            level_end_snd.play()
    elif stage == LEVEL_COMPLETE:
        countdown -= 1
        if countdown <= 0:
            current_level += 1

            if current_level < len(levels):  
                start_level()
                stage = PLAYING
            else:
                hero.score += hero.health * 3000
                win_snd.play()
                stage = WIN

        
    if hero.rect.centerx < WIDTH - 14 * GRID_SIZE:
        offset_x = 0
    elif hero.rect.centerx > world_width - 14 * GRID_SIZE:
        offset_x = world_width - WIDTH
    else:
        offset_x = hero.rect.centerx - 10 * GRID_SIZE

    music_on = pygame.mixer.music.get_busy()
    if not music_on:
        if stage == START:
            play_random_track(start_music)
        elif stage == PLAYING:
            play_random_track(play_music)
         
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

