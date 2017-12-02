import re

nice = set()
nice2 = set()
excluded = ['ab', 'cd', 'pq', 'xy']


def num_vowels(input):
    return sum(input.count(vowel) for vowel in 'aeiou')


def has_doubles(input):
    '''returns true if there is at least one letter that appears twice consequtively'''
    for char in input:
        if input.count(char+char):
            return True
    return False


def has_substrings(input, excluded):
    '''contains any of the substrings provided in the input list'''
    for substring in excluded:
        if substring in input:
            return True
    return False


def pairs(input):
    '''return a set of strings of all consequtive pairs in the input string'''
    return set(line[i]+line[i+1] for i in xrange(len(line) - 2))


def num_pairs(input):
    '''returns number of two letter pairs (that don't overlap)'''
    return sum(1 for _ in (input.count(pair) for pair in pairs(input) if input.count(pair) >= 2))


with open('05.txt') as f:
    for line in f.readlines():
        if num_vowels(line) >= 3 and has_doubles(line) and not has_substrings(line, excluded):
            nice.add(line)

        if num_pairs(line) and any(re.search(char+'.'+char, line) for char in line):
            nice2.add(line)


print len(nice)
print len(nice2)
