DEFAULT_INPUT = 'day10.txt'

def day_10(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        seq = f.readline().rstrip()
    for i in range(50):
        seq = next_in_seq(seq)
        if i == 39:
            part_1_res = len(seq)
    return part_1_res, len(seq)

def next_in_seq(s: str) -> str:
    next_seq = ''
    prev = s[0]
    count = 0
    for ch in s:
        if ch == prev:
            count += 1
        else:
            next_seq += str(count)
            next_seq += prev
            prev = ch
            count = 1
    next_seq += str(count)
    next_seq += prev
    return next_seq
    
if __name__ == '__main__':
    part_1, part_2 = day_10()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
