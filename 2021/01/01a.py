from sys import stdin
nums = list(map(int, stdin.readlines()))
print(sum(1 for n in zip(nums, nums[1:]) if n[0] < n[1]))
