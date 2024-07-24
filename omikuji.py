import pygame, random


pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("おみくじ")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (116, 80, 48)
DARK_BROWN = (78, 53, 36)
GRAY = (126, 126, 126)

display_surface.fill(BLACK)

FPS = 60
clock = pygame.time.Clock()

button = pygame.Rect(100, 200, 200, 300)
button_cover = pygame.Rect(110, 210, 180, 280)

font = pygame.font.Font('NotoSansJP-Regular.ttf', 30)
u_font = pygame.font.Font('NotoSansJP-Regular.ttf', 80)

text = font.render("おみくじ", True, WHITE)
daikichi = u_font.render("大吉", True, YELLOW)
chukichi = u_font.render("中吉", True, WHITE)
matsukichi = u_font.render("末吉", True, WHITE)
kyou = u_font.render("大凶", True, GRAY)

daikichi_rect = daikichi.get_rect()
chukichi_rect = chukichi.get_rect()
matsukichi_rect = matsukichi.get_rect()
kyou_rect = kyou.get_rect()

daikichi_rect.center = (WINDOW_WIDTH // 2, 100)
chukichi_rect.center = (WINDOW_WIDTH // 2, 100)
matsukichi_rect.center = (WINDOW_WIDTH // 2, 100)
kyou_rect.center = (WINDOW_WIDTH // 2, 100)

u_list = [(daikichi, daikichi_rect), (chukichi, chukichi_rect), (matsukichi, matsukichi_rect), (kyou, kyou_rect)]

previous_random_number = -1


running = True

while running:
    pygame.draw.rect(display_surface, BROWN, button)
    pygame.draw.rect(display_surface, DARK_BROWN, button_cover)

    display_surface.blit(text, (140, 300))

    pygame.display.update()
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                display_surface.fill(BLACK)

                while True:
                    random_number = random.randrange(0, len(u_list))
                    if previous_random_number != random_number:
                        previous_random_number = random_number
                        break
                
                u, u_rect = u_list[random_number]
                
                display_surface.blit(u, u_rect)

pygame.quit()