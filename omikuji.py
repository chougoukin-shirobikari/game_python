import pygame

pygame.init()

display_surface = pygame.display.set_mode((400, 600))

pygame.display.set_caption("おみくじ")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()