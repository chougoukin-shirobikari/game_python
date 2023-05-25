import pygame

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('〇×ゲーム')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

LINE_WIDTH = 5

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

def init():
    pygame.draw.rect(display_surface, WHITE, (100, 100, 300, 300), LINE_WIDTH)

    pygame.draw.line(display_surface, WHITE, (200, 100), (200, 399), LINE_WIDTH)
    pygame.draw.line(display_surface, WHITE, (300, 100), (300, 399), LINE_WIDTH)
    pygame.draw.line(display_surface, WHITE, (100, 200), (399, 200), LINE_WIDTH)
    pygame.draw.line(display_surface, WHITE, (100, 300), (399, 300), LINE_WIDTH)

    title_font = pygame.font.SysFont('hg丸ｺﾞｼｯｸmpro', 50)
    title = title_font.render("〇×ゲーム", True, WHITE)
    title_font_rect = title.get_rect()
    title_font_rect.center = (WINDOW_WIDTH // 2, 50)
    
    display_surface.blit(title, title_font_rect)

init()

game = [[''] * 3 for _ in range(3)]

def mouseCheck(x, y):
    mouse_click_y, mouse_click_x = y // 100, x // 100

    mouse_click_y -= 1
    mouse_click_x -= 1
    
    print(mouse_click_y, mouse_click_x)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            mouseCheck(mouseX, mouseY)
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()