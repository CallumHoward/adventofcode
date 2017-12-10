# part1.py
# Callum Howard, 2017

from sys import stdin
from itertools import permutations

#sum = 0
#for line in stdin.readlines():
#    ns = list(map(int, line.split()))
#    sum += max(ns) - min(ns)
#print(sum)

print(sum(next(a // b for a, b in permutations(ns, 2) if a % b == 0)
        for ns in (list(map(int, line.split()))
                for line in stdin.readlines())))
