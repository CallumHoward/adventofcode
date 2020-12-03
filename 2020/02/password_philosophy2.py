# password_philosophy.py
# Callum Howard, 2020

from sys import stdin
import re

def solve(line):
    range, letter, password = line.split()
    pos1, pos2 = (int(x) - 1 for x in range.split('-'))
    return sum((password[pos1] == letter[0], password[pos2] == letter[0])) == 1

def solve2(line):
    pos1, pos2, letter, password = re.match(r'(\d+)-(\d+)\s([a-z]):\s(\w+)', line).groups()
    return sum((password[int(pos1) - 1] == letter, password[int(pos2) - 1] == letter)) == 1

print(sum(solve2(line) for line in stdin.readlines()))
