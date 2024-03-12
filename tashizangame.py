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

    CHOICE_WIDTH = 100
    CHOICE_HEIGHT = 150

    LINE_WIDTH = 3

    def __init__(self):
        self.choice1, self.choice2, self.choice3, self.choice4 = self.lineCreate()

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

        return [pygame.draw.rect(display_surface, WHITE, (self.CHOICE_X + self.CHOICE_PADDING * c, self.CHOICE_Y, self.CHOICE_WIDTH, self.CHOICE_HEIGHT), self.LINE_WIDTH) for c in range(4)]
    
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

    def clickCheck(self, playerChoiceIndex):
        if self.answer == self.choice_number[playerChoiceIndex]:
            self.resultSurface(True)
        else:
            self.resultSurface(False)
    
    def resultSurface(self, judge):
        answer_index = self.choice_number.index(self.answer)
        pygame.draw.rect(display_surface, STEELBLUE, ((answer_index * self.CHOICE_PADDING) + self.CHOICE_X, self.CHOICE_Y, self.CHOICE_WIDTH, self.CHOICE_HEIGHT), 3)
        text_board('NotoSansJP-Regular.ttf', 100, f'{self.choice_number[answer_index]}', GOLD, (answer_index * self.CHOICE_PADDING) + self.CHOICE_X + 50, self.CHOICE_Y + 70)
        pygame.draw.rect(display_surface, LemonChiffon, (50, 480, 500, 100))
        text_board('NotoSansJP-Regular.ttf', 100, f'{self.a}+{self.b}={self.answer}', BLACK, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 75)

        if judge:
            pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 75), 125, 25)
            self.count += 1
        else:
            pygame.draw.line(display_surface, RED, (170, 100), (430, 360), 25)
            pygame.draw.line(display_surface, RED, (430, 100), (170, 360), 25)
        
            if self.count > self.best_count:
                self.best_count = self.count
            
            self.count = 0

        continue_check = True

        pygame.display.update()

        while continue_check:
            global running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue_check = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    continue_check = False
                    self.gameContinue()
    
    def gameContinue(self):
        self.a = random.randrange(1, 5)
        self.b = random.randrange(1, 6)

        self.answer = self.a + self.b

        self.choice_number = []

        pygame.draw.rect(display_surface, BLACK, (20, 100, 560, 480))

        self.add()

        self.lineCreate()

        self.countTextBoard()

        self.choiceNumber()


game = Game()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if game.choice1.collidepoint(x, y):
                    game.clickCheck(0)
                if game.choice2.collidepoint(x, y):
                    game.clickCheck(1)
                if game.choice3.collidepoint(x, y):
                    game.clickCheck(2)
                if game.choice4.collidepoint(x, y):
                    game.clickCheck(3)
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()