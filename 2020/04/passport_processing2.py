# passport_processing.py
# Callum Howard, 2020

import sys
import re

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def valid(key, value):
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    if key == 'iyr':
        return 2010 <= int(value) <= 2020
    if key == 'eyr':
        return 2020 <= int(value) <= 2030
    if key == 'hgt':
        return (150 <= int(value[:-2]) <= 193 if value[-2:] == 'cm' else
                59 <= int(value[:-2]) <= 76 if value[-2:] == 'in' else False)
    if key == 'hcl':
        return bool(re.match(r'#[0-9a-f]{6}', value))
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'pid':
        return value.isdigit() and len(value) == 9
    return True

def solve(entry):
    return all(key in [pair[0] for pair in entry if valid(*pair)] for key in keys)

print(sum(solve([pair.split(':') for pair in entries.replace('\n', ' ').split(' ')])
        for entries in sys.stdin.read().split('\n\n')))
