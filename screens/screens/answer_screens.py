from screens.screen import Screen


class CorrectScreen(Screen):
    def __init__(self, screen_size, clock, question):
        super().__init__(screen_size, clock)
        self.question = question

    def draw_screen(self, surface):
        super().draw_screen(surface)
        self.question_text.set_text('Correct!')
        self.next_button.set_text('Next question')
    def next_button_action(self):
        nav_to_question_screen()

class FailScreen(Screen):
    def __init__(self, screen_size, clock, question, correct_answer):
        super().__init__(screen_size, clock)
        self.question = question
        self.correct_answer = correct_answer

    def draw_screen(self, surface):
        super().draw_screen(surface)
        self.question_text.set_text('Wrong! The correct answer was:' + self.correct_answer)
        self.next_button.set_text('Next question')
    def next_button_action(self):
        nav_to_question_screen()