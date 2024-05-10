import pygame, random


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ビンゴゲーム")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
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
        pygame.draw.rect(display_surface, WHITE, (410, 425, 180, 255), 1)
        
        self.number_button = pygame.draw.rect(display_surface, WHITE, (30, WINDOW_HEIGHT - 125, 350, 80), 1)

        text_board('NotoSansJP-Regular.ttf', 50, 'ビンゴゲーム', YELLOW, None, WINDOW_WIDTH // 2, 50)
        text_board('NotoSansJP-Regular.ttf', 30, '番号', SILVER, None, 500, 165)
        text_board('NotoSansJP-Regular.ttf', 30, '出た数字', SILVER, None, 500, 390)
        text_board('NotoSansJP-Regular.ttf', 40, '番号を選ぶ', WHITE, None, 208, WINDOW_HEIGHT - 85)

        self.bingo_display()

    def bingo_display(self):
        bingo_numbers = product_bingo_numbers()
        for y in range(5):
            for x in range(5):
                number = str(bingo_numbers.pop(random.randrange(len(bingo_numbers))))
                rect = pygame.draw.rect(display_surface, WHITE, (20 + 75 * x, 160 + 75 * y, 70, 70), 1)
                if y == x == 2:
                    number = 'Free'
                    pygame.draw.rect(display_surface, LemonChiffon, (rect.x + 1, rect.y + 1, rect.width - 2, rect.height - 2))
                    text_board('NotoSansJP-Regular.ttf', 30, number, GRAY, None, rect.centerx, rect.centery)
                else:
                    text_board('NotoSansJP-Regular.ttf', 30, number, WHITE, None, rect.centerx, rect.centery)

def product_bingo_numbers():
    bingo_numbers = []

    for i in range(1, 76):
        bingo_numbers.append(i)
    
    return bingo_numbers

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