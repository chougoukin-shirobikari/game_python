import pygame


pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

BALL_RADIUS = 10
ball_x = WINDOW_WIDTH // 2 + BALL_RADIUS
ball_y = WINDOW_HEIGHT - 50

dx = 5
dy = -5

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ブロック崩し")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

BOARD_WIDTH = 80
BOARD_HEIGHT = 15
BOARD_MOVE = 5

board_x = WINDOW_WIDTH // 2
board_y = WINDOW_HEIGHT - BOARD_HEIGHT

def board_display():
    pygame.draw.rect(display_surface, WHITE, (board_x, board_y, BOARD_WIDTH, BOARD_HEIGHT))

BLOCK_WIDTH = 60
BLOCK_HEIGHT = 25
BLOCK_PADDING = 10
BLOCK_DRAW_X = 30
BLOCK_DRAW_Y = 10

block = []

for y in range(5):
    block_x = []
    for x in range(5):
        block_x.append([BLOCK_DRAW_X + (BLOCK_PADDING + BLOCK_WIDTH) * x, BLOCK_DRAW_Y + (BLOCK_PADDING + BLOCK_HEIGHT) * y, BLOCK_WIDTH, BLOCK_HEIGHT, True])
    block.append(block_x)

def block_display():
    for y in range(5):
        for x in range(5):
            block_true = block[y][x][-1]
            if block_true:
                block_x = block[y][x][0]
                block_y = block[y][x][1]
                block_width = block[y][x][2]
                block_height = block[y][x][3]
                pygame.draw.rect(display_surface, WHITE, (block_x, block_y, block_width, block_height))

def block_collision_check():
    global dy

    for y in range(5):
        for x in range(5):
            block_x = block[y][x][0]
            block_y = block[y][x][1]
            block_width = block[y][x][2]
            block_height = block[y][x][3]
            block_true = block[y][x][4]

            if block_true:
                if block_x <= ball_x + dx <= block_x + block_width and block_y <= ball_y + dy <= block_y + block_height:
                    dy = -dy
                    block[y][x][4] = False

def board_collision_check():
    global dy

    if board_x <= ball_x + dx <= board_x + BOARD_WIDTH and ball_y + dy >= WINDOW_HEIGHT - BOARD_HEIGHT:
        dy = -dy


running = True

while running:
    display_surface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(display_surface, WHITE, (ball_x, ball_y), BALL_RADIUS)

    block_display()

    board_display()

    board_collision_check()

    block_collision_check()

    if not (BALL_RADIUS <= ball_x + dx <= WINDOW_WIDTH - BALL_RADIUS):
        dx = -dx
    if BALL_RADIUS > ball_y + dy:
        dy = -dy
    if ball_y + dy > WINDOW_HEIGHT - BOARD_HEIGHT:
        running = False

    ball_x += dx
    ball_y += dy

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if 0 <= board_x - BOARD_MOVE:
            board_x -= BOARD_MOVE
    if keys[pygame.K_RIGHT]:
        if board_x + BOARD_MOVE <= WINDOW_WIDTH - BOARD_WIDTH:
            board_x += BOARD_MOVE

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()