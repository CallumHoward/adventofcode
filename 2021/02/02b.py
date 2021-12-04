from sys import stdin

horizontal = 0
depth = 0
aim = 0
for dir, dist in ((dir, int(dist)) for dir, dist in map(lambda x: x.split(), stdin.readlines())):
    if dir == "forward":
        horizontal += dist
        depth += aim * dist
    elif dir == "down":
        aim += dist
    elif dir == "up":
        aim -= dist

print(horizontal * depth)
