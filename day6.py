from collections import defaultdict
import re

DEFAULT_INPUT = 'day6.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    lights = defaultdict(bool)
    with open(loc) as f:
        instructions = f.readlines()
    for inst in instructions:
        m = re.match(r'(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)', inst)
        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if m.group(1) == 'toggle':
                    lights[(x, y)] = not lights[(x, y)]
                else:
                    lights[(x, y)] = m.group(1) == 'turn on'
    return sum(lights.values())

def part_2(loc: str = DEFAULT_INPUT) -> int:
    lights = defaultdict(int)
    with open(loc) as f:
        instructions = f.readlines()
    for inst in instructions:
        m = re.match(r'(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)', inst)
        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if m.group(1) == 'toggle':
                    lights[(x, y)] += 2
                elif m.group(1) == 'turn on':
                    lights[(x, y)] += 1
                else:
                    lights[(x, y)] = max(0, lights[(x, y)] - 1)
    return sum(lights.values())
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
