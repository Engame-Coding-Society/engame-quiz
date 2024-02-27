from screens.screen import Screen
from screens.text import Text
from screens.backends import EventType
import pygame_gui
import pygame
import leaderboard


class PlayerPromptScreen(Screen):
    def __init__(self, size, clock, loader, next_action):
        super().__init__(size, clock, loader)
        self.next_action = next_action
        self.entry_value = ""
        self.init_ui()

    def init_ui(self):
        self.title = Text(pygame.Rect(0, 0, self.screen_size[0], 50), "You've completed the Engame quiz!", self.ui)
        self.label = pygame_gui.elements.UILabel(pygame.Rect(0, 150, self.screen_size[0], 50), "Enter a player name:", self.ui)
        self.entry = pygame_gui.elements.UITextEntryLine(pygame.Rect(50, 200, self.screen_size[0]-100, 50), self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect(0, 250, self.screen_size[0], 100), "Next",self.ui)

    def process_screen_events(self, event):
        if event.type == EventType.ENTRY_VALUE_CHANGED:
            self.entry_value = event.value
        if event.type == EventType.BUTTON_PRESSED:
            self.next_action(self.entry_value)
        self.ui.process_events(event)


class PlacementScreen(Screen):
    def __init__(self, screen_size, clock, loader, result, next_action):
        super().__init__(screen_size, clock, loader)
        self.result = result
        self.next_action = next_action
        self.init_ui()

    def init_ui(self):
        self.title_label = pygame_gui.elements.UILabel(
            pygame.Rect(0, 100, self.screen_size[0], 25), f"Congrats {self.result['name']}!", self.ui)
        self.place_label = pygame_gui.elements.UILabel(
            pygame.Rect(0, 200, self.screen_size[0], 100), f"You're earned {self.result['score']} points!", self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect(0, 400, self.screen_size[0], 100), "Go to Leaderboard", self.ui)

    def process_screen_events(self, event):
        if event.type == EventType.BUTTON_PRESSED:
            self.next_action()
        self.ui.process_events(event)


class LeaderboardScreen(Screen):
    def __init__(self, screen_size, clock, loader):
        super().__init__(screen_size, clock, loader)
        top_players_resp = leaderboard.get_top()
        self.top_players = top_players_resp["data"] if top_players_resp["success"] else [{"name": "Error", "score": top_players_resp["cause"]}]

    def init_ui(self):
        self.title = pygame_gui.elements.UILabel(
            pygame.Rect(0, 25, self.screen_size[0], 50), "Leaderboard", self.ui)
        self.name_column = pygame_gui.elements.UILabel(pygame.Rect(25, 100, 120, 50), "Player")
        self.score_column = pygame_gui.elements.UILabel(pygame.Rect(200, 100, 120, 50), "Score")

        for pi in range(len(self.top_players)):
            pygame_gui.elements.UILabel(pygame.Rect(25,  150+pi*25, 120, 50), self.top_players[pi]["name"], self.ui)
            pygame_gui.elements.UILabel(pygame.Rect(200, 150+pi*25, 120, 50), str(self.top_players[pi]["score"]), self.ui)

    def process_screen_events(self, event):
        self.ui.process_events(event)
