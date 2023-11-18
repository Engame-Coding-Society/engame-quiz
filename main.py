import pygame

pygame.init()
pygame.display.set_caption('Engame Quiz')
window_surface = pygame.display.set_mode((800, 600))

bg = pygame.Surface((800, 600))
bg.fill(pygame.Color("#ebebeb"))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(bg, (0, 0))
    pygame.display.update()
