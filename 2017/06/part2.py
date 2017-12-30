# 06/part2.py
# http://adventofcode.com/2017/day/6
# Callum Howard, 2017

from itertools import count


def redistribute(banks):
    banks = list(banks)
    mi, m = max_index(banks)
    banks[mi] = 0
    for x in range(1, m + 1):
        banks[(mi + x) % len(banks)] += 1
    return tuple(banks)


def max_index(list):
    max_i = 0
    max_e = 0
    for i, e in enumerate(list):
        if e > max_e:
            max_i = i
            max_e = e
    return max_i, max_e


def solve1(banks):
    seen = set()
    for steps in count(1):
        seen.add(banks)
        banks = redistribute(banks)
        if banks in seen:
            return banks
    return 0


def solve(banks):
    seen = set()
    for steps in count(1):
        seen.add(banks)
        banks = redistribute(banks)
        if banks in seen:
            return steps
    return 0


assert(redistribute((0, 2, 7, 0)) == (2, 4, 1, 2))
assert(solve((0, 2, 7, 0)) == 5)
assert(solve((2, 4, 1, 2)) == 4)

print(solve(solve1(tuple(map(int, input().split())))))
