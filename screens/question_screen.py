from screens.screen import Screen
import pygame_gui
import pygame


class QuestionScreen(Screen):
    def __init__(self, screen_size, clock, loader, question, on_got_answer):
        super().__init__(screen_size, clock, loader)
        self.question = question
        self.loader = loader
        self.on_got_answer = on_got_answer
        self.init_ui()

    def init_ui(self):
        self.question_text = pygame_gui.elements.UILabel(
            pygame.Rect((0, 0), (self.screen_size[0], 100)), self.question.question, self.ui
        )
        # #### Answer buttons
        width = self.screen_size[0]
        self.answer_buttons = [
            pygame_gui.elements.UIButton(pygame.Rect(0, 225, self.screen_size[0], 50), self.question.options[0], self.ui),
            pygame_gui.elements.UIButton(pygame.Rect(0, 300, self.screen_size[0], 50), self.question.options[1], self.ui),
            pygame_gui.elements.UIButton(pygame.Rect(0, 375, self.screen_size[0], 50), self.question.options[2], self.ui),
            pygame_gui.elements.UIButton(pygame.Rect(0, 450, self.screen_size[0], 50), self.question.options[3], self.ui)
        ]

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for bi in range(len(self.answer_buttons)):
                button = self.answer_buttons[bi]
                if button == event.ui_element:
                    self.on_got_answer(self.clock, self.loader, self.question, bi)
        self.ui.process_events(event)

    def draw_screen(self, surface):
        super().draw_screen(surface)