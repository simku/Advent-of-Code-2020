seat_ids = []
for line in open('input.txt', 'r'):
    seat_ids.append(int(line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2))

for i in range(2 ** 10):
    if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
        print(i)
        exit()
