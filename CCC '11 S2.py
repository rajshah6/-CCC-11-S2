n = int(input())
student_answers = []
correct_answers = []

for i in range(n):
    student_answers.append(input())

for i in range(n):
    correct_answers.append(input())

correct = 0
for i in range(n):
    if student_answers[i] == correct_answers[i]:
        correct += 1

print(correct)
