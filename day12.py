import json
from typing import Union

DEFAULT_INPUT = 'day12.txt'

JS = Union[list, dict, int, str]

def day_12(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        j = json.loads(f.readline().rstrip())
    return sum_of_numbers(j, False), sum_of_numbers(j, True)

def sum_of_numbers(j: JS, part_two: bool) -> int:
    if isinstance(j, str):
        return 0
    if isinstance(j, int):
        return j
    if isinstance(j, list):
        return sum(sum_of_numbers(ele, part_two) for ele in j)
    if isinstance(j, dict):
        if part_two and 'red' in j.values():
            return 0
        return sum(sum_of_numbers(value, part_two) for value in j.values())
    
if __name__ == '__main__':
    part_1, part_2 = day_12()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
