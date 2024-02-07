import pygame


pygame.init()

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("シンプルなピアノ")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

sound = ['ド', 'レ', 'ミ', 'ファ', 'ソ', 'ラ', 'シ', 'ド']

keyboard_info = []

def text_board(font, size, text, color, x, y):
    font = pygame.font.Font(font, size)
    textsurf = font.render(text, True, color)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    display_surface.blit(textsurf, textsurf_rect)

text_board('NotoSansJP-Regular.ttf', 50, 'シンプルなピアノ', WHITE, WINDOW_WIDTH // 2, 50)

pygame.draw.rect(display_surface, WHITE, (0, WINDOW_HEIGHT // 2, WINDOW_WIDTH, WINDOW_HEIGHT // 2))

for c in range(8):
    keyboard_info.append(pygame.draw.rect(display_surface, BLACK, (6 + (WINDOW_WIDTH // 8 * c), WINDOW_HEIGHT // 2, WINDOW_WIDTH // 8 - 10, WINDOW_HEIGHT // 2 - 10), 2))

for c in range(8):
    text_board('NotoSansJP-Regular.ttf', 30, sound[c], BLACK, 6 + (WINDOW_WIDTH // 8 * c) + 35, WINDOW_HEIGHT // 2 + 100)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if keyboard_info[0].collidepoint(x, y):
                    print('ド')
                if keyboard_info[1].collidepoint(x, y):
                    print('レ')
                if keyboard_info[2].collidepoint(x, y):
                    print('ミ')
                if keyboard_info[3].collidepoint(x, y):
                    print('ファ')
                if keyboard_info[4].collidepoint(x, y):
                    print('ソ')
                if keyboard_info[5].collidepoint(x, y):
                    print('ラ')
                if keyboard_info[6].collidepoint(x, y):
                    print('シ')
                if keyboard_info[7].collidepoint(x, y):
                    print('ド')  
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()