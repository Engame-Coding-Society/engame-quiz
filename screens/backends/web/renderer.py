from screens.backends import Rect
from screens.backends.components import Entry, Button, Text
from screens.backends.renderer import Renderer
from screens.screen import Screen
from screens.backends.web.components import WebText, WebButton
import web


class WebRenderer(Renderer):
    def __init__(self):
        super().__init__()
        self.rendered = False
        self.__components = []

    def init_ui(self, screen: Screen) -> None:
        self.rendered = False
        self.screen = screen
        self.screen.init_ui(self)

    def draw(self):
        if self.rendered:
            return
        print("currently drawing!")
        html_content = ""
        for component in self.__components:
            html_content += component.generate()
        web.render(html_content)
        self.rendered = True

    def handle_events(self):
        pass

    def _serialize_event(self, event, *args):
        pass

    def update(self):
        pass

    def __add_component(self, component):
        self.__components.append(component)
        return component

    def text(self, rect: Rect, text: str, id: str = None, object_class: str = None) -> Text:
        return self.__add_component(WebText(rect, text, id, object_class))

    def button(self, rect: Rect, text: str, id: str = None, object_class: str = None) -> Button:
        return self.__add_component(WebButton(rect, text, id, object_class))

    def entry(self, rect: Rect, id: str, placeholder: str = "", object_class: str = None) -> Entry:
        pass
