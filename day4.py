from hashlib import md5

DEFAULT_INPUT = 'day4.txt'

def day_4(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        key = f.readline().rstrip()
    part_1_res = 0
    i = 0
    while True:
        k = (key + str(i)).encode()
        m = md5(k).hexdigest()
        if m.startswith('00000') and not part_1_res:
            part_1_res = i
        if m.startswith('000000'):
            return part_1_res, i
        i += 1

if __name__ == '__main__':
    part_1, part_2 = day_4()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
