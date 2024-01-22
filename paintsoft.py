import pygame


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ペイントソフト")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FUCHSIA = (255, 0, 255)
AQUA = (0, 255, 255)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
DIMGRAY = (105, 105, 105)

display_surface.fill(BLACK)

FPS = 100
clock = pygame.time.Clock()

pygame.draw.rect(display_surface, WHITE, (10, WINDOW_HEIGHT - 90, 80, 80), 1)
pygame.draw.rect(display_surface, WHITE, (100, WINDOW_HEIGHT - 90, 300, 80))
pygame.draw.rect(display_surface, DIMGRAY, (10, 10, 390, 390), 1)

clear_display = pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50), 35)

line1_display = pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH - 90, 10, 80, 80), 1)
line2_display = pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH - 90, 100, 80, 80), 1)
line3_display = pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH - 90, 190, 80, 80), 1)

pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH - 57, 20, 10, 60))
pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH - 63, 110, 25, 60))
pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH - 75, 200, 50, 60))

player_current_color = WHITE

def current_display_color():
    pygame.draw.rect(display_surface, player_current_color, (11, WINDOW_HEIGHT - 89, 78, 78))

current_display_color()

colors = [BLACK, RED, GREEN, BLUE, YELLOW, FUCHSIA, AQUA, GRAY, SILVER, NAVY, TEAL, OLIVE, PURPLE, MAROON]
choice_color = []

for i in range(len(colors)):
    choice_color.append([colors[i], pygame.draw.rect(display_surface, colors[i], (110 + (20 * i), WINDOW_HEIGHT - 85, 20, 70))])
    

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if clear_display.collidepoint((mouse_x, mouse_y)):
                print('画面のクリアボタンがクリックされた！')
            if line1_display.collidepoint((mouse_x, mouse_y)):
                print('線の幅のボタン1がクリックされた！')
            if line2_display.collidepoint((mouse_x, mouse_y)):
                print('線の幅のボタン2がクリックされた！')
            if line3_display.collidepoint((mouse_x, mouse_y)):
                print('線の幅のボタン3がクリックされた！')
            
            for c, r in choice_color:
                if r.collidepoint((mouse_x, mouse_y)):
                    player_current_color = c
                    current_display_color()
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()