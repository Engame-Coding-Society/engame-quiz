import yaml


class Question:
    """
    General class for the questions model
    See params in the `__init__` method
    """

    PROMPTS = []

    def __init__(self, question, options):
        """
        Constructor of the question model
        :param question: Question displayed
        :param options: List of possible answers
        """
        self.question = question
        self.options = options

    @staticmethod
    def load(path: str) -> list:
        """
        Loads every question from the 'questions.yml' file
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
