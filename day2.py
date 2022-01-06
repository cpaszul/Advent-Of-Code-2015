DEFAULT_INPUT = 'day2.txt'

def day_2(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        presents = [map(int, line.rstrip().split('x')) for line in f.readlines()]
    part_1_res = 0
    part_2_res = 0
    for l, w, h in presents:
        part_1_res += surface_area(l, w, h) + min(l * w, l * h, w * h)
        part_2_res += smallest_perimeter(l, w, h) + l * w * h
    return part_1_res, part_2_res

def surface_area(l: int, w: int, h: int) -> int:
    return 2 * l * w + 2 * l * h + 2 * w * h

def smallest_perimeter(l: int, w: int, h: int) -> int:
    return min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)
    
if __name__ == '__main__':
    part_1, part_2 = day_2()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
