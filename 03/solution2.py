import re

map = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for line in open('input.txt', 'r'):
    map.append(line)

result = 1

for slope in slopes:
    x, y = slope
    trees_encountered = 0
    while y < len(map):
        if map[y][x % (len(map[y]) - 1)] == '#':
            trees_encountered += 1
        x += slope[0]
        y += slope[1]
    result *= trees_encountered

print(result)