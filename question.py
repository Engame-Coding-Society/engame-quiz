

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
