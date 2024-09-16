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

def text_board(font, size, text, color, x, y):
    font = pygame.font.SysFont(font, size)
    textsurf = font.render(text, True, color)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)

text_board('meiryo', 50, "なにを選びますか？", WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()