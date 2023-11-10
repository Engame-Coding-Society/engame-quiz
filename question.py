import yaml

PROMPTS = []


class Question:
    """
    The Model of Questions.
    See params in the `__init__` method.
    """

    def __init__(self, question, options):
        """
        The constructor of the question model
        :param question: The title (the question itself)
        :param options: The list of possible answers
        """
        self.question = question
        self.options = options


def load_questions():
    """
    Loads every question from the 'questions.yml' file.
    """
    PROMPTS.clear()
    with open("questions.yml", 'r') as file:
        prompts = yaml.safe_load(file)
        for prompt in prompts["questions"]:
            question = prompt["question"]
            answers = prompt["answers"]
            if not isinstance(question, str):
                print(f"Got incorrect type for question: {type(question)}")
                continue
            if not isinstance(answers, list):
                print(f"Got incorrect type for answer: {type(answers)}")
                continue
            PROMPTS.append(Question(question, answers))
