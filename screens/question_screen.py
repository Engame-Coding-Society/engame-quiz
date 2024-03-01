from screens.screen import Screen
from screens.backends import EventType, Rect
from randomization import randomize_array


class QuestionScreen(Screen):
    def __init__(self, question, on_got_answer):
        super().__init__()
        self.question = question
        self.on_got_answer = on_got_answer

    def init_ui(self, renderer):
        self.question_text = renderer.text(Rect("0px", "0px", "100%", "100px"),
                                  self.question.question)
        # #### Answer buttons
        random_options = randomize_array(self.question.options)
        self.answer_buttons = [
            renderer.button(Rect("0px", "225px", "100%", "150px"), random_options[0], "answer_1"),
            renderer.button(Rect("0px", "400px", "100%", "150px"), random_options[1], "answer_2"),
            renderer.button(Rect("0px", "550px", "100%", "150px"), random_options[2], "answer_3"),
            renderer.button(Rect("0px", "725px", "100%", "150px"), random_options[3], "answer_4")
        ]

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            for bi in range(len(self.answer_buttons)):
                button = self.answer_buttons[bi]
                if button == event.component:
                    self.on_got_answer(self.question, button.text)
