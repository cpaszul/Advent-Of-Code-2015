from collections import deque
import re

DEFAULT_INPUT = 'day14.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    reindeer = []
    with open(loc) as f:
        for line in f.readlines():
            digits = re.findall(r'(\d+)', line)
            reindeer.append([int(digits[0])] * int(digits[1]) + \
                            [0] * int(digits[2]))
    return max(distance_traveled(r, 2503) for r in reindeer)

def distance_traveled(reindeer: list[int], t: int) -> int:
    d = 0
    i = 0
    for _ in range(t):
        d += reindeer[i]
        i += 1
        i %= len(reindeer)
    return d

def part_2(loc: str = DEFAULT_INPUT) -> int:
    reindeer = []
    with open(loc) as f:
        for line in f.readlines():
            digits = re.findall(r'(\d+)', line)
            reindeer.append(deque([int(digits[0])] * int(digits[1]) + \
                                  [0] * int(digits[2])))
    leads = [0] * len(reindeer)
    current_distances = [0] * len(reindeer)
    for _ in range(2503):
        for i, r in enumerate(reindeer):
            current_distances[i] += r[0]
            r.rotate(-1)
        furthest_distance = max(current_distances)
        for i in range(len(reindeer)):
            if current_distances[i] == furthest_distance:
                leads[i] += 1
    return max(leads)
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
