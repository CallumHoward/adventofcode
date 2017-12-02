import re
from string import lowercase as lc

def has_straight(input):
    '''has an increasing straight of three letters'''
    for straight in zip(lc, lc[1:], lc[2:]):
        if ''.join(straight) in input:
            return True
    return False


def contains(input, letters):
    return any(letter for letter in letters if letter in input)


def num_pairs(input):
    pair_pattern = re.compile(r'([a-z])\1')
    counter = 0
    while pair_pattern.search(input):
        input = pair_pattern.sub('.', input, count=1)
        counter += 1

    return counter


def next_pass(input):
    last_letter = input[-1]
    next_letter = lc[(lc.find(last_letter) + 1) % len(lc)]
    if next_letter == 'a':
        return next_pass(input[:-1]) + next_letter
    else:
        return input[:-1] + next_letter


p = 'hepxcrrq'
p = next_pass('hepxxyzz')
while not (has_straight(p) and not contains(p, ['i', 'o', 'l']) and num_pairs(p) >= 2):
    p = next_pass(p)

print p
