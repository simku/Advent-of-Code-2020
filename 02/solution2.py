import re

valid_passwords = 0

for line in open('input.txt', 'r'):
    res = re.match(r'^(\d+)-(\d+) (\w): (\w+)$', line)
    position_1, position_2, letter, word = [res.group(i) for i in range(1, 5)]

    position_1_correct = word[int(position_1) - 1] == letter
    position_2_correct = word[int(position_2) - 1] == letter
    if position_1_correct ^ position_2_correct:
        valid_passwords += 1

print(valid_passwords)
