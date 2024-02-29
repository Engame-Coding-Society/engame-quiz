from screens.backends.events import *
from screens.backends.components import Rect

try:
    import pygame
    import screens.backends.pygame.renderer as pygame_backend
    RENDERER = pygame_backend.PygameRenderer()
except ImportError as import_err:
    print("couldn't init pygame!")
    from screens.backends.web.renderer import WebRenderer
    RENDERER = WebRenderer()
