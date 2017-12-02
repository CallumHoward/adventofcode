import json

with open('12.txt') as f:
    input = json.load(f)


def process(input):
    count = 0
    is_dict = False

    if type(input) == dict:
        input = input.values()
        is_dict = True

    for item in input:
        if item == 'red' and is_dict:
            return 0
        elif type(item) == dict or type(item) == list:
            count += process(item)
        elif type(item) == int:
            count += item

    return count


print process(input)
