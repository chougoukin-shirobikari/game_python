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

font = pygame.font.SysFont('hg丸ｺﾞｼｯｸmpro', 80)
maru_font = font.render("〇", True, WHITE)
batu_font = font.render("×", True, WHITE)
blank_font = font.render("", True, WHITE)

player = 0

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
    global player

    mouse_click_y, mouse_click_x = y // 100, x // 100

    mouse_click_y -= 1
    mouse_click_x -= 1

    if game[mouse_click_y][mouse_click_x] == '':
        if player == 0:
            game[mouse_click_y][mouse_click_x] = '〇'

            display_surface.blit(maru_font, ((mouse_click_x + 1) * 100 + 10, (mouse_click_y + 1) * 100 + 10))
        
        elif player == 1:
            game[mouse_click_y][mouse_click_x] = '×'
            display_surface.blit(batu_font, ((mouse_click_x + 1) * 100 + 10, (mouse_click_y + 1) * 100 + 10))
    
        player = (player + 1) % 2

def gameCheck():
    if game[0][0] == game[0][1] == game[0][2] == '〇':
        return '〇'
    elif game[0][0] == game[0][1] == game[0][2] == '×':
        return '×'
    elif game[1][0] == game[1][1] == game[1][2] == '〇':
        return '〇'
    elif game[1][0] == game[1][1] == game[1][2] == '×':
        return '×'
    elif game[2][0] == game[2][1] == game[2][2] == '〇':
        return '〇'
    elif game[2][0] == game[2][1] == game[2][2] == '×':
        return '×'
    elif game[0][0] == game[1][0] == game[2][0] == '〇':
        return '〇'
    elif game[0][0] == game[1][0] == game[2][0] == '×':
        return '×'
    elif game[0][1] == game[1][1] == game[2][1] == '〇':
        return '〇'
    elif game[0][1] == game[1][1] == game[2][1] == '×':
        return '×'
    elif game[0][2] == game[1][2] == game[2][2] == '〇':
        return '〇'
    elif game[0][2] == game[1][2] == game[2][2] == '×':
        return '×'
    elif game[0][0] == game[1][1] == game[2][2] == '〇':
        return '〇'
    elif game[0][0] == game[1][1] == game[2][2] == '×':
        return '×'
    elif game[0][2] == game[1][1] == game[2][0] == '〇':
        return '〇'
    elif game[0][2] == game[1][1] == game[2][0] == '×':
        return '×'
    elif '' not in sum(game, []):
        return 0
    else:
        return -1

def gameClear(victory, victory_message):
    judgement_font = pygame.font.SysFont('hg丸ｺﾞｼｯｸmpro', 65)
    judgement = judgement_font.render(victory_message, True, WHITE)
    judgement_font_rect = judgement.get_rect()
    judgement_font_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
    display_surface.blit(judgement, judgement_font_rect)

    gameclear_font = pygame.font.SysFont('hg丸ｺﾞｼｯｸmpro', 35)
    gameclear = gameclear_font.render('再プレイ：スペースキーを押す', True, BLACK, WHITE)
    gameclear_font_rect = gameclear.get_rect()
    gameclear_font_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    display_surface.blit(gameclear, gameclear_font_rect)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            waku_check = False

            if mouseX < 100:
                print('大枠より左を打った')
                waku_check = True
            if mouseX > 400:
                print('大枠より右を打った')
                waku_check = True
            if mouseY < 100:
                print('大枠より上を打った')
                waku_check = True
            if mouseY > 400:
                print('大枠より下を打った')
                waku_check = True
            
            if waku_check:
                continue

            if 100 <= mouseX <= 100 + LINE_WIDTH:
                print('大枠の左を打った')
                waku_check = True
            if 100 + 300 - LINE_WIDTH <= mouseX <= 100 + 300:
                print('大枠の右を打った')
                waku_check = True
            if 100 <= mouseY <= 100 + LINE_WIDTH:
                print('大枠の上を打った')
                waku_check = True
            if 100 + 300 - LINE_WIDTH <= mouseY <= 100 + 300:
                print('大枠の下を打った')
                waku_check = True
            
            if waku_check:
                continue


            line_width_half = LINE_WIDTH // 2 + 1

            if 200 - line_width_half <= mouseX <= 200 + line_width_half:
                print('枠1を打った')
                waku_check = True
            if 300 - line_width_half <= mouseX <= 300 + line_width_half:
                print('枠2を打った')
                waku_check = True
            if 200 - line_width_half <= mouseY <= 200 + line_width_half:
                print('枠3を打った')
                waku_check = True
            if 300 - line_width_half <= mouseY <= 300 + line_width_half:
                print('枠4を打った')
                waku_check = True
            
            if waku_check:
                continue
            
            mouseCheck(mouseX, mouseY)

            ans = gameCheck()
            
            if ans != -1:
                if ans == 0:
                    gameClear(ans, '引き分け')
                else:
                    gameClear(ans, f'{ans}の勝ち')

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()