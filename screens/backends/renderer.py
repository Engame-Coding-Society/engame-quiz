from screens.screen import Screen
from screens.backends.components import Rect, Text, Button, Entry
from abc import abstractmethod


class Renderer:
    def __init__(self):
        self.screen: Screen = None

    @abstractmethod
    def init_ui(self, screen: Screen) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    @abstractmethod
    def handle_events(self):
        raise NotImplementedError

    @abstractmethod
    def _serialize_event(self, event, *args):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def text(self, rect: Rect, text: str, id: str=None, object_class: str=None) -> Text:
        raise NotImplementedError

    @abstractmethod
    def button(self, rect: Rect, text: str, id: str=None, object_class: str=None) -> Button:
        raise NotImplementedError

    @abstractmethod
    def entry(self, rect: Rect,  id: str, placeholder: str="", object_class: str=None) -> Entry:
        raise NotImplementedError
    