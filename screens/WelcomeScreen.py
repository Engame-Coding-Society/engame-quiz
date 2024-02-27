from screens.screen import Screen
from screens.backends import EventType, ButtonPressedEvent
import pygame_gui
import pygame


class WelcomeScreen(Screen):
    def __init__(self, screen_size, clock, loader, set_callback):
        super().__init__(screen_size, clock, loader)
        self.set_callback = set_callback

    def init_ui(self):
        # Title label
        self.title_label = pygame_gui.elements.UILabel(
            pygame.Rect((0, 0), (self.screen_size[0], 75)), "Engame Quiz", self.ui
        )

        # Start quiz button
        self.start_quiz_button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 100), (self.screen_size[0], 175)), "Start Quiz", self.ui
        )

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            if event.component == self.start_quiz_button:
                self.set_callback()
        self.ui.process_events(event)
