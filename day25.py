import re

DEFAULT_INPUT = 'day25.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        target_y, target_x = map(int, re.findall(r'\d+', f.readline()))
    nums = {(1, 1): 20151125}
    x = 1
    y = 1
    max_y = 1
    while (target_x, target_y) not in nums:
        current = nums[(x, y)]
        if y == 1:
            x = 1
            y = max_y + 1
            max_y += 1
        else:
            x += 1
            y -= 1
        nums[(x, y)] = current * 252533 % 33554393
    return nums[(target_x, target_y)]
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
