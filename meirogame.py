import pygame, random
from mazeResource import maze_list


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("迷路")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LemonChiffon = (255, 250, 205)
BROWN = (165, 42, 42)
STEELBLUE = (70, 130, 180)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

def text_board(font, size, text, color, bgColor, x, y):
    font = pygame.font.Font(font, size)
    textsurf = font.render(text, True, color, bgColor)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)

class Maze():
    def __init__(self):
        self.x = 70
        self.y = 100
        
        self.createMaze()
    
    def createMaze(self):
        text_board('NotoSansJP-Regular.ttf', 50, '迷路', WHITE, None, WINDOW_WIDTH // 2, 50)

        choosed_maze = random.choice(maze_list)

        for y in range(15):
            for x in range(15):
                if choosed_maze[y][x] == 'o':
                    pygame.draw.rect(display_surface, WHITE, (self.x + 30 * x, self.y + 30 * y, 30, 30))
                elif choosed_maze[y][x] == 'x':
                    pygame.draw.rect(display_surface, GRAY, (self.x + 30 * x, self.y + 30 * y, 30, 30))
                elif choosed_maze[y][x] == 'G':
                    pygame.draw.rect(display_surface, RED, (self.x + 30 * x, self.y + 30 * y, 30, 30))
                elif choosed_maze[y][x] == 'Y':
                    pygame.draw.rect(display_surface, YELLOW, (self.x + 30 * x, self.y + 30 * y, 30, 30))
                elif choosed_maze[y][x] == 'B':
                    pygame.draw.rect(display_surface, BROWN, (self.x + 30 * x, self.y + 30 * y, 30, 30))


maze = Maze()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()