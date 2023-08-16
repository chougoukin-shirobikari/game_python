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
        self.drawLines(WHITE)

        self.playButton = pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 120, 200, 80), 2)

        self.start, self.start_rect = self.text_board('NotoSansJP-Regular.ttf', 55, "START", WHITE)
        self.stop, self.stop_rect = self.text_board('NotoSansJP-Regular.ttf', 55, "STOP", WHITE)

        self.start_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 82.5)
        self.stop_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 82.5)

        self.milliseconds0, self.milliseconds0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.milliseconds1, self.milliseconds1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.milliseconds2, self.milliseconds2_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.seconds0, self.seconds0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.seconds1, self.seconds1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.minutes0, self.minutes0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)
        self.minutes1, self.minutes1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, "0", WHITE)

        self.stopWatchTimeRect()
        
        self.stopWatchDisplay()

        self.timeStart = False

        self.update_time = 0

        self.playButtonDisplay()
    
    def drawLines(self, color):
        pygame.draw.rect(display_surface, BLACK, (0, WINDOW_HEIGHT - 178, WINDOW_WIDTH, 6))

        pygame.draw.line(display_surface, color, (30, WINDOW_HEIGHT - 175), (130, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, color, (140, WINDOW_HEIGHT - 175), (240, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, color, (270, WINDOW_HEIGHT - 175), (370, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, color, (380, WINDOW_HEIGHT - 175), (480, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, color, (510, WINDOW_HEIGHT - 175), (610, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, color, (620, WINDOW_HEIGHT - 175), (720, WINDOW_HEIGHT - 175), 5)
        pygame.draw.line(display_surface, color, (730, WINDOW_HEIGHT - 175), (830, WINDOW_HEIGHT - 175), 5)

    def playButtonDisplay(self):
        pygame.draw.rect(display_surface, BLACK, (WINDOW_WIDTH // 2 - 90, WINDOW_HEIGHT - 110, 180, 60))

        if self.timeStart:
            display_surface.blit(self.stop, self.stop_rect)
        else:
            display_surface.blit(self.start, self.start_rect)
    
    def stopWatchUpdate(self):
        self.stopWatchFill()
        time_check = pygame.time.get_ticks() - self.update_time
        time_check = str(time_check).zfill(7)

        milliseconds0 = time_check[4]
        milliseconds1 = time_check[5]
        milliseconds2 = time_check[6]
        seconds = int(time_check[:4]) % 60
        minutes = int(time_check[:4]) // 60

        seconds0, seconds1 = str(seconds).zfill(2)
        minutes0, minutes1 = str(minutes).zfill(2)

        self.milliseconds0, self.milliseconds0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, milliseconds0, WHITE)
        self.milliseconds1, self.milliseconds1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, milliseconds1, WHITE)
        self.milliseconds2, self.milliseconds2_rect = self.text_board('NotoSansJP-Regular.ttf', 95, milliseconds2, WHITE)
        self.seconds0, self.seconds0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, seconds0, WHITE)
        self.seconds1, self.seconds1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, seconds1, WHITE)
        self.minutes0, self.minutes0_rect = self.text_board('NotoSansJP-Regular.ttf', 95, minutes0, WHITE)
        self.minutes1, self.minutes1_rect = self.text_board('NotoSansJP-Regular.ttf', 95, minutes1, WHITE)

        self.stopWatchTimeRect()
        self.stopWatchDisplay()

        if minutes == 10:
            self.timeStart = False
            self.drawLines(WHITE)
            self.playButtonDisplay()
            self.update_time = 0
            return

    
    def text_board(self, font, size, text, color):
        font = pygame.font.Font(font, size)
        textsurf = font.render(text, True, color)
        textsurf_rect = textsurf.get_rect()

        return (textsurf, textsurf_rect)
    
    def stopWatchTimeRect(self):
        self.milliseconds0_rect.topleft = (530, WINDOW_HEIGHT - 175 - self.milliseconds0_rect.height)
        self.milliseconds1_rect.topleft = (640, WINDOW_HEIGHT - 175 - self.milliseconds1_rect.height)
        self.milliseconds2_rect.topleft = (750, WINDOW_HEIGHT - 175 - self.milliseconds2_rect.height)
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
    
    def stopWatchFill(self):
        pygame.draw.rect(display_surface, BLACK, (530, WINDOW_HEIGHT - 175 - self.milliseconds0_rect.height, 80, 120))
        pygame.draw.rect(display_surface, BLACK, (640, WINDOW_HEIGHT - 175 - self.milliseconds1_rect.height, 80, 120))
        pygame.draw.rect(display_surface, BLACK, (750, WINDOW_HEIGHT - 175 - self.milliseconds2_rect.height, 80, 120))
        pygame.draw.rect(display_surface, BLACK, (290, WINDOW_HEIGHT - 175 - self.seconds0_rect.height, 80, 120))
        pygame.draw.rect(display_surface, BLACK, (400, WINDOW_HEIGHT - 175 - self.seconds1_rect.height, 80, 120))
        pygame.draw.rect(display_surface, BLACK, (50, WINDOW_HEIGHT - 175 - self.minutes0_rect.height, 80, 120))
        pygame.draw.rect(display_surface, BLACK, (160, WINDOW_HEIGHT - 175 - self.minutes1_rect.height, 80, 120))
    
    def clickCheck(self, x, y):
        if self.playButton.collidepoint(x, y):
            if not self.timeStart:
                self.timeStart = True
                self.playButtonDisplay()
                self.drawLines(BLUE)
                self.update_time = pygame.time.get_ticks()
            else:
                self.timeStart = False
                self.playButtonDisplay()
                self.drawLines(WHITE)
                self.update_time = 0

stop_watch = StopWatch()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            stop_watch.clickCheck(mouse_x, mouse_y)
        
    if stop_watch.timeStart:
        stop_watch.stopWatchUpdate()
    
    clock.tick(FPS)

    pygame.display.update()

pygame.quit()