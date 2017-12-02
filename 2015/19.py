# 19.py
# Callum Howard, 2016

import sys
from collections import defaultdict
from string import lowercase as lc


def process(input):
    results = set()
    for idx, char in enumerate(input):
        for replace in tokens[char]:
            results.add(input[:idx] + replace + input[idx + 1:])
        if idx == len(input) - 1:
            continue
        if input[idx + 1] not in lc:
            continue
        for replace in tokens[input[idx] + input[idx + 1]]:
            results.add(input[:idx] + replace + input[idx + 2:])
    return results

tokens = defaultdict(list)

line = raw_input()

while line != '':
    token, _, replace = line.split()
    tokens[token].append(replace)
    line = raw_input()

input = raw_input()
results = process(input)

print len(results)
