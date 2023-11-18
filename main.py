import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption('Engame Quiz')
window_surface = pygame.display.set_mode((800, 600))

bg = pygame.Surface((800, 600))
bg.fill(pygame.Color("#ebebeb"))

ui = pygame_gui.UIManager((800, 600))
hello_text = pygame_gui.elements.UILabel(pygame.Rect((50, 0), (200, 150)), "Hello everyone!", ui)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        ui.process_events(event)

    ui.update(time_delta)
    window_surface.blit(bg, (0, 0))
    ui.draw_ui(window_surface)
    pygame.display.update()

