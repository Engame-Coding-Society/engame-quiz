from question import Question

q = Question("What programming language are you using now?", 
             ["Python", "Javascript", "HTML", "C#"])  # used the simplified constructor

print(q.question)
print("Options:", q.options)
# Get player's answer
answer_idx = int(input("Enter the index of your answer: "))
# Check if the answer is correct
print(q.is_correct(answer_idx))
