import re

valid_passwords = 0

for line in open('input.txt', 'r'):
    res = re.match(r'^(\d+)-(\d+) (\w): (\w+)$', line)
    min, max, letter, word = [res.group(i) for i in range(1, 5)]

    diff = abs(len(word) - len(word.replace(letter, '')))
    if int(min) <= diff <= int(max):
        valid_passwords += 1

print(valid_passwords)
