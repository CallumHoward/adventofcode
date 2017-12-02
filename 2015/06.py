import re

class Light(object):

    def __init__(self):
        self.state = False

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def toggle(self):
        if self.state:
            self.off()
        else:
            self.on()


class Light2(object):

    def __init__(self):
        self.state = 0

    def on(self):
        self.state += 1

    def off(self):
        if self.state > 0:
            self.state -= 1

    def toggle(self):
        self.state += 2


class Grid(object):
    def __init__(self, height, width):
        self.grid = [[Light2() for _ in xrange(width)] for row in xrange(height)]

    def on_range(self, coords):
        for row in xrange(coords[1], coords[3]+1):
            for col in xrange(coords[0], coords[2]+1):
                self.grid[row][col].on()

    def off_range(self, coords):
        for row in xrange(coords[1], coords[3]+1):
            for col in xrange(coords[0], coords[2]+1):
                self.grid[row][col].off()

    def toggle_range(self, coords):
        for row in xrange(coords[1], coords[3]+1):
            for col in xrange(coords[0], coords[2]+1):
                self.grid[row][col].toggle()

    def count_on(self):
        count = 0
        for row in self.grid:
            for light in row:
                if light.state:
                    count += light.state
        return count



def parse_coords(line):
    return re.findall('\d+', line)


grid = Grid(1000, 1000)
with open('06.txt') as f:
    for line in f.readlines():
        coords = map(int, parse_coords(line))
        assert(coords[0] <= coords[2])
        assert(coords[1] <= coords[3])

        if re.match('turn on', line):
            grid.on_range(coords)
        elif re.match('turn off', line):
            grid.off_range(coords)
        else:
            grid.toggle_range(coords)

print grid.count_on()




