from screens.screen import Screen
import pygame_gui
import pygame


class QuestionScreen(Screen):
    def __init__(self, screen_size, clock, question, loader, on_got_answer):
        super().__init__(screen_size, clock, loader)
        self.question = question
        self.on_got_answer = on_got_answer
        self.init_ui()

    def init_ui(self):
        self.question_text = pygame_gui.elements.UILabel(
            pygame.Rect((0, 0), (800, 100)), self.question.question, self.ui
        )
        # #### Answer buttons
        self.answer_buttons = [
            pygame_gui.elements.UIButton(pygame.Rect(50, 350, 250, 100), self.question.options[0], self.ui),
            pygame_gui.elements.UIButton(pygame.Rect(500, 350, 250, 100), self.question.options[1], self.ui),
            pygame_gui.elements.UIButton(pygame.Rect(50, 475, 250, 100), self.question.options[2], self.ui),
            pygame_gui.elements.UIButton(pygame.Rect(500, 475, 250, 100), self.question.options[3], self.ui)
        ]

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for bi in range(len(self.answer_buttons)):
                button = self.answer_buttons[bi]
                if button == event.ui_element:
                    self.on_got_answer(self.question, bi)
                    print(bi)
        self.ui.process_events(event)

    def draw_screen(self, surface):
        super().draw_screen(surface)