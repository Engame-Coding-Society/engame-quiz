import yaml


class Question:
    """
    The Model of Questions.
    See params in the `__init__` method.
    """
    
    PROMPTS = []

    def __init__(self, question, options, correct_idx=0):
        """
        The constructor of the question model
        :param question: The title (the question itself)
        :param options: The list of possible answers
        :param correct_idx: The index of the correct answer. 0 by default.
        """
        self.question = question
        self.options = options
        self.correctIdx = correct_idx

    def is_correct(self, answer_idx):
        """
        Check if the given answer index is correct.
        :param answer_idx: The index of the answer chosen by the player.
        """
        return answer_idx == self.correctIdx

    @staticmethod
    def load(path: str) -> list:
        """
        Loads every question from the 'questions.yml' file.
        :param path: Relative path to the file to read from
        :return: A list of :class:`Question` loaded, or empty list if file is empty or doesn't exist
        """
        Question.PROMPTS.clear()
        with open(path, 'r') as file:
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
                Question.PROMPTS.append(Question(question, answers))
        return Question.PROMPTS
