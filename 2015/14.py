import re
from collections import namedtuple, defaultdict

Raindeer = namedtuple('Raindeer', ['speed', 'time', 'rest'])

raindeer = {}
points = defaultdict(int)

with open('14.txt') as f:
    for line in f.readlines():
        r = re.search(r'[A-Z][a-z]+', line).group()
        raindeer[r] = Raindeer(*map(int, re.findall(r'\d+', line)))


def distance(raindeer, seconds):
    total = 0
    stamina = raindeer.time
    while seconds > 0:
        total += raindeer.speed
        stamina -= 1
        seconds -= 1
        if stamina <= 0:
            seconds -= raindeer.rest
            stamina = raindeer.time
    return total


def lead(s = 2503):
    return max(distance(raindeer[r], s) for r in raindeer)

for s in xrange(1, 2503+1):
    for r in raindeer.values():
        if distance(r, s) == lead(s):
            points[r] += 1

print points
print max(points.values())


