import re

trees_encountered = 0
map = []
slope = (3, 1)

for line in open('input.txt', 'r'):
    map.append(line)

x, y = 3, 1
while y < len(map):
    if map[y][x % (len(map[y])-1)] == '#':
        trees_encountered += 1
    x += 3
    y += 1

print(trees_encountered)