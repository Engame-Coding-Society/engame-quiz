import asyncio
from enum import Enum
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
questions = randomization.randomize_array(Question.load("questions.yml"))
current_question = -1
player_result = {"name": "unkown", "score": 0}
scores = ScoreManager()


def init_screen():
    screen = construct_screen()
    RENDERER.init_ui(screen)
    return screen


def construct_screen():
    match current_screen:
        case Screens.START:
            return WelcomeScreen(nav_to_question_screen)
        case Screens.QUESTION:
            return QuestionScreen(questions[current_question], nav_to_answer_screen)
        case Screens.CORRECT:
            return CorrectScreen(nav_to_question_screen)
        case Screens.FAIL:
            return FailScreen(questions[current_question].options[0], nav_to_question_screen)
        case Screens.LEADERBOARD_PLAYER_PROMPT:
            return PlayerPromptScreen(nav_to_results)
        case Screens.LEADERBOARD_PLACEMENT:
            return PlacementScreen(player_result, nav_to_leaderboard)
        case Screens.LEADERBOARD:
            return LeaderboardScreen()
        case _:
            raise NotImplementedError("You haven't implemented your screen yet!")


def nav_to_answer_screen(q: Question, a: str):
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


def nav_to_results(player_name):
    global current_screen
    global player_result
    global screen_instance

    current_screen = Screens.LEADERBOARD_PLACEMENT
    if player_name != "":
        response = leaderboard.save_player(player_name, scores.get_score())
        if not response["success"]:
            print("Couldn't save the player score")
        else:
            player_result = response["data"]
    else:
        player_result["score"] = scores.get_score()
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
