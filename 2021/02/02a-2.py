from sys import stdin
from functools import reduce
from math import prod

# (horizontal, depth)
def get_pos_delta(dir, dist):
    if dir == "forward":
        return int(dist), 0
    elif dir == "down":
        return 0, int(dist)
    elif dir == "up":
        return 0, -int(dist)
    else:
        print("Invalid input")
        return (0, 0)

def elwise_sum(lhs, rhs):
    return [sum(x) for x in zip(lhs, rhs)]

print(prod(reduce(elwise_sum, [get_pos_delta(*line.split()) for line in stdin.readlines()])))
