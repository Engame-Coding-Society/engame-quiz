import pygame
import pygame_gui
from pygame_gui.core import ObjectID, IncrementalThreadedResourceLoader
from question import Question
from screens import *

SCREEN_SIZE = (800, 600)
current_screen = 0
last_screen = 0
current_question = 0

def nav_to_answer_screen(q: Question, a: int):
    global current_screen
    global last_screen
    if q.is_correct(a):
        current_screen = 1  # Index of CurrentScreen
    else:
        current_screen = 2  # Index of FailScreen
    last_screen = 0


def init_screens(clock, loader):
    return [
        QuestionScreen(SCREEN_SIZE, clock, questions[current_question], loader, nav_to_answer_screen),
        CorrectScreen(SCREEN_SIZE, clock, questions[current_question], loader, nav_to_question_screen),
        FailScreen(SCREEN_SIZE, clock, questions[current_question].options[0],
                   loader, nav_to_question_screen)
    ]


def nav_to_question_screen(clock, loader):
    global current_screen
    global last_screen
    global current_question
    global screen_instances

    last_screen = current_screen
    current_screen = 0
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
            screen_instances[current_screen].process_screen_events(event)
        # ## Update the UI
        screen_instances[current_screen].update(delta_time)
        window_surface.blit(bg, (0, 0))
        screen_instances[current_screen].draw_screen(window_surface)

        pygame.display.update()
