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
    
    def gameOverCheck(self):
        return self.y >= WINDOW_HEIGHT - 50

enemy = Enemy(WINDOW_WIDTH - 50, 0, -5)

player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT - 50)


running = True

while running:
    display_surface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    
    if keys[pygame.K_SPACE]:
        player.shot()
    
    player.shotUpdate(display_surface)
    
    player.draw(display_surface)

    enemy.draw(display_surface)

    enemy.update()

    if enemy.gameOverCheck():
        running = False

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()