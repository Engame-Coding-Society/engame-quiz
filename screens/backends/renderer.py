from screens.screen import Screen
from abc import abstractmethod


class Renderer:
    def __init__(self):
        self.screen: Screen = None

    def init_ui(self, screen: Screen) -> None:
        self.screen = screen
        self.screen.init_ui()

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    @abstractmethod
    def handle_events(self):
        raise NotImplementedError

    @abstractmethod
    def serialize_event(self, *args):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    