# 18.py
# Advent of Code
# Callum Howard, 2016

import sys

directions = ((-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1))


class GridState(object):

    def __init__(self, size):
        self.size = size
        self.on_lights = set()

    def add_on_light(self, position):
        return self.on_lights.add(position)

    def remove_on_light(self, position):
        return self.on_lights.remove(position)

    def in_bounds(self, (r, c)):
        return 0 <= r < self.size and 0 <= c < self.size

    def adjacent(self, (pos_r, pos_c)):
        return (pos for pos in map(lambda (r, c): (pos_r + r, pos_c + c),
                directions) if self.in_bounds(pos))

    def count_on(self, position):
        return sum(1 for a in self.adjacent(position) if a in self.on_lights)

    def print_state(self):
        for r in xrange(self.size):
            print "".join('#' if (r, c) in self.on_lights else '.' for c in
                          xrange(self.size))

    def next_state(self):
        new = GridState(self.size)

        for r in xrange(self.size):
            for c in xrange(self.size):

                n_on = self.count_on((r, c))

                if ((r, c) in self.on_lights) and (n_on == 2 or n_on == 3):
                    new.add_on_light((r, c))
                elif (r, c) not in self.on_lights and n_on == 3:
                    new.add_on_light((r, c))

        return new


input_state = GridState(100)

for row, line in enumerate(sys.stdin.readlines()):
    for col, char in enumerate(line):
        if char == '#':
            input_state.add_on_light((row, col))

current_state = input_state

for steps in xrange(100):
    # part 2
    s = current_state.size - 1
    for stuck in ((0, 0), (0, s), (s, 0), (s, s)):
        current_state.add_on_light(stuck)

#     current_state.print_state()
#     print
    current_state = current_state.next_state()

# part 2
s = current_state.size - 1
for stuck in ((0, 0), (0, s), (s, 0), (s, s)):
    current_state.add_on_light(stuck)

# current_state.print_state()
# print

print len(current_state.on_lights)
