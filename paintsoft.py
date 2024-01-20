import pygame


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ペイントソフト")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FUCHSIA = (255, 0, 255)
AQUA = (0, 255, 255)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
DIMGRAY = (105, 105, 105)

display_surface.fill(BLACK)

FPS = 100
clock = pygame.time.Clock()

pygame.draw.rect(display_surface, WHITE, (10, WINDOW_HEIGHT - 90, 80, 80), 1)
pygame.draw.rect(display_surface, WHITE, (100, WINDOW_HEIGHT - 90, 300, 80))
pygame.draw.rect(display_surface, DIMGRAY, (10, 10, 390, 390), 1)

clear_display = pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50), 35)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()