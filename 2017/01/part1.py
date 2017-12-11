# 01/part1.py
# http://adventofcode.com/2017/day/1
# Callum Howard, 2017

from itertools import islice, cycle

input = list(map(int, input()))
shift = 1 #len(input) // 2
print(sum(a for a, b in zip(input, input[shift:] + input[:shift]) if a == b))
print(sum(a for a, b in zip(input, islice(cycle(input), shift, None)) if a == b))
print(sum(a for i, a in enumerate(input) if a == input[(i + shift) % len(input)]))
