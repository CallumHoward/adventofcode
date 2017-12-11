# 02/part2.py
# http://adventofcode.com/2017/day/2
# Callum Howard, 2017

from sys import stdin
from itertools import permutations

print(sum(next(a // b for a, b in permutations(ns, 2) if a % b == 0)
        for ns in (list(map(int, line.split()))
                for line in stdin.readlines())))
