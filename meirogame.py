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

        self.wall = []
        self.gate = []
        self.key = []
        self.goal = None
        
        self.createMaze()
    
    def createMaze(self):
        text_board('NotoSansJP-Regular.ttf', 50, '迷路', WHITE, None, WINDOW_WIDTH // 2, 50)

        choosed_maze = random.choice(maze_list)

        for y in range(15):
            for x in range(15):
                if choosed_maze[y][x] == 'o':
                    pygame.draw.rect(display_surface, WHITE, (self.x + 30 * x, self.y + 30 * y, 30, 30))
                elif choosed_maze[y][x] == 'x':
                    self.wall.append(pygame.draw.rect(display_surface, GRAY, (self.x + 30 * x, self.y + 30 * y, 30, 30)))
                elif choosed_maze[y][x] == 'G':
                    self.goal = pygame.draw.rect(display_surface, RED, (self.x + 30 * x, self.y + 30 * y, 30, 30))
                    text_board('NotoSansJP-Regular.ttf', 10, 'ゴール', BLACK, None, self.x + 30 * x + 15, self.y + 30 * y + 15)
                elif choosed_maze[y][x] == 'Y':
                    self.key.append(pygame.draw.rect(display_surface, YELLOW, (self.x + 30 * x, self.y + 30 * y, 30, 30)))
                    text_board('NotoSansJP-Regular.ttf', 10, '鍵', BLACK, None, self.x + 30 * x + 15, self.y + 30 * y + 15)
                elif choosed_maze[y][x] == 'B':
                    self.gate.append(pygame.draw.rect(display_surface, BROWN, (self.x + 30 * x, self.y + 30 * y, 30, 30)))
                    text_board('NotoSansJP-Regular.ttf', 10, '門', BLACK, None, self.x + 30 * x + 15, self.y + 30 * y + 15)

class Player():
    def __init__(self, maze):
        self.maze = maze
        self.x = self.maze.x + 30
        self.y = self.maze.y + 30

        self.player_key = 0
        self.goal_check = 0

        self.player = pygame.draw.rect(display_surface, STEELBLUE, (self.x, self.y, 30, 30))
    
    def draw(self, x, y):
        delete_map = []

        for w in self.maze.wall:
            if w.collidepoint(self.x + x, self.y + y):
                return
        
        for k in self.maze.key:
            if k.collidepoint(self.x + x, self.y + y):
                self.player_key += 1
                delete_map.append(k)
        
        for g in self.maze.gate:
            if g.collidepoint(self.x + x, self.y + y) and self.player_key == 0:
                return
            elif g.collidepoint(self.x + x, self.y + y) and self.player_key > 0:
                self.player_key -= 1
                delete_map.append(g)
        
        if self.maze.goal.collidepoint(self.x + x, self.y + y):
            print('goal')
            self.goal_check = True

        self.player = pygame.draw.rect(display_surface, WHITE, (self.x, self.y, 30, 30))
        
        self.x += x
        self.y += y
        self.player = pygame.draw.rect(display_surface, STEELBLUE, (self.x, self.y, 30, 30))

        for d in delete_map:
            if d in self.maze.key:
                self.maze.key.pop(self.maze.key.index(d))
            if d in self.maze.gate:
                self.maze.gate.pop(self.maze.gate.index(d))
        
    def playerGoalCheck(self):
        return self.goal_check
    
    def playerGoal(self):
        while self.goal_check:
            global running
            text_board('NotoSansJP-Regular.ttf', 55, '迷路をクリア！', BLACK, LemonChiffon, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
            text_board('NotoSansJP-Regular.ttf', 35, 'もう一度プレイ：スペースキーを押す', BLACK, LemonChiffon, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.goal_check = False
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    display_surface.fill(BLACK)
                    self.goal_check = False


maze = Maze()

player = Player(maze)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.draw(0, -30)
            if event.key == pygame.K_DOWN:
                player.draw(0, 30)
            if event.key == pygame.K_RIGHT:
                player.draw(30, 0)
            if event.key == pygame.K_LEFT:
                player.draw(-30, 0)
        
        if player.playerGoalCheck():
            player.playerGoal()

            maze = None
            player = None
            
            maze = Maze()
            player = Player(maze)
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()