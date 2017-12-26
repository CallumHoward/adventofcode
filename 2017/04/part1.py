# 04/part1.py
# http://adventofcode.com/2017/day/4
# Callum Howard, 2017

import sys


def no_duplicates(line):
    words = set()
    for word in line.split():
        if word in words:
            return False
        words.add(word)
    return True


assert(no_duplicates('aa bb cc dd ee'))
assert(not no_duplicates('aa bb cc dd aa'))
assert(no_duplicates('aa bb cc dd aaa'))

print(sum(1 for line in sys.stdin.readlines() if no_duplicates(line.strip())))
