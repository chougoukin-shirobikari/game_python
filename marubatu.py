import pygame

pygame.init()

display_surface = pygame.display.set_mode((500, 500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()