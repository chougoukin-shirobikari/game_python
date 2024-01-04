import pygame


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("RGBソフト")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

red_button = pygame.draw.rect(display_surface, WHITE, (50, WINDOW_HEIGHT - 150, 100, 100), 1)
green_button = pygame.draw.rect(display_surface, WHITE, (200, WINDOW_HEIGHT - 150, 100, 100), 1)
blue_button = pygame.draw.rect(display_surface, WHITE, (350, WINDOW_HEIGHT - 150, 100, 100), 1)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()