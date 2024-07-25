import pygame


pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

BALL_RADIOUS = 10

ball_x = 100
ball_y = 100

dx = 5
dy = 5

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ブロック崩し")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(display_surface, WHITE, (ball_x, ball_y), BALL_RADIOUS)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()