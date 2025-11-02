import pygame


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("インベーダーゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

        self.playerMove = 10
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    
    def moveLeft(self):
        if 0 <= self.x - self.playerMove:
            self.x -= self.playerMove
    
    def moveRight(self):
        if self.x + self.playerMove <= WINDOW_WIDTH - self.width:
            self.x += self.playerMove

player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT - 50)


running = True

while running:
    display_surface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.moveLeft()
    
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    
    player.draw(display_surface)

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()
