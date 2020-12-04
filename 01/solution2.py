nums = []
for line in open('input.txt', 'r'):
    nums.append(int(line))
for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] <= 2020:
            for k in range(2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i] * nums[j] * nums[k])
                    exit()
