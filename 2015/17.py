
with open('17.txt') as f:
    containers = map(int, f.readlines())

total = 150
#containers = (20, 15, 10, 5, 5)
used = [0 for c in containers]


def capacity(used):
    return sum(u * c for u, c in zip(used, containers))


def next_increment(digits):
    if digits[0] == 0:
        digits[0] = 1
        return digits
    else:
        return [0] + next_increment(digits[1:])


num_containers = len(containers)
combo_count = 0
while used != [1 for c in containers]:
    used = next_increment(used)
    if capacity(used) == total:
        combo_count += 1
        num_containers = min(num_containers, sum(used))

print combo_count
print num_containers

ways_count = 0
used = [0 for c in containers]
while used != [1 for c in containers]:
    used = next_increment(used)
    if capacity(used) == total and sum(used) == num_containers:
        ways_count += 1

print ways_count


#def unused(used, containers):
#    return(container for container)
#
#
#
#def eggnog(used=tuple(0 for c in containers)):
#    for container in unused(used, containers):
#        if sum(used) + container == quantity:
#            return 1
#        if sum(used) + container < quantity:
#            return eggnog(used + tuple(container))



