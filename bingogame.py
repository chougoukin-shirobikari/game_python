import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ビンゴゲーム")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
        pygame.draw.rect(display_surface, WHITE, (410, 425, 180, 225), 1)

        self.number_button = pygame.draw.rect(display_surface, WHITE, (30, WINDOW_HEIGHT - 125, 350, 80), 1)

        text_board('NotoSansJP-Regular.ttf', 50, 'ビンゴゲーム', YELLOW, None, WINDOW_WIDTH // 2, 50)

def text_board(font, size, text, color, bgColor, x, y):
    font = pygame.font.Font(font, size)
    textsurf = font.render(text, True, color, bgColor)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)

bingo = Bingo()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()