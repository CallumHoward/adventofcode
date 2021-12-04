from sys import stdin

horizontal = 0
depth = 0
for dir, dist in ((dir, int(dist)) for dir, dist in map(lambda x: x.split(), stdin.readlines())):
    if dir == "forward":
        horizontal += dist
    elif dir == "down":
        depth += dist
    elif dir == "up":
        depth -= dist

print(horizontal * depth)
