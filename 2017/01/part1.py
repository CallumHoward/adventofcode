# part1.py
# Callum Howard, 2017

from itertools import islice, cycle

input = list(map(int, input()))
shift = len(input) // 2 # 1
print(sum(a for a, b in zip(input, input[shift:] + input[:shift]) if a == b))
print(sum(a for a, b in zip(input, islice(cycle(input), shift, None)) if a == b))
print(sum(a for i, a in enumerate(input) if a == input[(i + shift) % len(input)]))
