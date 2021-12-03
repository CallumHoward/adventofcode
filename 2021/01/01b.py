from sys import stdin
nums = list(map(int, stdin.readlines()))
sums = list(sum(triplet) for triplet in zip(nums, nums[1:], nums[2:]))
print(sum(1 for n in zip(sums, sums[1:]) if n[0] < n[1]))
