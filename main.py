import pygame, asyncio
from enum import Enum
from pygame_gui.core import IncrementalThreadedResourceLoader
from question import Question
from score import ScoreManager
from screens import *
from screens.backends import RENDERER
import leaderboard, randomization


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
# # Asset loading
questions = randomization.randomize_array(Question.load("tests/questions.yml"))
current_question = -1
player_result = {"name": "unkown", "score": 0}
scores = ScoreManager()
# ## UI Init
res_loader = IncrementalThreadedResourceLoader()
clock = pygame.time.Clock()


def init_screen():
    screen = construct_screen()
    RENDERER.init_ui(screen)
    return screen


def construct_screen():
    match current_screen:
        case Screens.START:
            return WelcomeScreen(SCREEN_SIZE, clock, res_loader, nav_to_question_screen)
        case Screens.QUESTION:
            return QuestionScreen(SCREEN_SIZE, clock, res_loader,
                                  questions[current_question], nav_to_answer_screen)
        case Screens.CORRECT:
            return CorrectScreen(SCREEN_SIZE, clock, res_loader,
                                 questions[current_question], nav_to_question_screen)
        case Screens.FAIL:
            return FailScreen(SCREEN_SIZE, clock, res_loader,
                              questions[current_question].options[0], nav_to_question_screen)
        case Screens.LEADERBOARD_PLAYER_PROMPT:
            return PlayerPromptScreen(SCREEN_SIZE, clock, res_loader, nav_to_results)
        case Screens.LEADERBOARD_PLACEMENT:
            return PlacementScreen(SCREEN_SIZE, clock, res_loader, player_result, nav_to_leaderboard)
        case Screens.LEADERBOARD:
            return LeaderboardScreen(SCREEN_SIZE, clock, res_loader)
        case _:
            raise NotImplementedError("You haven't implemented your screen yet!")


def nav_to_answer_screen(q: Question, a: int):
    global current_screen
    global scores
    global screen_instance
    if q.is_correct(a):
        current_screen = Screens.CORRECT  # Index of CurrentScreen
        scores.increment() 
    else:
        current_screen = Screens.FAIL  # Index of FailScreen
    screen_instance = init_screen()


def nav_to_question_screen():
    global current_screen
    global current_question
    global screen_instance

    if (current_question+1) < len(questions):
        current_screen = Screens.QUESTION
        current_question += 1
    else:
        current_screen = Screens.LEADERBOARD_PLAYER_PROMPT
    screen_instance = init_screen()


def nav_to_results(result):
    global current_screen
    global player_result
    global screen_instance

    current_screen = Screens.LEADERBOARD_PLACEMENT

    response = leaderboard.save_player(result, scores.get_score())
    if not response["success"]:
        print("Couldn't save the player score")
    else:
        player_result = response["data"]
    screen_instance = init_screen()
    

def nav_to_leaderboard():
    global current_screen
    global screen_instance

    current_screen = Screens.LEADERBOARD
    screen_instance = init_screen()


screen_instance = None


async def main():
    global screen_instance
    screen_instance = init_screen()
    # # Main game-loop
    is_running = True
    while is_running:
        RENDERER.handle_events()
        RENDERER.update()
        RENDERER.draw()
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
