# 02/part1.py
# http://adventofcode.com/2017/day/2
# Callum Howard, 2017

from sys import stdin

#sum = 0
#for line in stdin.readlines():
#    ns = list(map(int, line.split()))
#    sum += max(ns) - min(ns)
#print(sum)

print(sum(max(ns) - min(ns)
        for ns in (list(map(int, line.split()))
                for line in stdin.readlines())))

#print(sum(max(ns) - min(ns) for ns in
#        map(lambda l: list(map(int, l.split())), stdin.readlines())))

#print(sum(max(map(int, line.split())) - min(map(int, line.split()))
#        for line in stdin.readlines()))
