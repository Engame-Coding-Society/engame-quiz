import pygame
import pygame_gui


class Screen:
    def __init__(self, screen_size, clock):
        self.screen_size = screen_size
        self.clock = clock
        self.init_ui()

    @abstractmethod
    def init_ui(self):
        """Initialize the UI elements for this screen."""
        raise NotImplementedError

    @abstractmethod
    def process_screen_events(self, event):
        """Handle events that occur on this screen."""
        raise NotImplementedError

    @abstractmethod
    def draw_screen(self, surface):
        """Draw the UI elements for this screen to the provided surface."""
        raise NotImplementedError
