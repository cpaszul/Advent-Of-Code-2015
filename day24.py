from functools import cache
from math import prod

DEFAULT_INPUT = 'day24.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        packages = tuple(int(line) for line in f.readlines())
    target = sum(packages) // 3
    groups = split(0, packages, target)
    smallest = len(min(groups, key=len))
    groups = [g for g in groups if len(g) == smallest]
    return prod(min(groups, key=prod))

@cache
def split(i: int, packages: tuple[int], target: int) -> list[tuple[int]]:
    if i == len(packages) or packages[i] > target:
        return [()]
    current = packages[i]
    if current == target:
        return [(current,)]
    else:
        valid = []
        with_current = split(i + 1, packages, target - current)
        for result in with_current:
            if result:
                valid.append((current,) + result)
        without_current = split(i + 1, packages, target)
        for result in without_current:
            if result:
                valid.append(result)
        return valid

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        packages = tuple(int(line) for line in f.readlines())
    target = sum(packages) // 4
    groups = split(0, packages, target)
    smallest = len(min(groups, key=len))
    groups = [g for g in groups if len(g) == smallest]
    return prod(min(groups, key=prod))
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
