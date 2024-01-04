import pygame
import pygame_gui
from pygame_gui.core import ObjectID, IncrementalThreadedResourceLoader
from question import Question
from screens.question_screen import QuestionScreen


def nav_to_answer_screen(q: Question, a: int):
    # Check the answer and set the correct flag based on the answer
    correct_answer = q.options[a]
    if q.answer == correct_answer:
        screen = CorrectScreen(screen_size, clock, q)
    else:
        screen = FailScreen(screen_size, clock, q, correct_answer)
    screen.next_button_action = lambda: nav_to_question_screen()
    question_screen.on_got_answer = lambda: nav_to_answer_screen(q, a)
    question_screen.set_question(q)

    screen.draw_screen(window_surface)
    pygame.display.update()


if __name__ == '__main__':


# # PyGame display init
pygame.init()
pygame.display.set_caption('Engame Quiz')
window_surface = pygame.display.set_mode((800, 600))

# ## Background
bg = pygame.Surface((800, 600))
bg.fill(pygame.Color("#ebebeb"))

# ## UI Init
loader = IncrementalThreadedResourceLoader()
clock = pygame.time.Clock()
ui = pygame_gui.UIManager((800, 600), 'assets/theme.json', resource_loader=loader)

def render_screen(surface):
    global screen
    if screen == 0:
        # Show the question screen
        question_screen.draw_screen(window_surface)
    elif screen == 1:
        # Show the correct screen
        correct_screen.draw_screen(window_surface)
    elif screen == 2:
        # Show the fail screen
        fail_screen.draw_screen(window_surface)

# # Main game-loop
is_running = True
while is_running:
    # ## Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # ### Shutdown algorythm
            is_running = False
        if event.type == pygame.UI_BUTTON_PRESSED:
            # ### Button pressed: find which one has pressed?
            idx = -10
            element = event.ui_element
            if element == question_screen.answer0_button:
                idx = 0
            elif element == question_screen.answer1_button:
                idx = 1
            elif element == question_screen.answer2_button:
                idx = 2
            elif element == question_screen.answer3_button:
                idx = 3
            question_screen.on_got_answer(idx)

    # ## Update the UI
    ui.update(time_delta)
    window_surface.blit(bg, (0, 0))
    render_screen(window_surface)
    pygame.display.update()
