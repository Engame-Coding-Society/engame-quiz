import unittest
from randomize_the_quetions.question import Question
from randomize_the_quetions.randomization import randomize_questions


class TestRandomization(unittest.TestCase):

    def test_randomization(self):
        questions_list = [
            Question("Question 1", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 2", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 3", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 4", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 5", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 6", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 7", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 8", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 9", ["Option 1", "Option 2", "Option 3"]),
            Question("Question 10", ["Option 1", "Option 2", "Option 3"]),
        ]

        for _ in range(10):
            random_question = randomize_questions(questions_list)
            print(f"Random Question: {random_question.question}")


if __name__ == '__main__':
    unittest.main()
