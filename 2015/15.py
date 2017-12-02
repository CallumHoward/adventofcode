import re
from collections import namedtuple, defaultdict
#from functools32 import lru_cache

properties = ['capacity', 'durability', 'flavor', 'texture', 'calories']
Ingredient = namedtuple('Ingredient', properties)
ingredients = {}
total_capacity = 100

with open('15.txt') as f:
    for line in f.readlines():
        ingredient = re.search(r'^[A-Z][a-z]+', line).group()
        property_values = map(int, re.findall(r'-?\d+', line))
        ingredients[ingredient] = Ingredient(*property_values)

# ignoring calories for now
properties = ['capacity', 'durability', 'flavor', 'texture']


def calculate(count):
    total = 1
    for property in properties:
        sub_total = 0
        for ingredient in ingredients:
            sub_total += getattr(ingredients[ingredient], property) * count[ingredients.keys().index(ingredient)]
        if sub_total < 0:
            sub_total = 0
        total *= sub_total
    return total


def calc_calories(count):
    total = 0
    for ingredient in ingredients:
        total += ingredients[ingredient].calories * count[ingredients.keys().index(ingredient)]
    return total


def knapsack(capacity, count=defaultdict(int)):
    counts = []
    for ingredient in ingredients:
        if capacity == ingredients[ingredient].capacity:
            count[ingredient] += 1
            return count
        elif capacity > ingredients[ingredient].capacity:
            new_count = count.copy()
            new_count[ingredient] += 1
            counts.append(knapsack(capacity + ingredients[ingredient].capacity, new_count))

    # select the best result
    return max(calculate(c) for c in counts)



best = 0
rad = [0 for _ in ingredients.keys()]
while rad[-1] != 100:
    rad[0] += 1
    for x in xrange(len(rad)):
        if rad[x] >= 100 and x < len(rad)-1:
            rad[x] = 0
            rad[x+1] += 1

    if sum(rad) == 100 and calc_calories(rad) == 500:
        best = max(best, calculate(rad))

print best

