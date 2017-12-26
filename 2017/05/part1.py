# 05/part1.py
# http://adventofcode.com/2017/day/5
# Callum Howard, 2017

import sys
from itertools import count

ns = [int(n.strip()) for n in sys.stdin.readlines()]

def solve(ns, index=0):
    for step in count(1):
        temp = ns[index]
        ns[index] += 1
        index += temp
        if not (0 <= index < len(ns)):
            return step

assert(solve([0, 3, 0, 1, -3]) == 5)
print(solve(ns))
