from screens.screen import Screen
from screens.backends import EventType
import pygame, pygame_gui


class CorrectScreen(Screen):
    def __init__(self, screen_size, clock, loader, question, next_button_action):
        super().__init__(screen_size, clock, loader)
        self.question = question
        self.next_button_action = next_button_action

    def init_ui(self):
        self.question_text = pygame_gui.elements.UILabel(
            pygame.Rect((0, 50), (self.screen_size[0], 100)), "Correct!", self.ui
        )
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect(0, int(self.screen_size[1] / 2) - 50, self.screen_size[0], 100), "Next", self.ui)

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            self.next_button_action()
        self.ui.process_events(event)


class FailScreen(Screen):
    def __init__(self, screen_size, clock, loader, correct_answer, next_button_action):
        super().__init__(screen_size, clock, loader)
        self.correct_answer = correct_answer
        self.next_button_action = next_button_action

    def init_ui(self):
        self.question_title = pygame_gui.elements.UILabel(pygame.Rect((0, 0), (self.screen_size[0], 25)), "Wrong!", self.ui)
        self.answer_title = pygame_gui.elements.UILabel(pygame.Rect((0, 25), (self.screen_size[0], 25)),"The correct answer is", self.ui)
        self.correct_answer_label = pygame_gui.elements.UILabel(pygame.Rect((0, 50), (self.screen_size[0], 50)), self.correct_answer, self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect((0, int(self.screen_size[1] / 2) - 25), (self.screen_size[0], 100)), "Next", self.ui)

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            self.next_button_action()
        self.ui.process_events(event)

    def draw_screen(self, surface):
        super().draw_screen(surface)
