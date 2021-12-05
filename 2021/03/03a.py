from sys import stdin
from statistics import mode

lines = [line.strip() for line in stdin.readlines()]
gamma = int("".join(mode(col) for col in zip(*lines)), 2)
epsilon = 2**len(lines[0]) - gamma - 1
print(gamma * epsilon)
