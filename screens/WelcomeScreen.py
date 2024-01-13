from screens.screen import Screen
import pygame_gui
import pygame


class WelcomeScreen(Screen):
    def __init__(self, screen_size, clock, loader, set_callback):
        super().__init__(screen_size, clock, loader)
        self.set_callback = set_callback
        self.loader = loader
        self.init_ui()

    def init_ui(self):
        # Title label
        self.title_label = pygame_gui.elements.UILabel(
            pygame.Rect((0, 0), (800, 100)), "Engame Quiz", self.ui
        )

        # Start quiz button
        self.start_quiz_button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 100), (800, 100)), "Start Quiz", self.ui
        )

    def start_quiz(self):
        self.set_callback()

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_quiz_button:
                self.set_callback(self.clock, self.loader)
        self.ui.process_events(event)

    def draw_screen(self, surface):
        self.ui.draw_ui(surface)
