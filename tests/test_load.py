from question import Question

questions = Question.load("questions.yml")

for i, prompt in zip(range(len(questions)), questions):
    print(f"\nQuestion {i+1}: {prompt.question}")
    for option in prompt.options:
        print(" -", option)
