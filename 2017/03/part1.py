# 03/part1.py
# http://adventofcode.com/2017/day/3
# Callum Howard, 2017

# directions
N = (+0, -1)
S = (+0, +1)
E = (+1, +0)
W = (-1, +0)


def go(point, dir):
    return point[0] + dir[0], point[1] + dir[1]


def is_even(n):
    return n % 2 == 0


def next_square(input):
    n = int(sqrt(input))
    return n + 1 if is_even(n) else n + 1


def gen_spiral(n):
    ln = next_square(n)
    
