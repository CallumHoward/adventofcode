# part1.py
# Callum Howard, 2017
input = list(map(int, input()))
shift = len(input) // 2
print(sum(a for a, b in zip(input, input[shift:] + input[:shift]) if a == b))
