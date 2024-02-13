import pygame


pygame.init()

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("じゃんけんゲーム")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 125, 128)

FPS = 60
clock = pygame.time.Clock()

def text_board(font, size, text, color, x, y):
    font = pygame.font.SysFont(font, size)
    textsurf = font.render(text, True, color)
    textsurf_rect = textsurf.get_rect()
    textsurf_rect.center = (x, y)
    
    return (textsurf, textsurf_rect)

choice, choice_rect = text_board('meiryo', 50, "なにを選びますか？", WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150)
choice_gu, choice_gu_rect = text_board('meiryo', 60, "グー", WHITE, 100, WINDOW_HEIGHT - 50)
choice_choki, choice_choki_rect = text_board('meiryo', 60, "チョキ", WHITE, 335, WINDOW_HEIGHT - 50)
choice_pa, choice_pa_rect = text_board('meiryo', 60, "パー", WHITE, 550, WINDOW_HEIGHT - 50)

game_choice = [(choice, choice_rect), (choice_gu, choice_gu_rect), (choice_choki, choice_choki_rect), (choice_pa, choice_pa_rect)]

win, win_rect = text_board('hgｺﾞｼｯｸe', 64, "あなたの勝ち！", YELLOW, WINDOW_WIDTH // 2, 80)
lose, lose_rect = text_board('hgｺﾞｼｯｸe', 64, "あなたの負け", GRAY, WINDOW_WIDTH // 2, 80)
draw, draw_rect = text_board('hgｺﾞｼｯｸe', 64, "引き分け", WHITE, WINDOW_WIDTH // 2, 80)

continue_text, continue_rect = text_board('meiryo', 50, "続ける", WHITE, WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100)
quit_text, quit_rect = text_board('meiryo', 50, "やめる", WHITE, WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT - 100)

continue_choice = [(continue_text, continue_rect), (quit_text, quit_rect)]

player_dict = {'gu': text_board('hgｺﾞｼｯｸe', 64, "グー", WHITE, 200, 250),
               'choki': text_board('hgｺﾞｼｯｸe', 64, "チョキ", WHITE, 200, 250),
               'pa': text_board('hgｺﾞｼｯｸe', 64, "パー", WHITE, 200, 250)}

opponent_dict = {'gu': text_board('hgｺﾞｼｯｸe', 64, "グー", WHITE, 470, 250),
                 'choki': text_board('hgｺﾞｼｯｸe', 64, "チョキ", WHITE, 470, 250),
                 'pa': text_board('hgｺﾞｼｯｸe', 64, "パー", WHITE, 470, 250)}

def game_text(message):
    [display_surface.blit(c, r) for c, r in message]

game_text(game_choice)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()