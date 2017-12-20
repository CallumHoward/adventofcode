# 03/part1.py
# http://adventofcode.com/2017/day/3
# Callum Howard, 2017

from math import sqrt

# directions
N = (+0, -1)
S = (+0, +1)
E = (+1, +0)
W = (-1, +0)


def go(point, dir):
    return point[0] + dir[0], point[1] + dir[1]


def is_even(n):
    return n % 2 == 0


def find_diagonal(square):
    return square // 2, square // 2


def manhattan(point):
    return abs(point[0]) + abs(point[1])


def prev_odd_square(input):
    n = int(sqrt(input))
    return n - 1 if is_even(n) else n


def solve(target):
    sroot = prev_odd_square(target)
    point = find_diagonal(sroot)
    square = sroot * sroot
    index = square

    print('\n======')
    print(f'testing {target}')
    print(f'square:\t{square}')
    print(f'index:\t{index}\tpoint:\t{point}')

    spiral = [(E, 1),
            (N, sroot),
            (W, sroot + 1),
            (S, sroot + 1),
            (E, sroot + 1)]

    if index == target:
        return manhattan(point)

    for direction, distance in spiral:
        for _ in range(distance):
            point = go(point, direction)
            index += 1

            print(f'index:\t{index},\tpoint:\t{point}')

            if index == target:
                return manhattan(point)
            assert(index < target)


def test_prev_odd_square():
    assert(prev_odd_square(1) == 1)
    assert(prev_odd_square(2) == 1)
    assert(prev_odd_square(8) == 1)
    assert(prev_odd_square(9) == 3)
    assert(prev_odd_square(10) == 3)
    assert(prev_odd_square(32) == 5)
    assert(prev_odd_square(37) == 5)


def test_find_diagonal():
    p1 = find_diagonal(prev_odd_square(11))
    assert(p1 == (1, 1))

    p2 = find_diagonal(prev_odd_square(32))
    assert(p2 == (2, 2))

    p3 = find_diagonal(prev_odd_square(37))
    assert(p3 == (2, 2))

    p4 = find_diagonal(1)
    assert(p4 == (0, 0))


def test_manhattan():
    assert(manhattan((-2, 2)) == 4)
    assert(manhattan((2, 2)) == 4)
    assert(manhattan((2, -2)) == 4)
    assert(manhattan((-2, -2)) == 4)
    assert(manhattan((-2, 0)) == 2)


def test_solve():
    assert(solve(1) == 0)
    assert(solve(2) == 1)
    assert(solve(3) == 2)
    assert(solve(4) == 1)
    assert(solve(5) == 2)
    assert(solve(9) == 2)
    assert(solve(10) == 3)
    assert(solve(11) == 2)
    assert(solve(12) == 3)
    assert(solve(13) == 4)
    assert(solve(14) == 3)
    assert(solve(15) == 2)
    assert(solve(16) == 3)
    assert(solve(17) == 4)
    assert(solve(11) == 2)
    assert(solve(49) == 6)
    assert(solve(26) == 5)
    assert(solve(1024) == 31)
    assert(solve(1025) == 32)


# testing
test_prev_odd_square()
test_find_diagonal()
test_manhattan()
test_solve()


target = int(input())

print(f'target:\t{target}')

print(solve(target))
