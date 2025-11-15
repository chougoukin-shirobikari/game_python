import pygame, math, gc, random


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("横スクロールシューティングゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Object():
    def __init__(self, x, y, color, type):
        self.x = x
        self.y = y
        self.color = color
        self.type = type
        self.width = 50
        self.height = 20
    
    def draw(self):
        if self.type == 0:
            pygame.draw.rect(display_surface, self.color, (self.x, self.y, self.width, self.height))
        elif self.type == 1:
            pygame.draw.circle(display_surface, self.color, (self.x, self.y), self.shotSize)

class Player(Object):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, type)

        self.shotList = []
    
    def shotCheck(self):
        temp = []
        delete_temp = []

        for i in range(len(self.shotList)):
            if self.shotList[i].shotUpdate():
                temp.append(self.shotList[i])
            else:
                delete_temp.append(self.shotList[i])
        
        self.shotList = temp
        del delete_temp

        gc.collect()
    
    def move(self, dx, dy):
        self.x += dx * 8
        self.y += dy * 8

        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)
        
        if 0 >= self.x + dx:
            self.x = 0
        elif self.x + dx >= WINDOW_WIDTH - self.width:
            self.x = WINDOW_WIDTH - self.width
        else:
            self.x += dx
        
        if 0 >= self.y + dy:
            self.y = 0
        elif self.y + dy >= WINDOW_HEIGHT - self.height:
            self.y = WINDOW_HEIGHT - self.height
        else:
            self.y += dy
    
    def shot(self):
        self.shotList.append(Shot(self.x + self.width + 5, self.y + self.height // 2, WHITE, 1, 5, 10))

class Shot(Object):
    def __init__(self, x, y, color, type, shotSize, shotSpeed):
        super().__init__(x, y, color, type)

        self.shotSize = shotSize
        self.shotSpeed = shotSpeed
    
    def shotUpdate(self):
        super().draw()

        if 0 < self.x + self.shotSpeed < WINDOW_WIDTH:
            self.x += self.shotSpeed
            return self
        else:
            return False

class Enemy(Object):
    def __init__(self, x, y, color, type, enemy_type):
        super().__init__(x, y, color, type)

        self.enemy_type = enemy_type
        self.moveSpeed = [1, 2, 3][enemy_type]
        self.shotSpeed = [-5, -8, -10][enemy_type]
        self.shot = None
    
    def move(self):
        if self.x - self.moveSpeed >= -self.width:
            self.x -= self.moveSpeed
            return self
        else:
            return False
    
    def shotOn(self):
        if self.shot is None:
            self.shot = Shot(self.x - 5, self.y + self.height // 2, self.color, 1, 5, self.shotSpeed)
    
    def shotCheck(self):
        if self.shot:
            if not self.shot.shotUpdate():
                self.shot = None

player = Player(10, 50, WHITE, 0)

enemy_event = pygame.USEREVENT + 0
pygame.time.set_timer(enemy_event, 3000)

enemy_shot_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_shot_event, 2000)

enemy_list = []

def enemy_move_check(e_list):
    temp = []
    delete_temp = []

    for i in range(len(e_list)):
        if e_list[i].move():
            temp.append(e_list[i])
        else:
            delete_temp.append(e_list[i])
    
    e_list = temp
    del delete_temp

    gc.collect()

    return e_list

player_up = False
player_down = False
player_right = False
player_left = False


running = True

while running:
    display_surface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.shot()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_up = True
            if event.key == pygame.K_DOWN:
                player_down = True
            if event.key == pygame.K_RIGHT:
                player_right = True
            if event.key == pygame.K_LEFT:
                player_left = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_up = False
            if event.key == pygame.K_DOWN:
                player_down = False
            if event.key == pygame.K_RIGHT:
                player_right = False
            if event.key == pygame.K_LEFT:
                player_left = False
        
        if event.type == enemy_event:
            enemy_type = random.randrange(3)
            enemy_list.append(Enemy(WINDOW_WIDTH, random.randrange(0, WINDOW_HEIGHT - 20), [RED, GREEN, BLUE][enemy_type], 0, enemy_type))

        if event.type == enemy_shot_event:
            for e in enemy_list:
                e.shotOn()

    [e.draw() for e in enemy_list]

    [e.move() for e in enemy_list]

    [e.shotCheck() for e in enemy_list]

    enemy_list = enemy_move_check(enemy_list)

    dx = 0
    dy = 0

    if player_up:
        dy = -1
    if player_down:
        dy = 1
    if player_right:
        dx = 1
    if player_left:
        dx = -1
    
    player.move(dx, dy)

    player.shotCheck()
    
    player.draw()

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()
