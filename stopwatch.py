import pygame


pygame.init()

WINDOW_WIDTH = 860
WINDOW_HEIGHT = 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ストップウォッチ")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 250)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class StopWatch():
    def __init__(self):
        pygame.draw.line(display_surface, WHITE, (30, WINDOW_HEIGHT - 175), (130, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, WHITE, (140, WINDOW_HEIGHT - 175), (240, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, WHITE, (270, WINDOW_HEIGHT - 175), (370, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, WHITE, (380, WINDOW_HEIGHT - 175), (480, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, WHITE, (510, WINDOW_HEIGHT - 175), (610, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, WHITE, (620, WINDOW_HEIGHT - 175), (720, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, WHITE, (730, WINDOW_HEIGHT - 175), (830, WINDOW_HEIGHT - 175), 5)

        self.playButton = pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 120, 200, 80), 2)

stop_watch = StopWatch()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()