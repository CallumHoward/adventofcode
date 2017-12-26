# 05/part2.py
# http://adventofcode.com/2017/day/5
# Callum Howard, 2017

import sys
from itertools import count

ns = [int(n.strip()) for n in sys.stdin.readlines()]

def solve(ns, index=0):
    for step in count(1):
        temp = ns[index]
        if temp >= 3:
            ns[index] -= 1
        else:
            ns[index] += 1
        index += temp
        if not (0 <= index < len(ns)):
            return step


assert(solve([0, 3, 0, 1, -3], 0) == 10)
assert(solve([1, 3, 0, 1, -3], 0) == 9)
assert(solve([2, 3, 0, 1, -3], 1) == 8)
assert(solve([2, 2, 0, 1, -3], 4) == 7)
#assert(solve([2, 2, 0, 1, -4], 1) == 6)
#assert(solve([2, 3, 0, 1, -4], 3) == 5)
#assert(solve([2, 3, 0, 2, -4], 4) == 4)
#assert(solve([2, 3, 0, 2, -3], 0) == 3)
#assert(solve([3, 3, 0, 2, -3], 2) == 2)
#assert(solve([3, 3, 1, 2, -3], 2) == 1)
#assert(solve([3, 3, 2, 2, -3], 3) == 0)

#  0  1  2  3  4
# [0, 3, 0, 1, -3] 0
# [1, 3, 0, 1, -3] 0
# [2, 3, 0, 1, -3] 1
# [2, 2, 0, 1, -3] 4
# [2, 2, 0, 1, -4] 1
# [2, 3, 0, 1, -4] 3
# [2, 3, 0, 2, -4] 4
# [2, 3, 0, 2, -3] 0
# [3, 3, 0, 2, -3] 2
# [3, 3, 1, 2, -3] 2
# [3, 3, 2, 2, -3] 3

print(solve(ns))
