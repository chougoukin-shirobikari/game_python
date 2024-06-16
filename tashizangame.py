import pygame, random


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("足し算ゲーム")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LemonChiffon = (255, 250, 205)
STEELBLUE = (70, 130, 180)
GOLD = (225, 223, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

def text_board(font, size, text, color, x, y):
    font = pygame.font.Font(font, size)
    textsurf = font.render(text, True, color)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)

text_board('NotoSansJP-Regular.ttf', 50, '足し算ゲーム', WHITE, WINDOW_WIDTH // 2, 50)

class Game():
    CHOICE_X = 25
    CHOICE_Y = 305
    CHOICE_PADDING = 150

    def __init__(self):
        self.lineCreate()

        self.a = random.randrange(1, 5)
        self.b = random.randrange(1, 6)

        self.add()

        self.answer = self.a + self.b

        self.choice_number = []

        self.count = 0
        self.best_count = 0
        self.countTextBoard()

        self.choiceNumber()
    
    def countTextBoard(self):
        text_board('NotoSansJP-Regular.ttf', 30, f'連続正解数：{self.count}', WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100)
        text_board('NotoSansJP-Regular.ttf', 30, f'今回の最高連続正解数：{self.best_count}', WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
    
    def lineCreate(self):
        pygame.draw.rect(display_surface, WHITE, (50, 120, 500, 150), 3)
        pygame.draw.rect(display_surface, WHITE, (25, 305, 100, 150), 3)
        pygame.draw.rect(display_surface, WHITE, (175, 305, 100, 150), 3)
        pygame.draw.rect(display_surface, WHITE, (325, 305, 100, 150), 3)
        pygame.draw.rect(display_surface, WHITE, (475, 305, 100, 150), 3)
    
    def add(self):
        text_board('NotoSansJP-Regular.ttf', 100, f'{self.a} + {self.b}', WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100)

    def choiceNumber(self):
        while len(self.choice_number) < 3:
            temp_number = random.randrange(2, 10)
            if temp_number not in self.choice_number and temp_number != self.answer:
                self.choice_number.append(temp_number)
        
        self.choice_number.insert(random.randrange(4), self.answer)

        for c in range(4):
            text_board('NotoSansJP-Regular.ttf', 100, f'{self.choice_number[c]}', WHITE, (c * self.CHOICE_PADDING) + self.CHOICE_X + 50, self.CHOICE_Y + 70)

game = Game()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('左クリックされた！')
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()