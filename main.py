import pygame
from enum import Enum
from pygame_gui.core import IncrementalThreadedResourceLoader
from question import Question
from screens import *
from score import ScoreManager
import leaderboard


class Screens(Enum):
    START = 0
    QUESTION = 1
    CORRECT = 2
    FAIL = 3
    LEADERBOARD_PLAYER_PROMPT = 4
    LEADERBOARD_PLACEMENT = 5
    LEADERBOARD = 6


SCREEN_SIZE = (350, 500)
current_screen = Screens.START
last_screen = Screens.START

current_question = -1
player_result = {"name": "unkown", "score": 0}
scores = ScoreManager()


def init_screen(game_clock, loader):
    match current_screen:
        case Screens.START:
            return WelcomeScreen(SCREEN_SIZE, game_clock, loader, nav_to_question_screen)
        case Screens.QUESTION:
            return QuestionScreen(SCREEN_SIZE, game_clock, loader,
                                  questions[current_question], nav_to_answer_screen)
        case Screens.CORRECT:
            return CorrectScreen(SCREEN_SIZE, game_clock, loader,
                                 questions[current_question], nav_to_question_screen)
        case Screens.FAIL:
            return FailScreen(SCREEN_SIZE, game_clock, loader,
                              questions[current_question].options[0], nav_to_question_screen)
        case Screens.LEADERBOARD_PLAYER_PROMPT:
            return PlayerPromptScreen(SCREEN_SIZE, game_clock, loader, nav_to_results)
        case Screens.LEADERBOARD_PLACEMENT:
            return PlacementScreen(SCREEN_SIZE, game_clock, loader, player_result, nav_to_leaderboard)
        case Screens.LEADERBOARD:
            return LeaderboardScreen(SCREEN_SIZE, game_clock, loader)
        case _:
            raise NotImplementedError("You haven't implemented your screen yet!")


def nav_to_answer_screen(game_clock: pygame.time.Clock, loader: IncrementalThreadedResourceLoader,
                         q: Question, a: int):
    global current_screen
    global last_screen
    global scores
    global screen_instance
    if q.is_correct(a):
        current_screen = Screens.CORRECT  # Index of CurrentScreen
        scores.increment() 
    else:
        current_screen = Screens.FAIL  # Index of FailScreen
    last_screen = Screens.QUESTION
    screen_instance = init_screen(game_clock, loader)


def nav_to_question_screen(clock, loader):
    global current_screen
    global last_screen
    global current_question
    global screen_instance

    last_screen = current_screen
    if (current_question+1) < len(questions):
        current_screen = Screens.QUESTION
        current_question += 1
    else:
        current_screen = Screens.LEADERBOARD_PLAYER_PROMPT
    screen_instance = init_screen(clock, loader)


def nav_to_results(clock, res_loader, result):
    global current_screen
    global last_screen
    global player_result
    global screen_instance

    last_screen = current_screen
    current_screen = Screens.LEADERBOARD_PLACEMENT

    response = leaderboard.save_player(result, scores.get_score())
    if not response["success"]:
        print("Couldn't save the player score")
        return
    player_result = response["data"]
    screen_instance = init_screen(clock, res_loader)
    

def nav_to_leaderboard(clock, res_loader):
    global current_screen
    global last_screen
    global screen_instance

    last_screen = current_screen
    current_screen = Screens.LEADERBOARD

    screen_instance = LeaderboardScreen(SCREEN_SIZE, clock, res_loader)


if __name__ == '__main__':
    # # Asset loading
    questions = Question.load("tests/questions.yml")
    # # PyGame display init
    pygame.init()
    pygame.display.set_caption('Engame Quiz')
    window_surface = pygame.display.set_mode(SCREEN_SIZE)

    # ## Background
    BG_COLOR = pygame.Color("#ebebeb")
    bg = pygame.Surface(SCREEN_SIZE)
    bg.fill(BG_COLOR)
    # ## UI Init
    res_loader = IncrementalThreadedResourceLoader()
    clock = pygame.time.Clock()

    screen_instance = init_screen(clock, res_loader)

    # # Main game-loop
    is_running = True
    while is_running:
        delta_time = clock.tick(60) / 1000.0
        # ## Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ### Shutdown algorythm
                is_running = False
            screen_instance.process_screen_events(event)
        # ## Update the UI
        screen_instance.update(delta_time)
        window_surface.fill(BG_COLOR)
        window_surface.blit(bg, (0, 0))
        screen_instance.draw_screen(window_surface)

        pygame.display.update()
