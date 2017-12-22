# 03/part2.py
# http://adventofcode.com/2017/day/3
# Callum Howard, 2017

from math import sqrt

# directions
N  = (+0, -1)
NW = (-1, -1)
S  = (+0, +1)
SE = (+1, +1)
E  = (+1, +0)
NE = (+1, -1)
W  = (-1, +0)
SW = (-1, +1)

all_dirs = [N, NW, S, SE, E, NE, W, SW]


def go(point, dir):
    return point[0] + dir[0], point[1] + dir[1]


def adjacent(values, point):
    return [values[go(point, dir)] if go(point, dir) in values else 0 for dir in all_dirs]


def solve(target):
    values = dict()
    sroot = 1
    point = (0, 0)
    values[point] = 1

    if values[point] > target:
        return values[point]

    while True:
        spiral = [(E, 1),
                (N, sroot),
                (W, sroot + 1),
                (S, sroot + 1),
                (E, sroot + 1)]

        for direction, distance in spiral:

            for _ in range(distance):
                point = go(point, direction)
                values[point] = sum(adjacent(values, point))

                if values[point] > target:
                    return values[point]

        sroot += 2


target = int(input())
print(f'target:\t{target}')
print(solve(target))
