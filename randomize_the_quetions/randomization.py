import random


def randomize_questions(question_instances):
    """
    Randomize questions.
    :param question_instances: List of Question instances
    :return: Randomized list of Question instances
    """
    return random.choice(question_instances)
