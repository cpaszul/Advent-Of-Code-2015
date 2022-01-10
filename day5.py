from collections import defaultdict
from itertools import combinations

DEFAULT_INPUT = 'day5.txt'

def day_5(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        strings = [line.rstrip() for line in f.readlines()]
    return len([s for s in strings if nice_p1(s)]), \
           len([s for s in strings if nice_p2(s)])

def nice_p1(s: str) -> bool:
    if any(bad_string in s for bad_string in ('ab', 'cd', 'pq', 'xy')):
        return False
    return len([ch for ch in s if ch in 'aeiou']) >= 3 and has_double(s)

def has_double(s: str) -> bool:
    for a, b in zip(s, s[1:]):
        if a == b:
            return True
    return False

def nice_p2(s: str) -> bool:
    return has_pairs(s) and has_pair_with_gap(s)

def has_pairs(s: str) -> bool:
    pairs = defaultdict(list)
    for i, ch in enumerate(s[:-1]):
        pairs[(ch + s[i + 1])].append(i)
    pairs = {k:v for k, v in pairs.items() if len(v) > 1}
    for indexes in pairs.values():
        for a, b in combinations(indexes, 2):
            if abs(a - b) > 1:
                return True
    return False

def has_pair_with_gap(s: str) -> bool:
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == c:
            return True
    return False
    
if __name__ == '__main__':
    part_1, part_2 = day_5()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
