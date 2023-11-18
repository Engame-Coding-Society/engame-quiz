import pygame
import pygame_gui
from pygame_gui.core import ObjectID, IncrementalThreadedResourceLoader

pygame.init()
pygame.display.set_caption('Engame Quiz')
window_surface = pygame.display.set_mode((800, 600))

bg = pygame.Surface((800, 600))
bg.fill(pygame.Color("#ebebeb"))

loader = IncrementalThreadedResourceLoader()
clock = pygame.time.Clock()
ui = pygame_gui.UIManager((800, 600), 'theme.json', resource_loader=loader)
ui.add_font_paths("Montserrat",
                  "assets/fonts/Montserrat-Regular.ttf",
                  "assets/fonts/Montserrat-Bold.ttf",
                  "assets/fonts/Montserrat-Italic.ttf",
                  "assets/fonts/Montserrat-BoldItalic.ttf")

load_time_1 = clock.tick()
ui.preload_fonts([{'name': 'Montserrat', 'html_size': 4.5, 'style': 'bold'},
                  {'name': 'Montserrat', 'html_size': 4.5, 'style': 'regular'},
                  {'name': 'Montserrat', 'html_size': 2, 'style': 'regular'},
                  {'name': 'Montserrat', 'html_size': 2, 'style': 'italic'},
                  {'name': 'Montserrat', 'html_size': 6, 'style': 'bold'},
                  {'name': 'Montserrat', 'html_size': 6, 'style': 'regular'},
                  {'name': 'Montserrat', 'html_size': 6, 'style': 'bold_italic'},
                  {'name': 'Montserrat', 'html_size': 4, 'style': 'bold'},
                  {'name': 'Montserrat', 'html_size': 4, 'style': 'regular'},
                  {'name': 'Montserrat', 'html_size': 4, 'style': 'italic'},
                  ])
loader.start()
finished_loading = False
while not finished_loading:
    finished_loading, progress = loader.update()
load_time_2 = clock.tick()
print('Font load time taken:', load_time_2 / 1000.0, 'seconds.')

hello_text = pygame_gui.elements.UILabel(pygame.Rect((0, 0), (800, 100)), "Hello everyone!", ui,
                                         object_id=ObjectID("#the_title", "@text"), anchors={'top': 'top'})

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        ui.process_events(event)

    ui.update(time_delta)
    window_surface.blit(bg, (0, 0))
    ui.draw_ui(window_surface)
    pygame.display.update()
