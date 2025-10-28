import pygame


pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

BALL_RADIUS = 10

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
    display_surface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(display_surface, WHITE, (ball_x, ball_y), BALL_RADIUS)

    if not (BALL_RADIUS <= ball_x + dx <= WINDOW_WIDTH - BALL_RADIUS):
        dx = -dx
    
    if not (BALL_RADIUS <= ball_y + dy <= WINDOW_HEIGHT - BALL_RADIUS):
        dy = -dy

    ball_x += dx
    ball_y += dy

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
