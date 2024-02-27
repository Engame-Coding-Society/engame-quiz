from screens.backends.renderer import Renderer

try:
    import pygame
    import screens.backends.pygame as pygame_backend
    RENDERER = pygame_backend.PygameRenderer()
except ImportError:
    RENDERER = Renderer()
