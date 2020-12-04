nums = set()
for line in open('input.txt', 'r'):
    num = int(line)
    if (2020 - num) in nums:
        print((2020 - num) * num)
        exit(0)
    else:
        nums.add(num)
