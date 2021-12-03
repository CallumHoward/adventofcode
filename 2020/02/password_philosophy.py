# password_philosophy.py
# Callum Howard, 2020

from sys import stdin
import re

def solve(line):
    range, letter, password = line.split()
    min, max = map(int, range.split('-'))
    return min <= sum(l == letter[0] for l in password) <= max

def solve2(line):
    min, max, letter, password = re.match(r'(\d+)-(\d+)\s([\w+]):\s(\w+)', line).groups()
    return int(min) <= sum(l == letter for l in password) <= int(max)

print(sum(solve2(line) for line in stdin.readlines()))
