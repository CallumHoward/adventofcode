# 03/part2-2.py
# http://adventofcode.com/2017/day/3
# Callum Howard, 2017

from math import sqrt
from itertools import count


class Cardinal():
    # directions
    N  = (+0, -1)
    NW = (-1, -1)
    S  = (+0, +1)
    SE = (+1, +1)
    E  = (+1, +0)
    NE = (+1, -1)
    W  = (-1, +0)
    SW = (-1, +1)
    directions = [N, NW, S, SE, E, NE, W, SW]

    @staticmethod
    def spiral(square_root):
        return [(Cardinal.E, 1),
                (Cardinal.N, square_root),
                (Cardinal.W, square_root + 1),
                (Cardinal.S, square_root + 1),
                (Cardinal.E, square_root + 1)]


def go(point, direction):
    return point[0] + direction[0], point[1] + direction[1]


def adjacent_values(values, point):
    return [values[go(point, direction)]
            if go(point, direction) in values else 0
            for direction in Cardinal.directions]


def solve(target):
    point = (0, 0)
    values = {point: 1}

    for square_root in count(1, 2):
        for direction, distance in Cardinal.spiral(square_root):
            for _ in range(distance):
                point = go(point, direction)
                values[point] = sum(adjacent_values(values, point))

                if values[point] > target:
                    return values[point]


print(solve(int(input())))
