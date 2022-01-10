from functools import cache

DEFAULT_INPUT = 'day7.txt'
RULES = {}

def day_7(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    global RULES
    RULES = {}
    with open(loc) as f:
        for line in f.readlines():
            lhs, rhs = line.rstrip().split(' -> ')
            RULES[rhs] = lhs.split(' ')
    part_1_res = get_value('a')
    RULES['b'] = [str(part_1_res)]
    get_value.cache_clear()
    return part_1_res, get_value('a')

@cache
def get_value(wire: str) -> int:
    if wire.isdigit():
        return int(wire)
    val = RULES[wire]
    if len(val) == 1:
        return get_value(val[0])
    elif len(val) == 2:
        return get_value(val[1]) ^ 65535
    else:
        if val[1] == 'AND':
            return get_value(val[0]) & get_value(val[2])
        elif val[1] == 'OR':
            return get_value(val[0]) | get_value(val[2])
        elif val[1] == 'RSHIFT':
            return get_value(val[0]) >> get_value(val[2])
        else:
            return get_value(val[0]) << get_value(val[2])
    
if __name__ == '__main__':
    part_1, part_2 = day_7()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
