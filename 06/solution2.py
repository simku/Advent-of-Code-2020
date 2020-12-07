sum = 0
with open('input.txt') as f:
    lines = f.read()
    groups = [i.split() for i in lines.split('\n\n')]
    for group in groups:
        questions = set([question for question in group[0]])
        for answers in group:
            questions = set([x for x in questions if x in answers])
        sum += len(questions)

print(sum)
