from sys import stdin, stdout

dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
keypad2 = [
        ['0', '0', '1', '0', '0'],
        ['0', '2', '3', '4', '0'],
        ['5', '6', '7', '8', '9'],
        ['0', 'A', 'B', 'C', '0'],
        ['0', '0', 'D', '0', '0']]
pos = (1, 1)

for line in (x.strip() for x in stdin.readlines()):
    for letter in line:
        new_pos = tuple(x + y for x, y in zip(pos, dirs[letter]))
        new_pos = min(new_pos[0], 4), min(new_pos[1], 4)
        new_pos = max(new_pos[0], 0), max(new_pos[1], 0)
        if keypad2[new_pos[0]][new_pos[1]] != '0':
            pos = new_pos
    stdout.write(str(keypad2[pos[0]][pos[1]]))
print
