
coord = (0, 0)
houses = set(coord)

coord_s = (0, 0)
coord_r = (0, 0)
santa = set()
robos = set()



with open('03.txt') as f:
    for i, move in enumerate(f.read()):
        if move == '<':
            coord = (coord[0] + 1, coord[1])
        elif move == '>':
            coord = (coord[0] - 1, coord[1])
        elif move == '^':
            coord = (coord[0], coord[1] + 1)
        elif move == 'v':
            coord = (coord[0], coord[1] - 1)
        else:
            continue;

        houses.add(coord)

        # part 2
        if i % 2:
            if move == '<':
                coord_s = (coord_s[0] + 1, coord_s[1])
            elif move == '>':
                coord_s = (coord_s[0] - 1, coord_s[1])
            elif move == '^':
                coord_s = (coord_s[0], coord_s[1] + 1)
            elif move == 'v':
                coord_s = (coord_s[0], coord_s[1] - 1)
            santa.add(coord_s)
        else:
            if move == '<':
                coord_r = (coord_r[0] + 1, coord_r[1])
            elif move == '>':
                coord_r = (coord_r[0] - 1, coord_r[1])
            elif move == '^':
                coord_r = (coord_r[0], coord_r[1] + 1)
            elif move == 'v':
                coord_r = (coord_r[0], coord_r[1] - 1)
            robos.add(coord_r)


print len(houses)
print len(santa.union(robos))

