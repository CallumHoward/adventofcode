import sys
from itertools import izip_longest
args = [[int(x) for x in line.split()] for line in sys.stdin]
print args
print sum(sum(y[0] + y[1] > y[2]
              for y in [sorted(tri) for tri in zip(*x)])
          for x in zip(*args))
