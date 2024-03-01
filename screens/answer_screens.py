from screens.screen import Screen
from screens.backends import EventType, Rect


class CorrectScreen(Screen):
    def __init__(self, next_button_action):
        super().__init__()
        self.next_button_action = next_button_action

    def init_ui(self, renderer):
        self.question_text = renderer.text(
            Rect("0px", "100px", "100%", "100px"), "Correct!" )
        self.next_button = renderer.button(Rect("0px", "45%", "100%", "100px"), "Next", "next_btn")

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            self.next_button_action()


class FailScreen(Screen):
    def __init__(self, correct_answer, next_button_action):
        super().__init__()
        self.correct_answer = correct_answer
        self.next_button_action = next_button_action

    def init_ui(self, renderer):
        self.question_title = renderer.text(Rect("0px","100px", "100%", "100px"), f"Wrong!\nThe correct answer is\n{self.correct_answer}")
        self.next_button = renderer.button(Rect("0px", "45%", "100%", "100px"), "Next", "next_btn")

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            self.next_button_action()
