import pygame


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("タイピングゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Game():
    def __init__(self):
        pygame.draw.rect(display_surface, WHITE, (50, 80, WINDOW_WIDTH - 100, 250), 5)

game = Game()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()