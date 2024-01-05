from abc import abstractmethod
from pygame_gui import UIManager


class Screen:
    def __init__(self, screen_size, clock, loader):
        self.screen_size = screen_size
        self.clock = clock
        self.ui = UIManager(self.screen_size, "assets/theme.json", resource_loader=loader)

    @abstractmethod
    def init_ui(self):
        """Initialize the UI elements for this screen."""
        raise NotImplementedError

    @abstractmethod
    def process_screen_events(self, event):
        """Handle events that occur on this screen."""
        raise NotImplementedError

    def update(self, time_delta):
        self.ui.update(time_delta)


    def draw_screen(self, surface):
        """Draw the UI elements for this screen to the provided surface."""
        self.ui.draw_ui(surface)
