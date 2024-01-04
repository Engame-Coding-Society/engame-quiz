from screens.screen import Screen


class QuestionScreen(Screen):
    def __init__(self, screen_size, clock, question):
        super().__init__(screen_size, clock)
        self.question = question

    def init_ui(self):
        super().init_ui()

        # ###Actual User Interface
        self.question_text = pygame_gui.elements.UILabel(
            pygame.Rect((0, 0), (800, 100)), self.question.question, self.ui
        )
        # #### Answer buttons
        self.answer0_button = pygame_gui.elements.UIButton(
            pygame.Rect(50, 350, 250, 100), self.question.options[0], self.ui
        )
        self.answer1_button = pygame_gui.elements.UIButton(
            pygame.Rect(500, 350, 250, 100), self.question.options[1], self.ui
        )
        self.answer2_button = pygame_gui.elements.UIButton(
            pygame.Rect(50, 475, 250, 100), self.question.options[2], self.ui
        )
        self.answer3_button = pygame_gui.elements.UIButton(
            pygame.Rect(500, 475, 250, 100), self.question.options[3], self.ui
        )

    def process_screen_events(self, event):
        super().process_screen_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            idx = -10
            element = event.ui_element
            if element == self.answer0_button:
                idx = 0
            elif element == self.answer1_button:
                idx = 1
            elif element == self.answer2_button:
                idx = 2
            elif element == self.answer3_button:
                idx = 3
            print(self.question.options[idx])

    def draw_screen(self, surface):
        super().draw_screen(surface)

