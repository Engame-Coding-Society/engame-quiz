from screens.backends.renderer import Renderer
from screens.backends.events import *

try:
    import pygame
    import screens.backends.pygame as pygame_backend
    RENDERER = pygame_backend.PygameRenderer()
except ImportError:
    RENDERER = Renderer()
