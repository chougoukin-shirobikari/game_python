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

game = Game(10, 20, WINDOW_WIDTH - 20, 160)
game.draw()

answer1, answer2, answer3, answer4 = Game(50, 200), Game(50, 300), Game(50, 400), Game(50, 500)

answers = [answer1, answer2, answer3, answer4]

[answer.draw() for answer in answers]


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()