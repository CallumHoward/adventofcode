# 01.py
# Callum Howard, 2016

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW
map = set()


def run(instructions):
    dir = 0
    pos = (0, 0)

    for instruction in instructions:
        dir = dir + 1 if instruction[0] == 'R' else dir - 1
        dir %= 4
        for x in xrange(int(instruction[1:])):
            pos = pos[0] + dirs[dir][0], pos[1] + dirs[dir][1]
            if pos in map:
                print pos, sum(abs(x) for x in pos)
                return
            map.add(pos)

    print pos, sum(abs(x) for x in pos)


run([x.strip() for x in raw_input().split(',')])
