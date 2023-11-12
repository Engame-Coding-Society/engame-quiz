class Question:
    """
    The Model of Questions.
    See params in the `__init__` method.
    """

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
