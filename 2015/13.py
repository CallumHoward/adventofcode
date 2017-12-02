import re
from itertools import permutations
from collections import defaultdict

party = defaultdict(dict)

with open('13.txt') as f:
    for line in f.readlines():
        attendees = re.findall(r'[A-Z][a-z]+', line)
        happiness = int(re.search(r'\d+', line).group())
        if re.search(r'lose', line): happiness = -happiness
        party[attendees[0]][attendees[1]] = happiness

def get_happiness(pairs):
    return sum(party[p1][p2] + party[p2][p1] for p1, p2 in pairs)


most = 0
for perm in permutations(party):
    h = get_happiness(pair for pair in zip(perm, perm[1:]) + [(perm[-1], perm[0])])
    most = max(most, h)
print most


most = 0
for perm in permutations(party):
    h = get_happiness(pair for pair in zip(perm, perm[1:]))
    most = max(most, h)
print most
