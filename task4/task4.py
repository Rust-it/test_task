from sys import argv

filename = argv[1]

with open(filename) as f:
    nums = [int(line.strip()) for line in f]
    nums.sort()
    median = nums[len(nums) // 2]
    print(sum(abs(num - median) for num in nums))