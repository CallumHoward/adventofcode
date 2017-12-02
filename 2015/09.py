import re
from Queue import PriorityQueue
from collections import defaultdict
from itertools import permutations


graph = defaultdict(dict)
pq = PriorityQueue()

# parse data
with open('09.txt') as f:
    for line in f.readlines():
        edge = tuple(re.findall(r'[A-Z][A-Za-z]+', line))
        cost = int(re.search(r'\d+', line).group())
        graph[edge[0]][edge[1]] = cost
        graph[edge[1]][edge[0]] = cost



for perm in permutations(graph):
    cost = 0
    for edge in zip(perm, perm[1::]):
        cost += graph[edge[0]][edge[1]]
    pq.put(cost, tuple(perm))

print pq.get()

while not pq.empty():
    biggest = pq.get()

print biggest
