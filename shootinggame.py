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

FPS = 100
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
        if dy == -1:
            print('上が押された')
        if dy == 1:
            print('下が押された')
        if dx == 1:
            print('右が押された')
        if dx == -1:
            print('左が押された')

player = Player(10, 50, WHITE)
player.draw()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -1)
            if event.key == pygame.K_DOWN:
                player.move(0, 1)
            if event.key == pygame.K_RIGHT:
                player.move(1, 0)
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()