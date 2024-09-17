import pygame


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("タイピングゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Game():
    def __init__(self):
        pygame.draw.rect(display_surface, WHITE, (50, 80, WINDOW_WIDTH - 100, 250), 5)

        self.point, self.point_rect = self.text_board('NotoSansJP-Regular.ttf', 25, "正解した文字数：", WHITE)
        self.missing, self.missing_rect = self.text_board('NotoSansJP-Regular.ttf', 25, "間違えた文字数：", WHITE)
        self.key_input, self.key_input_rect = self.text_board('NotoSansJP-Regular.ttf', 40, "入力されたキー：", WHITE)

        self.point_rect.center = (WINDOW_WIDTH // 2 - 200, 30)
        self.missing_rect.center = (WINDOW_WIDTH // 2 + 150, 30)
        self.key_input_rect.center = (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100)

        display_surface.blit(self.point, self.point_rect)
        display_surface.blit(self.missing, self.missing_rect)
        display_surface.blit(self.key_input, self.key_input_rect)

    def text_board(self, font, size, text, color):
        font = pygame.font.Font(font, size)
        textsurf = font.render(text, True, color)
        textsurf_rect = textsurf.get_rect()

        return (textsurf, textsurf_rect)

game = Game()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()