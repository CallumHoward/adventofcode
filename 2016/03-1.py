from sys import stdin
def foo(edges): return edges[0] + edges[1] > edges[2]
lines = [map(int, y.split()) for y in stdin]
lines = [item for sublist in zip(*lines) for item in sublist]
print sum(1 for num in zip(lines[::3], lines[1::3], lines[2::3]) if foo(sorted(num)))
