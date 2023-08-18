import pygame,math


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
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.color = color
        self.width = 50
        self.height = 20

    def draw(self):
        pygame.draw.rect(display_surface, self.color, (self.x, self.y, self.width, self.height))

class Player(Object):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
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

player = Player(10, 50, WHITE)

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
            
    player.draw()

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()