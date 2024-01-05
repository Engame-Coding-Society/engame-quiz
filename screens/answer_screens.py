from screens.screen import Screen
import pygame, pygame_gui


class CorrectScreen(Screen):
    def __init__(self, screen_size, clock, question, loader, next_button_action):
        super().__init__(screen_size, clock, loader)
        self.question = question
        self.next_button_action = next_button_action
        self.loader = loader
        self.init_ui()

    def init_ui(self):
        self.question_text = pygame_gui.elements.UILabel(
            pygame.Rect((0, 0), (800, 100)), "Correct!", self.ui
        )
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect((0, 100), (800, 100)), "Next", self.ui)

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.next_button_action(self.clock, self.loader)
        self.ui.process_events(event)


class FailScreen(Screen):
    def __init__(self, screen_size, clock, correct_answer, loader, next_button_action):
        super().__init__(screen_size, clock, loader)
        self.correct_answer = correct_answer
        self.next_button_action = next_button_action
        self.loader = loader
        self.init_ui()

    def init_ui(self):
        self.question_text = pygame_gui.elements.UILabel(pygame.Rect((0, 0), (800, 100)), "Wrong! The correct answer is " + self.correct_answer, self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect((0, 100), (800, 100)), "Next", self.ui)

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.next_button_action(self.clock, self.loader)
        self.ui.process_events(event)

    def draw_screen(self, surface):
        super().draw_screen(surface)
