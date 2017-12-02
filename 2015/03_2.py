
coord = (0, 0)
houses = set()

coord_s = (0, 0)
coord_r = (0, 0)
santa = set()
robos = set()


with open('03.txt') as f:
    for i, direction in enumerate('>'):#f.read()):
        if direction == '<':
            move = (1, 0)
        elif direction == '>':
            move = (-1, 0)
        elif direction == '^':
            move = (0, 1)
        elif direction == 'v':
            move = (0, -1)

        coord = tuple(sum(x) for x in zip(coord, move))
        houses.add(coord)

        # part 2
        if i % 2:
            coord_s = tuple(sum(x) for x in zip(coord_s, move))
            santa.add(coord_s)
        else:
            coord_r = tuple(sum(x) for x in zip(coord_r, move))
            robos.add(coord_r)


print len(houses)
print len(santa.union(robos))

