from screens.screen import Screen
from screens.backends import EventType, Rect
import leaderboard


class PlayerPromptScreen(Screen):
    def __init__(self, next_action):
        super().__init__()
        self.next_action = next_action
        self.entry_value = ""

    def init_ui(self, renderer):
        self.title = renderer.text(Rect("0px", "0px", "100%", "50px"), "You've completed the Engame quiz!")
        self.label = renderer.text(Rect("0px", "150px", "100%", "50px"), "Enter a player name:")
        self.entry = renderer.entry(Rect("0px", "400px", "100%", "50px"), "player_input")
        self.next_button = renderer.button(Rect("0%", "550px", "100%", "50px"), "Next", "next_btn")

    def process_screen_events(self, event):
        if event.type == EventType.ENTRY_VALUE_CHANGED:
            self.entry_value = event.value
        if event.type == EventType.BUTTON_PRESSED:
            self.next_action(self.entry_value)


class PlacementScreen(Screen):
    def __init__(self, result, next_action):
        super().__init__()
        self.result = result
        self.next_action = next_action

    def init_ui(self, renderer):
        renderer.text(Rect("0px", "100px", "100%", "100px"),
                      f"Congrats {self.result['name']}!\nYou're earned {self.result['score']} points!")
        renderer.button(Rect("0px", "48%", "100%", "100px"), "Go to Leaderboard", "next_btn")

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            self.next_action()


class LeaderboardScreen(Screen):
    def __init__(self):
        super().__init__()
        top_players_resp = leaderboard.get_top()
        self.top_players = top_players_resp["data"] if top_players_resp["success"] else [{"name": "Error", "score": top_players_resp["cause"]}]

    def init_ui(self, renderer):
        renderer.text(Rect("0px", "25px", "100%", "50px"), "Leaderboard", "leaderboard")
        renderer.text(Rect("10%", "250px", "40%", "50px"), "Player", object_class="leaderboard_header")
        renderer.text(Rect("60%", "250px", "40%", "50px"), "Score", object_class="leaderboard_header")

        for pi in range(len(self.top_players)):
            renderer.text(Rect("10%", f"{300+pi*50}px", "40%", "50px"), self.top_players[pi]["name"])
            renderer.text(Rect("60%", f"{300+pi*50}px", "40%", "50px"), str(self.top_players[pi]["score"]))

    def process_screen_events(self, event):
        pass
