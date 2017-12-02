from sys import stdin, stdout

dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k_lim = (0, len(keypad) - 1)
pos = (1, 1)

for letter in stdin.read():
    if letter not in dirs: stdout.write(str(keypad[pos[0]][pos[1]])); continue
    pos = tuple(x + y for x, y in zip(pos, dirs[letter]))
    pos = min(pos[0], k_lim[1]), min(pos[1], k_lim[1])
    pos = max(pos[0], k_lim[0]), max(pos[1], k_lim[0])
print str(keypad[pos[0]][pos[1]])
