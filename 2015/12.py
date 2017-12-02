import re
import json

numbers = []

with open('12.txt') as f:
    for line in f.readlines():
        numbers.extend(re.findall('-?\d+', line))


print sum(map(int, numbers))


lines = []
numbers = []

with open('12.txt') as f:
    for line in f.readlines():
        lines.extend(re.sub('{.*?"red".*?}', '', line))

    for line in lines:
        numbers.extend(re.findall('-?\d+', line))

print sum(map(int, numbers))

with open('12.txt') as f:
    input = json.load(f)

#print input['a']


