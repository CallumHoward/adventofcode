# 07/part2.py
# http://adventofcode.com/2017/day/7
# Callum Howard, 2017

import sys

weights = dict()
parent = dict()

for line in sys.stdin.readlines():
    name, weight, *children = ''.join(c for c in line if c.isalnum() or c == ' ').split()
    weights[name] = int(weight)
    for child in children:
        parent[child] = name

while name in parent:
    name = parent[name]

print(name)
