import pygame, random
from quizResource import quiz


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("クイズゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Game():
    def __init__(self, x, y, width=WINDOW_WIDTH - 100, height=80):
        self.x = x
        self.y = y

        self.color = WHITE
        self.width = width
        self.height = height
        self.line = 1

        self.questionAnswer = -1
        self.answer1 = self.answer2 = self.answer3 = self.answer4 = self.answerDescription = None
    
    def draw(self):
        pygame.draw.rect(display_surface, self.color, (self.x, self.y, self.width, self.height), self.line)
    
    def theQuestion(self):
        number = 0
        number = random.randrange(len(quiz))

        question, self.answer1, self.answer2, self.answer3, self.answer4, self.questionAnswer, self.answerDescription = quiz[number]
        
        self.text_board('NotoSansJP-Regular.ttf', 30, question, WHITE, None, WINDOW_WIDTH // 2, 100)
        #self.text_board('NotoSansJP-Regular.ttf', 30, self.answer1, WHITE, None, WINDOW_WIDTH // 2, 240)
        #self.text_board('NotoSansJP-Regular.ttf', 30, self.answer2, WHITE, None, WINDOW_WIDTH // 2, 340)
        #self.text_board('NotoSansJP-Regular.ttf', 30, self.answer3, WHITE, None, WINDOW_WIDTH // 2, 440)
        #self.text_board('NotoSansJP-Regular.ttf', 30, self.answer4, WHITE, None, WINDOW_WIDTH // 2, 540)

        self.describeAnswers(WHITE)
    
    def text_board(self, font, size, text, color, bgColor, x, y):
        font = pygame.font.Font(font, size)
        textsurf = font.render(text, True, color, bgColor)
        textsurf_rect = textsurf.get_rect()
        textsurf_rect.center = (x, y)
        display_surface.blit(textsurf, textsurf_rect)
    
    def questionAnswerCheck(self):
        return self.questionAnswer - 1
    
    def describeAnswers(self, color, result=False):
        colors = [color] * 4

        if result:
            colors[self.questionAnswer - 1] = YELLOW

        self.text_board('NotoSansJP-Regular.ttf', 30, self.answer1, colors[0], None, WINDOW_WIDTH // 2, 240)
        self.text_board('NotoSansJP-Regular.ttf', 30, self.answer2, colors[1], None, WINDOW_WIDTH // 2, 340)
        self.text_board('NotoSansJP-Regular.ttf', 30, self.answer3, colors[2], None, WINDOW_WIDTH // 2, 440)
        self.text_board('NotoSansJP-Regular.ttf', 30, self.answer4, colors[3], None, WINDOW_WIDTH // 2, 540)

class Player(Game):
    def __init__(self, x, y):
        super().__init__(x, y)
        
        self.color = YELLOW
        self.answer = 0
        self.answerPosition = [(50, 200), (50, 300), (50, 400), (50, 500)]

    def draw(self):
        self.x, self.y = self.answerPosition[self.answer]
        pygame.draw.rect(display_surface, self.color, (self.x, self.y, self.width, self.height), self.line)
    
    def move(self, answer_choice):
        if answer_choice == -1 and self.answer > 0:
            pygame.draw.rect(display_surface, WHITE, (self.x, self.y, self.width, self.height), self.line)
            self.answer -= 1
        
        elif answer_choice == 1 and self.answer < 3:
            pygame.draw.rect(display_surface, WHITE, (self.x, self.y, self.width, self.height), self.line)
            self.answer += 1
    
    def answerCheck(self):
        return self.answer
        

game = Game(10, 20, WINDOW_WIDTH - 20, 160)
game.draw()
game.theQuestion()

answer1, answer2, answer3, answer4 = Game(50, 200), Game(50, 300), Game(50, 400), Game(50, 500)

answers = [answer1, answer2, answer3, answer4]

[answer.draw() for answer in answers]

player = Player(50, 200)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(-1)
            if event.key == pygame.K_DOWN:
                player.move(1)
            if event.key == pygame.K_SPACE:
                game.describeAnswers(GRAY, player.answerCheck() == game.questionAnswerCheck())

    player.draw()   
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()