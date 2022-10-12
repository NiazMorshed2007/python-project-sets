lists = []
scores = []
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    lists.append([name, score])
    scores.append(score)

min_score = min(scores)
scores = filter(lambda val: val != min_score, scores)
second_min_score = min(scores)
answers = []
for person in lists:
    if person[1] == second_min_score:
        answers.append(person[0])

print(sorted(answers))
