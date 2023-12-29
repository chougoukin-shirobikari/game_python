import pygame


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("インベーダーゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.playerMove = 10

        self.shotOn = False
        self.shotSize = 10
        self.shot_x = self.x + (self.width // 2)
        self.shot_y = self.y + self.shotSize
        self.shotSpeed = 15
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    
    def moveLeft(self):
        if 0 <= self.x - self.playerMove:
            self.x -= self.playerMove
    
    def moveRight(self):
        if self.x + self.playerMove <= WINDOW_WIDTH - self.width:
            self.x += self.playerMove
    
    def shot(self):
        if not self.shotOn:
            self.shotOn = True
            self.shot_x = self.x + (self.width // 2)
            self.shot_y = self.y + self.shotSize
    
    def shotUpdate(self, screen):
        if self.shotOn:
            if self.shot_y - self.shotSpeed <= 0:
                self.shotOn = False
                return
            else:
                self.shot_y -= self.shotSpeed
                pygame.draw.circle(screen, WHITE, (self.shot_x, self.shot_y), self.shotSize)
    
    def shotPosition(self):
        if self.shotOn:
            return (self.shot_x, self.shot_y)
        return False

class Enemy:
    def __init__(self, x, y, move_x):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.move_x = move_x
        self.move_y = self.height
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
    
    def update(self):
        self.x += self.move_x
        if self.x < 0:
            self.y += self.move_y
            self.move_x = -self.move_x
        elif self.x > WINDOW_WIDTH - self.width:
            self.y += self.move_y
            self.move_x = -self.move_x
    
    def shotCollisionCheck(self, shot_position_x, shot_position_y):
        if self.x <= shot_position_x <= self.x + self.width and self.y <= shot_position_y < self.y + self.height:
            return True
        return False
    
    def gameOverCheck(self):
        return self.y >= WINDOW_HEIGHT - 50

player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT - 50)

milliseconds_delay = 3000
enemy_event = pygame.USEREVENT + 0
pygame.time.set_timer(enemy_event, milliseconds_delay)

enemy_move_x = -5
enemy_list = [Enemy(WINDOW_WIDTH - 50, 0, enemy_move_x)]

count = 0

def make_enemy():
    enemy_list.append(Enemy(WINDOW_WIDTH - 50, 0, enemy_move_x))

def enemyGenerate(local_milliseconds_delay, local_enemy_move_x):
    global enemy_move_x
    global milliseconds_delay
    
    enemy_move_x = local_enemy_move_x
    milliseconds_delay = local_milliseconds_delay

    pygame.time.set_timer(enemy_event, 0)
    pygame.time.set_timer(enemy_event, milliseconds_delay)

def text_board(font, text, color, size, x, y):
    font = pygame.font.SysFont(font, size)
    textsurf = font.render(text, True, color)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)


running = True

while running:
    display_surface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == enemy_event:
            enemy_move_x = max(enemy_move_x - 0.25, -8)
            if count >= 5 and milliseconds_delay == 3000:
                enemyGenerate(2500, -5)
            elif count >= 10 and milliseconds_delay == 2500:
                enemyGenerate(2000, -5)
            elif count >= 15 and milliseconds_delay == 2000:
                enemyGenerate(1500, -5)
            elif count >= 30 and milliseconds_delay == 1500:
                enemyGenerate(1000, -5.5)
            elif count >= 50 and milliseconds_delay == 1000:
                enemyGenerate(600, -6)
            elif count >= 100 and milliseconds_delay == 600:
                enemyGenerate(500, -7)
            elif count >= 250 and milliseconds_delay == 500:
                enemyGenerate(300, -8)

            make_enemy()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    if keys[pygame.K_SPACE]:
        player.shot()
    
    player.shotUpdate(display_surface)

    position = player.shotPosition()

    if position:
        shot_position_x, shot_position_y = position
        for e in enemy_list:
            previous_len_enemy = len(enemy_list)
            enemy_list = [e for e in enemy_list if not e.shotCollisionCheck(shot_position_x, shot_position_y)]
            current_len_enemy = len(enemy_list)
            count += previous_len_enemy - current_len_enemy
    
    player.draw(display_surface)

    for e in enemy_list:
        e.draw(display_surface)
    
    for e in enemy_list:
        e.update()
    
    for e in enemy_list:
        if e.gameOverCheck():
            gameOver = True
            text_board('hg丸ｺﾞｼｯｸmpro', f'倒した敵の数：{count}', WHITE, 50, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
            text_board('hg丸ｺﾞｼｯｸmpro', f'再プレイ：sキーを押す', WHITE, 40, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
            pygame.display.update()

            while gameOver:
                pygame.time.set_timer(enemy_event, 0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        running = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        display_surface.fill(BLACK)
                        player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT - 50)
                        enemy_move_x = -5
                        enemy_list = [Enemy(WINDOW_WIDTH - 50, 0, enemy_move_x)]
                        count = 0
                        milliseconds_delay = 3000
                        pygame.time.set_timer(enemy_event, milliseconds_delay)
                        gameOver = False

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()