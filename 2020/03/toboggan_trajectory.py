# toboggan_trajectory.py
# Callum Howard, 2020

import sys
from functools import reduce
from operator import mul

trees = set()

input = sys.stdin.readlines()
for row, line in enumerate(input):
    for col, char in enumerate(line):
        if char == '#':
            trees.add((row, col))

def solve(right=3, down=1):
    count = 0
    n_cols = len(input[0].strip())
    for r in range(len(input)):
        for c in range(n_cols):
            if (r, c % n_cols) in trees:
                if c * down == r * right % n_cols and r != 0:
                    count += 1
                    print('X', end=' ')
                else:
                    print('#', end=' ')
            elif c * down == r * right % n_cols and r != 0:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()
    return count

def solve2(right=3, down=1):
    return sum((r, c * right % len(input[0].strip())) in trees and r != 0
            for c, r in enumerate(range(0, len(input), down)))

# print(solve2())

rs = [1, 3, 5, 7, 1]
ds = [1, 1, 1, 1, 2]
print(reduce(mul, map(solve2, rs, ds)))
