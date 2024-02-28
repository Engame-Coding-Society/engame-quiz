from screens.backends.renderer import Renderer
from screens.backends.events import ButtonPressedEvent, EntryValueChangedEvent
from screens.backends.pygame.components import PygameText, PygameButton, PygameEntry
import pygame, pygame_gui
from screens.backends.pygame.constants import SCREEN_SIZE
from screens.backends.components import Rect, Entry, Button, Text
from screens.screen import Screen


class PygameRenderer(Renderer):
    BG_COLOR = pygame.Color("#ebebeb")

    def __init__(self):
        super().__init__()
        self.__init_pygame()
        self.clock = pygame.time.Clock()
        self.loader = pygame_gui.core.IncrementalThreadedResourceLoader()
        self.delta_time = 0
        self.__components = []

    def __init_pygame(self):
        # # PyGame display init
        pygame.init()
        pygame.display.set_caption('Engame Quiz')
        self.window_surface = pygame.display.set_mode(SCREEN_SIZE)

        # ## Background
        self.bg = pygame.Surface(SCREEN_SIZE)
        self.bg.fill(PygameRenderer.BG_COLOR)

    def __init_ui_manager(self):
        self.ui_manager = pygame_gui.UIManager(
            SCREEN_SIZE, "assets/theme.json", resource_loader=self.loader)

    def init_ui(self, screen: Screen) -> None:
        self.__init_ui_manager()
        self.__components = []
        self.screen = screen
        self.screen.init_ui(self)

    def draw(self):
        self.window_surface.fill(PygameRenderer.BG_COLOR)
        self.window_surface.blit(self.bg, (0, 0))
        self.ui_manager.draw_ui(self.window_surface)
        pygame.display.update()

    def handle_events(self):
        self.delta_time = self.clock.tick(60) / 1000.0
        # ## Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ### Shutdown algorythm
                exit(0)
            screen_event = self._serialize_event(event)
            self.screen.process_screen_events(screen_event) if screen_event is not None else None
            self.ui_manager.process_events(event)

    def __find_component(self, event):
        for component in self.__components:
            if component.id == event.ui_element.object_ids[0]:
                return component
        return None

    def _serialize_event(self, event, *args):
        match event.type:
            case pygame_gui.UI_BUTTON_PRESSED:
                return ButtonPressedEvent(self.__find_component(event))
            case pygame_gui.UI_TEXT_ENTRY_CHANGED:
                return EntryValueChangedEvent(self.__find_component(event), event.text)
            case _:
                return None

    def update(self):
        self.ui_manager.update(self.delta_time)

    def __add_component(self, component):
        self.__components.append(component)
        return component

    def text(self, rect: Rect, text: str, id: str = None, object_class: str = None) -> Text:
        return self.__add_component(PygameText(self.ui_manager, rect, text, id, object_class))

    def button(self, rect: Rect, text: str, id: str = None, object_class: str = None) -> Button:
        return self.__add_component(PygameButton(self.ui_manager, rect, text, id, object_class))

    def entry(self, rect: Rect, id: str, placeholder: str = None, object_class: str = None) -> Entry:
        return self.__add_component(PygameEntry(self.ui_manager, rect, placeholder, id, object_class))
