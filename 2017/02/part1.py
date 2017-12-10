# part1.py
# Callum Howard, 2017

from sys import stdin

#sum = 0
#for line in stdin.readlines():
#    ns = list(map(int, line.split()))
#    sum += max(ns) - min(ns)
#print(sum)

#print(list(map(lambda l: list(map(int, l.split())), stdin.readlines())))

print(sum(max(ns) - min(ns)
        for ns in (list(map(int, line.split()))
                for line in stdin.readlines())))

#print(sum(max(ns) - min(ns) for ns in
        #map(lambda l: list(map(int, l.split())), stdin.readlines())))

#print(sum(max(map(int, line.split())) - min(map(int, line.split()))
#        for line in stdin.readlines()))

#print(sum(a - b for (a, b) in zip(map(lambda ns: max(ns), min(ns),
#        map(lambda line: map(int, line.split()), stdin.readlines())))))
