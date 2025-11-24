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

sound_do = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_1do.mp3")
sound_re = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_2re.mp3")
sound_mi = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_3mi.mp3")
sound_fa = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_4fa.mp3")
sound_so = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_5so.mp3")
sound_ra = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_6ra.mp3")
sound_si = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_7si.mp3")
sound_do2 = pygame.mixer.Sound("maou_se_inst/maou_se_inst_piano1_8do.mp3")

keyboard_sound = [sound_do, sound_re, sound_mi, sound_fa, sound_so, sound_ra, sound_si, sound_do2]

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
                
                for c in range(8):
                    if keyboard_info[c].collidepoint(x, y):
                        keyboard_sound[c].play()
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()
