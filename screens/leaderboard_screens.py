from screens.screen import Screen
import pygame_gui
import pygame
import leaderboard


class PlayerPromptScreen(Screen):
    def __init__(self, size, clock, loader, next_action):
        super().__init__(size, clock, loader)
        self.next_action = next_action
        self.loader = loader
        self.init_ui()

    def init_ui(self):
        self.label = pygame_gui.elements.UILabel(pygame.Rect(200, 200, 150, 50), "Enter a player name:", self.ui)
        self.entry = pygame_gui.elements.UITextEntryLine(pygame.Rect(200, 350, 150, 50), self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect(300, 500, 100, 150), "Next" ,self.ui)

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.next_action(self.clock, self.loader, self.entry.get_text())
        self.ui.process_events(event)


class PlacementScreen(Screen):
    def __init__(self, screen_size, clock, loader, result, next_action):
        super().__init__(screen_size, clock, loader)
        self.loader = loader
        self.result = result
        self.next_action = next_action
        self.init_ui()

    def init_ui(self):
        self.title_label = pygame_gui.elements.UILabel(
            pygame.Rect(0, 200, 800, 100), f"Congrats {self.result['name']}!", self.ui)
        self.place_label = pygame_gui.elements.UILabel(
            pygame.Rect(0, 300, 800, 100), f"You're earned the {self.result['score']}rd place on the leaderboard!", self.ui)
        self.next_button = pygame_gui.elements.UIButton(pygame.Rect(350, 400, 150, 50), "Next", self.ui)

    def process_screen_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.next_action(self.clock, self.loader)
        self.ui.process_events(event)


class LeaderboardScreen(Screen):
    def __init__(self, screen_size, clock, loader):
        super().__init__(screen_size, clock, loader)
        self.top_players = leaderboard.get_top()["data"]
        self.init_ui()

    def init_ui(self):
        self.title = pygame_gui.elements.UILabel(
            pygame.Rect(0, 50, 800, 50), "Leaderboard", self.ui
        )
        self.name_column = pygame_gui.elements.UILabel(pygame.Rect(200, 250, 120, 50), "Player")
        self.score_column = pygame_gui.elements.UILabel(pygame.Rect(600, 250, 120, 50), "Score")

        for pi in range(len(self.top_players)):
            pygame_gui.elements.UILabel(pygame.Rect(200, 300+pi*25, 120, 50), self.top_players[pi]["name"], self.ui)
            pygame_gui.elements.UILabel(pygame.Rect(600, 300+pi*25, 120, 50), str(self.top_players[pi]["score"]), self.ui)

    def process_screen_events(self, event):
        self.ui.process_events(event)

    def draw_screen(self, surface):
        self.ui.draw_screen(surface)