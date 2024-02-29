from screens.backends import Rect
from screens.backends.components import Entry, Button, Text
from screens.backends.renderer import Renderer
from screens.backends.events import ButtonPressedEvent, EntryValueChangedEvent
from screens.screen import Screen
from screens.backends.web.components import WebText, WebButton
import web, json


class WebRenderer(Renderer):
    def __init__(self):
        super().__init__()
        self.rendered = False
        self.__components = []

    def init_ui(self, screen: Screen) -> None:
        self.__components = []
        self.rendered = False
        self.screen = screen
        self.screen.init_ui(self)

    def draw(self):
        if self.rendered:
            return
        print("currently drawing!")
        html_content = []
        for component in self.__components:
            html_content.append(component.generate())
        web.render(json.dumps(html_content))
        self.rendered = True

    def handle_events(self):
        for event in web.get_events():
            self.screen.process_screen_events(self._serialize_event(event))
            print(event)

    def __find_component(self, id: str):
        for component in self.__components:
            if component.id == id:
                return component
        return None

    def _serialize_event(self, event, *args):
        component = self.__find_component(event.id)
        match event.type:
            case "button_pressed":
                return ButtonPressedEvent(component)
            case "entry_changed":
                return EntryValueChangedEvent(component, event.value)
            case _:
                raise NotImplementedError(f"You haven't implemented {event.type} event!")

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
