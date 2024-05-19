import pygame, random


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ビンゴゲーム")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
LemonChiffon = (255, 250, 205)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

class Bingo():
    def __init__(self):
        pygame.draw.rect(display_surface, WHITE, (10, 150, 390, 390), 1)
        pygame.draw.rect(display_surface, WHITE, (425, 200, 150, 150), 1)
        pygame.draw.rect(display_surface, WHITE, (410, 425, 180, 225), 1)
        
        self.number_button = pygame.draw.rect(display_surface, WHITE, (30, WINDOW_HEIGHT - 125, 350, 80), 1)

        text_board('NotoSansJP-Regular.ttf', 50, 'ビンゴゲーム', YELLOW, None, WINDOW_WIDTH // 2, 50)
        text_board('NotoSansJP-Regular.ttf', 30, '番号', SILVER, None, 500, 165)
        text_board('NotoSansJP-Regular.ttf', 30, '出た数字', SILVER, None, 500, 390)
        text_board('NotoSansJP-Regular.ttf', 40, '番号を選ぶ', WHITE, None, 208, WINDOW_HEIGHT - 85)

        self.bingo_list = []

        self.bingo_display()

        self.bingo_number_gray_display = {}

        self.record_the_bingo_numbers()

        self.not_choosed_numbers = product_bingo_numbers()

        self.bingo_game = [[False] * 5 for _ in range(5)]
        self.bingo_game[2][2] = True

        [print(i) for i in self.bingo_game]

    def bingo_display(self):
        bingo_numbers = product_bingo_numbers()
        for y in range(5):
            temp_bingo_list = []
            for x in range(5):
                number = str(bingo_numbers.pop(random.randrange(len(bingo_numbers))))
                rect = pygame.draw.rect(display_surface, WHITE, (20 + 75 * x, 160 + 75 * y, 70, 70), 1)
                if y == x == 2:
                    number = 'Free'
                    self.change_bingo_number(rect, number)
                else:
                    text_board('NotoSansJP-Regular.ttf', 30, number, WHITE, None, rect.centerx, rect.centery)
                
                temp_bingo_list.append([rect, number])
            
            self.bingo_list.append(temp_bingo_list)
    
    def change_bingo_number(self, rect, num, rect_color=LemonChiffon, num_color=GRAY):
        pygame.draw.rect(display_surface, rect_color, (rect.x + 1, rect.y + 1, rect.width - 2, rect.height - 2))
        text_board('NotoSansJP-Regular.ttf', 30, str(num), num_color, None, rect.centerx, rect.centery)
    
    def record_the_bingo_numbers(self):
        bingo_numbers = product_bingo_numbers()
        for y in range(10):
            for x in range(8):
                if bingo_numbers:
                    number = bingo_numbers.pop(0)
                    text_board('NotoSansJP-Regular.ttf', 15, str(number), WHITE, None, 430 + 20 * x, 445 + 20 * y)
                    self.bingo_number_gray_display[number] = ['NotoSansJP-Regular.ttf', 15, str(number), GRAY, None, 430 + 20 * x, 445 + 20 * y]

    def check_the_game(self, number):
        for y in range(len(self.bingo_list)):
            for x in range(len(self.bingo_list[y])):
                r, n = self.bingo_list[y][x]
                if n == number:
                    self.change_bingo_number(r, n)
                    self.bingo_game[y][x] = True
                    [print(i) for i in self.bingo_game]
    
    def check_bingo(self):
        check = False

        for y in range(5):
            if all(self.bingo_game[y]):
                check = True
                for x in range(5):
                    self.change_bingo_number(*self.bingo_list[y][x], YELLOW)
        
        for x in range(5):
            if all(self.bingo_game[y][x] for y in range(5)):
                check = True
                for y in range(5):
                    self.change_bingo_number(*self.bingo_list[y][x], YELLOW)
        
        if all(self.bingo_game[i][i] for i in range(5)):
            check = True
            for i in range(5):
                self.change_bingo_number(*self.bingo_list[i][i], YELLOW)
        
        if all(self.bingo_game[i][4-i] for i in range(5)):
            check = True
            for i in range(5):
                self.change_bingo_number(*self.bingo_list[i][4-i], YELLOW)
        
        return check

def product_bingo_numbers():
    bingo_numbers = []

    for i in range(1, 76):
        bingo_numbers.append(i)
    
    return bingo_numbers

def text_board(font, size, text, color, bgColor, x, y):
    font = pygame.font.Font(font, size)
    textsurf = font.render(text, True, color, bgColor)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)


bingo = Bingo()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if bingo.number_button.collidepoint(mouse_x, mouse_y):
                number = str(bingo.not_choosed_numbers.pop(random.randrange(len(bingo.not_choosed_numbers))))
                pygame.draw.rect(display_surface, BLACK, (426, 201, 148, 148))
                text_board('NotoSansJP-Regular.ttf', 100, str(number), WHITE, None, 500, 270)
                text_board(*bingo.bingo_number_gray_display[int(number)])
                bingo.check_the_game(number)
    
    check_bingo_result = bingo.check_bingo()
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()