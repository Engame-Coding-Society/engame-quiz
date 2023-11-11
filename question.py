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

    def is_correct(self, answer_idx):
        """
        Check if the given answer index is correct.
        :param answer_idx: The index of the answer chosen by the player.
        """
        return answer_idx == self.correctIdx

    @classmethod
    def load(cls) -> 'Question':
        """
        Create a sample question.
        :return: A :class:`Question` instance
        """
        question = "What programming language are you using now?"
        options = ["Python", "Javascript", "HTML", "C#"]
        correct_idx = 0
        return cls(question, options, correct_idx)

    def play(self):
        print(self.question)
        print("Options:", self.options)

        # Get player's answer
        answer_idx = int(input("Enter the index of your answer: "))

        # Check if the answer is correct
        print(self.is_correct(answer_idx))


loaded_question = Question.load()
loaded_question.play()
