# 04/part2.py
# http://adventofcode.com/2017/day/4
# Callum Howard, 2017

import sys


def no_duplicates(line):
    words = set()
    for word in line.split():
        word = ''.join(sorted(word))
        if word in words:
            return False
        words.add(word)
    return True


print(sum(1 for line in sys.stdin.readlines() if no_duplicates(line)))
