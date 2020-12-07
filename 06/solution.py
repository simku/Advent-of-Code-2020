sum = 0
with open('input.txt') as f:
    lines = f.read()
    groups = [i.split() for i in lines.split('\n\n')]
    for group in groups:
        questions = set()
        for answers in group:
            for question in answers:
                questions.add(question)
        sum += len(questions)

print(sum)
