import pygame
from enum import Enum
from pygame_gui.core import IncrementalThreadedResourceLoader
from question import Question
from screens import *
from screens.screen import Screen


class Screens(Enum):
    START = 0
    QUESTION = 1
    CORRECT = 2
    FAIL = 3
    LEADERBOARD = 4


SCREEN_SIZE = (800, 600)
current_screen = Screens.QUESTION
last_screen = Screens.START
current_question = 0


def nav_to_answer_screen(q: Question, a: int):
    global current_screen
    global last_screen
    if q.is_correct(a):
        current_screen = Screens.CORRECT  # Index of CurrentScreen
    else:
        current_screen = Screens.FAIL  # Index of FailScreen
    last_screen = Screens.QUESTION


def init_screens(clock, loader):
    return [
        Screen(SCREEN_SIZE, clock, loader),
        QuestionScreen(SCREEN_SIZE, clock, questions[current_question], loader, nav_to_answer_screen),
        CorrectScreen(SCREEN_SIZE, clock, questions[current_question], loader, nav_to_question_screen),
        FailScreen(SCREEN_SIZE, clock, questions[current_question].options[0],
                   loader, nav_to_question_screen),
        Screen(SCREEN_SIZE, clock, loader)
    ]


def nav_to_question_screen(clock, loader):
    global current_screen
    global last_screen
    global current_question
    global screen_instances

    last_screen = current_screen
    current_screen = Screens.QUESTION
    current_question += 1

    screen_instances = init_screens(clock, loader)


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

    screen_instances = init_screens(clock, res_loader)

    # # Main game-loop
    is_running = True
    while is_running:
        delta_time = clock.tick(60) / 1000.0
        # ## Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ### Shutdown algorythm
                is_running = False
            screen_instances[current_screen.value].process_screen_events(event)
        # ## Update the UI
        screen_instances[current_screen.value].update(delta_time)
        window_surface.blit(bg, (0, 0))
        screen_instances[current_screen.value].draw_screen(window_surface)

        pygame.display.update()
