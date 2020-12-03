# report_repair.py
# Callum Howard, 2020

import sys

def solve2(nums, target):
    for num in nums:
        if target - num in nums:
            return (num * (target - num))

def solve(nums, target):
    return next(n * (target - n) for n in nums if target - n in nums)

print(solve(set([int(n) for n in sys.stdin.readlines()]), 2020))
