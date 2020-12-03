# report_repair.py
# Callum Howard, 2020

import sys
from itertools import combinations

def solve2(nums, target):
    for a in nums:
        for b in nums:
            if target - a - b in nums:
                return (a * b * (target - a - b))

def solve(nums, target):
    return next(a * b * (target - a - b) for a, b in combinations(nums, 2) if target - a - b in nums)

print(solve(set([int(n) for n in sys.stdin.readlines()]), 2020))
