highest = 0
for line in open('input.txt', 'r'):
    highest = max(highest, int(line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2))

print(highest)