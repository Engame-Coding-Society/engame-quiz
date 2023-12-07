import unittest
from question import Question
from randomization import randomize_array


class TestRandomization(unittest.TestCase):

    def test_array_randomization(self):
        questions = [
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

        randomized_questions = randomize_array(questions)

        self.assertEqual(len(questions), len(randomized_questions))
        self.assertCountEqual(questions, randomized_questions)
        for random_question in randomized_questions:
            print(random_question.question)


if __name__ == '__main__':
    unittest.main()
