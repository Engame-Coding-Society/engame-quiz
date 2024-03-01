from screens.screen import Screen
from screens.backends import EventType, Rect


class WelcomeScreen(Screen):
    def __init__(self, set_callback):
        super().__init__()
        self.set_callback = set_callback

    def init_ui(self, renderer):
        # Title label
        self.title_label = renderer.text(Rect("0px", "100px", "100%", "75px"), "Engame Quiz")
        # Start quiz button
        self.start_quiz_button = renderer.button(Rect("0px", "450px", "100%", "150px"), "Start Quiz", "start_btn")

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            if event.component == self.start_quiz_button:
                self.set_callback()
