from abc import abstractmethod


class Screen:
    @abstractmethod
    def init_ui(self, renderer):
        """Initialize the UI elements for this screen."""
        raise NotImplementedError

    @abstractmethod
    def process_screen_events(self, event):
        """Handle events that occur on this screen."""
        raise NotImplementedError
