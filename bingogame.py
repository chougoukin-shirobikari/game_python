import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ビンゴゲーム")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
LemonChiffon = (255, 250, 205)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Bingo():
    def __init__(self):
        pygame.draw.rect(display_surface, WHITE, (10, 150, 390, 390), 1)
        pygame.draw.rect(display_surface, WHITE, (425, 200, 150, 150), 1)
        pygame.draw.rect(display_surface, WHITE, (410, 425, 180, 255), 1)
        
        self.number_button = pygame.draw.rect(display_surface, WHITE, (30, WINDOW_HEIGHT - 125, 350, 80), 1)


bingo = Bingo()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()