from screens.backends import Renderer, ButtonPressedEvent, EntryValueChangedEvent
import pygame, pygame_gui


class PygameRenderer(Renderer):
    SCREEN_SIZE = (350, 500)
    BG_COLOR = pygame.Color("#ebebeb")

    def __init__(self):
        super().__init__()
        self.__init_pygame()
        self.clock = pygame.time.Clock()
        self.loader = pygame_gui.core.IncrementalThreadedResourceLoader()
        self.ui_manager = pygame_gui.UIManager(
            PygameRenderer.SCREEN_SIZE, "assets/theme.json", resource_loader=self.loader)
        self.delta_time = 0

    def __init_pygame(self):
        # # PyGame display init
        pygame.init()
        pygame.display.set_caption('Engame Quiz')
        self.window_surface = pygame.display.set_mode(PygameRenderer.SCREEN_SIZE)

        # ## Background
        self.bg = pygame.Surface(PygameRenderer.SCREEN_SIZE)
        self.bg.fill(PygameRenderer.BG_COLOR)

    def draw(self):
        self.window_surface.fill(PygameRenderer.BG_COLOR)
        self.window_surface.blit(self.bg, (0, 0))
        self.screen.draw_screen(self.window_surface)
        pygame.display.update()

    def handle_events(self):
        self.delta_time = self.clock.tick(60) / 1000.0
        # ## Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ### Shutdown algorythm
                exit(0)
            self.screen.process_screen_events(self._serialize_event(event))

    def _serialize_event(self, event, *args):
        match event.type:
            case pygame_gui.UI_BUTTON_PRESSED:
                return ButtonPressedEvent(event.ui_element)
            case pygame_gui.UI_TEXT_ENTRY_CHANGED:
                return EntryValueChangedEvent(event.ui_element, event.text)
            case _:
                # TODO: remove this opportunity after the component implementation
                return event

    def update(self):
        self.screen.update(self.delta_time)
