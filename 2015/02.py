


with open('02.txt') as f:
    total = 0
    total2 = 0
    for line in f.readlines():
        dims = map(int, line.split('x'))
        (l, w, h) = dims
        dims.sort()
        total += 2*l*w + 2*w*h + 2*h*l + dims[0]*dims[1]

        # part 2
        smallest_perimeter = 2*dims[0] + 2*dims[1]
        volume = l*w*h
        total2 += smallest_perimeter + volume


    print total
    print total2



