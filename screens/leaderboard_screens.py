from screens.screen import Screen
import pygame_gui
import pygame


class PlayerPromptScreen(Screen):
    def __init__(self, size, mobile, clock, loader, next_action):
        super().__init__(size, mobile, clock, loader)
        self.next_action = next_action
        self.loader = loader
        self.init_ui()

    def init_ui(self):
        self.label = pygame_gui.elements.UILabel(pygame.Rect(200, 200, 150, 50), "Enter a player name:", self.ui)
        self.entry = pygame_gui.elements.UITextEntryLine(pygame.Rect(200, 350, 150, 50), self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect(300, 500, 100, 150), "Next" ,self.ui)

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.next_action(self.clock, self.next_action, self.entry.get_text())
        self.ui.process_events(event)

