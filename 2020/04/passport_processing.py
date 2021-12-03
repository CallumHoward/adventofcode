# passport_processing.py
# Callum Howard, 2020

import sys

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def solve(entry):
    return all(key in entry for key in keys)

print(sum(solve([pair.split(':')[0] for pair in entries.replace('\n', ' ').split(' ')])
        for entries in sys.stdin.read().split('\n\n')))
