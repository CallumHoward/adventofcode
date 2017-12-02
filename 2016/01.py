# 01.py
# Callum Howard, 2016

dir = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW
pos = (0, 0)

instructions = [x.strip() for x in raw_input().split(',')]
print instructions

for instruction in instructions:
    n_blocks = int(instruction[1:])
    dir = dir + 1 if instruction[0] == 'R' else dir - 1
    dir %= 4
    pos = pos[0] + n_blocks * dirs[dir][0], pos[1] + n_blocks * dirs[dir][1]
    print pos, sum(pos)
