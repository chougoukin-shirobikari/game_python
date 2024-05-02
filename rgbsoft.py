import pygame


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("RGBソフト")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

red_button = pygame.draw.rect(display_surface, WHITE, (50, WINDOW_HEIGHT - 150, 100, 100), 1)
green_button = pygame.draw.rect(display_surface, WHITE, (200, WINDOW_HEIGHT - 150, 100, 100), 1)
blue_button = pygame.draw.rect(display_surface, WHITE, (350, WINDOW_HEIGHT - 150, 100, 100), 1)

color_display = pygame.draw.rect(display_surface, WHITE, (WINDOW_WIDTH // 2 - 125, WINDOW_HEIGHT // 2 - 200, 250, 250), 1)

font = pygame.font.Font('NotoSansJP-Regular.ttf', 50)

red_button_number = 255
green_button_number = 255
blue_button_number = 255

def text_board(text, color, x, y):
    textsurf = font.render(text, True, color)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    
    display_surface.blit(textsurf, textsurf_rect)

def button_number_change(button, color, x, y):
    pygame.draw.rect(display_surface, BLACK, (x - 40, y - 40, 80, 80))
    text_board(button, color, x, y)

def button_number_update():
    button_number_change(str(red_button_number), RED, 100, WINDOW_HEIGHT - 100)
    button_number_change(str(green_button_number), GREEN, 250, WINDOW_HEIGHT - 100)
    button_number_change(str(blue_button_number), BLUE, 400, WINDOW_HEIGHT - 100)

button_number_update()

def display_color():
    pygame.draw.rect(display_surface, (red_button_number, green_button_number, blue_button_number), (WINDOW_WIDTH // 2 - 124, WINDOW_HEIGHT // 2 - 199, 248, 248))

display_color()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                if red_button.collidepoint((mouse_x, mouse_y)):
                    red_button_number -= 5
                    if red_button_number < 0:
                        red_button_number = 0
                if green_button.collidepoint((mouse_x, mouse_y)):
                    green_button_number -= 5
                    if green_button_number < 0:
                        green_button_number = 0
                if blue_button.collidepoint((mouse_x, mouse_y)):
                    blue_button_number -= 5
                    if blue_button_number < 0:
                        blue_button_number = 0
            elif event.button == 3:
                if red_button.collidepoint((mouse_x, mouse_y)):
                    red_button_number += 5
                    if red_button_number > 255:
                        red_button_number = 255
                if green_button.collidepoint((mouse_x, mouse_y)):
                    green_button_number += 5
                    if green_button_number > 255:
                        green_button_number = 255
                if blue_button.collidepoint((mouse_x, mouse_y)):
                    blue_button_number += 5
                    if blue_button_number > 255:
                        blue_button_number = 255
    
            button_number_update()
    
            display_color()
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()