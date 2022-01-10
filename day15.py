from collections import namedtuple
import re

DEFAULT_INPUT = 'day15.txt'

Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories'])

def part_1(loc: str = DEFAULT_INPUT) -> int:
    ingredients = []
    with open(loc) as f:
        for line in f.readlines():
            digits = re.findall(r'(-?\d+)', line)
            ingredients.append(Ingredient(*map(int, digits)))
    max_score = -1
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - (i + j)):
                for l in range(101 - (i + j + k)):
                    if i + j + k + l == 100:
                        capacity_score = ingredients[0].capacity * i + \
                                         ingredients[1].capacity * j + \
                                         ingredients[2].capacity * k + \
                                         ingredients[3].capacity * l
                        durability_score = ingredients[0].durability * i + \
                                           ingredients[1].durability * j + \
                                           ingredients[2].durability * k + \
                                           ingredients[3].durability * l
                        flavor_score = ingredients[0].flavor * i + \
                                       ingredients[1].flavor * j + \
                                       ingredients[2].flavor * k + \
                                       ingredients[3].flavor * l
                        texture_score = ingredients[0].texture * i + \
                                        ingredients[1].texture * j + \
                                        ingredients[2].texture * k + \
                                        ingredients[3].texture * l
                        capacity_score = max(0, capacity_score)
                        durability_score = max(0, durability_score)
                        flavor_score = max(0, flavor_score)
                        texture_score = max(0, texture_score)
                        score = capacity_score * durability_score * flavor_score * texture_score
                        max_score = max(max_score, score)
    return max_score

def part_2(loc: str = DEFAULT_INPUT) -> int:
    ingredients = []
    with open(loc) as f:
        for line in f.readlines():
            digits = re.findall(r'(-?\d+)', line)
            ingredients.append(Ingredient(*map(int, digits)))
    max_score = -1
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - (i + j)):
                for l in range(101 - (i + j + k)):
                    if i + j + k + l == 100:
                        total_calories = ingredients[0].calories * i + \
                                         ingredients[1].calories * j + \
                                         ingredients[2].calories * k + \
                                         ingredients[3].calories * l
                        if total_calories == 500:
                            capacity_score = ingredients[0].capacity * i + \
                                             ingredients[1].capacity * j + \
                                             ingredients[2].capacity * k + \
                                             ingredients[3].capacity * l
                            durability_score = ingredients[0].durability * i + \
                                               ingredients[1].durability * j + \
                                               ingredients[2].durability * k + \
                                               ingredients[3].durability * l
                            flavor_score = ingredients[0].flavor * i + \
                                           ingredients[1].flavor * j + \
                                           ingredients[2].flavor * k + \
                                           ingredients[3].flavor * l
                            texture_score = ingredients[0].texture * i + \
                                            ingredients[1].texture * j + \
                                            ingredients[2].texture * k + \
                                            ingredients[3].texture * l
                            capacity_score = max(0, capacity_score)
                            durability_score = max(0, durability_score)
                            flavor_score = max(0, flavor_score)
                            texture_score = max(0, texture_score)
                            score = capacity_score * durability_score * flavor_score * texture_score
                            max_score = max(max_score, score)
    return max_score
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
