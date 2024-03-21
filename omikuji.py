import pygame


pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("おみくじ")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (116, 80, 48)
DARK_BROWN = (78, 53, 36)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

button = pygame.Rect(100, 200, 200, 300)
button_cover = pygame.Rect(110, 210, 180, 280)

font = pygame.font.SysFont('hg丸ｺﾞｼｯｸmpro', 30)
text = font.render("おみくじ", True, WHITE)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                print('click')
    
    pygame.draw.rect(display_surface, BROWN, button)
    pygame.draw.rect(display_surface, DARK_BROWN, button_cover)

    display_surface.blit(text, (140, 300))

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()