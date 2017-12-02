from sys import stdin as s
print sum(n[0] + n[1] > n[2] for n in [sorted(map(int, l.split())) for l in s])
