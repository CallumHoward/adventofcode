import re

sues = []
changed = ['cats', 'trees', 'pomeranians', 'goldfish']
output = 'Constraints 0: children: 3 cats: 7 samoyeds: 2 pomeranians: 3\
    akitas: 0 vizslas: 0 goldfish: 5 trees: 3 cars: 2 perfumes: 1'

with open('16.txt') as f:
    for line in [output] + f.readlines():
        sues.append({})
        sue_number = int(re.search(r'\d+', line).group())
        properties = re.findall(r'[a-z]+(?=:)', line)
        quantities = map(int, re.findall(r'(?<=: )\d+', line))
        for property, quantity in zip(properties, quantities):
            sues[sue_number][property] = quantity


constraints = sues[0]
for sue_number, sue in enumerate(sues):
    #if all(constraints[property] == quantity for property, quantity in sue.items()):
    if all(constraints[property] == quantity for property, quantity in sue.items() if property not in changed):
        all_true = True
        if 'cats' in sue and not sue['cats'] > constraints['cats']:
            all_true = False
        if 'trees' in sue and not sue['trees'] > constraints['trees']:
            all_true = False
        if 'pomeranians' in sue and not sue['pomeranians'] < constraints['pomeranians']:
            all_true = False
        if 'goldfish' in sue and not sue['goldfish'] < constraints['goldfish']:
            all_true = False
        if all_true:
            print sue_number, sue
