import pygame

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("おみくじ")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

button = pygame.Rect(100, 100, 200, 300)

font = pygame.font.SysFont('hg丸ｺﾞｼｯｸmpro', 80)

text = font.render("おみくじ", True, WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(display_surface, WHITE, button)

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()