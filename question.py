

class Question:
    """
    The Model of Questions.
    See params in the `__init__` method.
    """

    def __init__(self, question, options, correct_idx):
        """
        The constructor of the question model
        :param question: The title (the question itself)
        :param options: The list of possible answers
        :param correct_idx: The index of the correct answer
        """
        self.question = question
        self.options = options
        self.correctIdx = correct_idx
