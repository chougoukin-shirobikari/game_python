import pygame


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

player = Player(10, 50, WHITE)

player_up = False
player_down = False
player_right = False
player_left = False


print(player.x, player.y, player.color, player.width, player.height)

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
        print(dy, dx)
            
    player.draw()
            

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()