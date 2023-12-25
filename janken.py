import pygame


pygame.init()

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("じゃんけんゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

FPS = 60
clock = pygame.time.Clock()

font = pygame.font.SysFont('meiryo', 50)
textsurf = font.render("なにを選びますか？", True, WHITE)
textsurf_rect = textsurf.get_rect()
textsurf_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150)
display_surface.blit(textsurf, textsurf_rect)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(FPS)

    pygame.display.update()

pygame.quit()