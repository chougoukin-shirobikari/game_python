import pygame, string, random


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

alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase

class Game():
    def __init__(self):
        self.typing_text = []
        self.key_input_index = 0
        self.correct_number = 0
        self.wrong_number = 0

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

        self.score_text_create()

    
    def text_board(self, font, size, text, color):
        font = pygame.font.Font(font, size)
        textsurf = font.render(text, True, color)
        textsurf_rect = textsurf.get_rect()

        return (textsurf, textsurf_rect)
    
    def score_text_create(self):
        pygame.draw.rect(display_surface, BLACK, (self.point_rect.x + self.point_rect.width + 10, self.point_rect.y, 50, 50))
        pygame.draw.rect(display_surface, BLACK, (self.missing_rect.x + self.missing_rect.width + 10, self.missing_rect.y, 50, 50))

        correct, correct_rect = self.text_board('NotoSansJP-Regular.ttf', 25, str(self.correct_number), WHITE)
        wrong, wrong_rect = self.text_board('NotoSansJP-Regular.ttf', 25, str(self.wrong_number), WHITE)

        correct_rect.topleft = (self.point_rect.x + self.point_rect.width + 10, self.point_rect.y)
        wrong_rect.topleft = (self.missing_rect.x + self.missing_rect.width + 10, self.missing_rect.y)

        display_surface.blit(correct, correct_rect)
        display_surface.blit(wrong, wrong_rect)
    
    def input_key_now(self, s):
        pygame.draw.rect(display_surface, BLACK, (480, 365, 80, 80))
        inputKey, inputKey_rect = self.text_board('NotoSansJP-Regular.ttf', 40, s, WHITE)
        inputKey_rect.center = (WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT - 100)
        
        display_surface.blit(inputKey, inputKey_rect)
    
    def alphabet_create(self):
        for _ in range(10):
            i = random.randrange(0, 10)
            if i <= 4:
                self.typing_text.append(random.choice(alphabet_lowercase))
            elif i <= 9:
                self.typing_text.append(random.choice(alphabet_uppercase))
    
    def display_typing_text(self):
        text, text_rect = self.text_board('NotoSansJP-Regular.ttf', 55, ''.join(self.typing_text), WHITE)
        text_rect.center = (WINDOW_WIDTH // 2, 200)

        display_surface.blit(text, text_rect)
    
    def key_input_check(self, key_):
        if self.typing_text[self.key_input_index] == key_:
            self.typing_text[self.key_input_index] = ''
            self.key_input_index += 1

            pygame.draw.rect(display_surface, BLACK, (60, 90, WINDOW_WIDTH - 120, 230))
            self.display_typing_text()

            self.correct_number += 1
        else:
            self.wrong_number += 1
    
    def gameInitCheck(self):
        if self.key_input_index == len(self.typing_text):
            self.key_input_index = 0
            self.typing_text = []
            self.correct_number = self.wrong_number = 0

            self.input_key_now('')
            self.alphabet_create()
            self.display_typing_text()

game = Game()
game.alphabet_create()
game.display_typing_text()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not(97 <= event.key <= 122):
                continue
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                game.input_key_now(pygame.key.name(event.key).upper())
                game.key_input_check(pygame.key.name(event.key).upper())
            else:
                game.input_key_now(pygame.key.name(event.key))
                game.key_input_check(pygame.key.name(event.key))
            
            game.gameInitCheck()
            
            game.score_text_create()
    
    pygame.display.update()
        
    clock.tick(FPS)

pygame.quit()