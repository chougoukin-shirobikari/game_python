import pygame


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
    
    def draw(self):
        pygame.draw.rect(display_surface, self.color, (self.x, self.y, self.width, self.height), self.line)

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

game = Game(10, 20, WINDOW_WIDTH - 20, 160)
game.draw()

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
    
    player.draw()
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()