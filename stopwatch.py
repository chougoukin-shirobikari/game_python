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
        self.start, self.start_rect = self.text_board('NotoSansJP-Regular.ttf', 55, "START", WHITE)
        self.stop, self.stop_rect = self.text_board('NotoSansJP-Regular.ttf', 55, "STOP", WHITE)

        self.start_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 82.5)
        self.stop_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 82.5)

        display_surface.blit(self.start, self.start_rect)
        #display_surface.blit(self.stop, self.stop_rect)

        self.milliseconds0, self.milliseconds0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.milliseconds1, self.milliseconds1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.milliseconds2, self.milliseconds2_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.seconds0, self.seconds0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.seconds1, self.seconds1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.minutes0, self.minutes0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.minutes1, self.minutes1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)

        self.stopWatchTimeRect()
        self.stopWatchDisplay()


    def text_board(self, font, size, text, color):
        font = pygame.font.Font(font, size)
        textsurf = font.render(text, True, color)
        textsurf_rect = textsurf.get_rect()

        return (textsurf, textsurf_rect)
    
    def stopWatchTimeRect(self):
        self.milliseconds0_rect.topleft = (530, WINDOW_HEIGHT - 175 - self.milliseconds0_rect.height)
        self.milliseconds1_rect.topleft = (640, WINDOW_HEIGHT - 175 - self.milliseconds1_rect.height)
        self.milliseconds2_rect.topleft = (750, WINDOW_HEIGHT - 175 - self.milliseconds0_rect.height)
        self.seconds0_rect.topleft = (290, WINDOW_HEIGHT - 175 - self.seconds0_rect.height)
        self.seconds1_rect.topleft = (400, WINDOW_HEIGHT - 175 - self.seconds1_rect.height)
        self.minutes0_rect.topleft = (50, WINDOW_HEIGHT - 175 - self.minutes0_rect.height)
        self.minutes1_rect.topleft = (160, WINDOW_HEIGHT - 175 - self.minutes1_rect.height)
    
    def stopWatchDisplay(self):
        display_surface.blit(self.milliseconds0, self.milliseconds0_rect)
        display_surface.blit(self.milliseconds1, self.milliseconds1_rect)
        display_surface.blit(self.milliseconds2, self.milliseconds2_rect)
        display_surface.blit(self.seconds0, self.seconds0_rect)
        display_surface.blit(self.seconds1, self.seconds1_rect)
        display_surface.blit(self.minutes0, self.minutes0_rect)
        display_surface.blit(self.minutes1, self.minutes1_rect)
        

stop_watch = StopWatch()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()