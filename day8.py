DEFAULT_INPUT = 'day8.txt'

def day_8(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    return sum(len(line) - chars_in_memory(line) for line in lines), \
           sum(encoded_chars(line) - len(line) for line in lines)

def chars_in_memory(line: str) -> int:
    line = line[1:-1]
    total = 0
    i = 0
    while i < len(line):
        total += 1
        ch = line[i]
        if ch == '\\' and line[i + 1] == 'x':
            i += 4
        elif ch == '\\':
            i += 2
        else:
            i += 1
    return total

def encoded_chars(line: str) -> int:
    return len(line) + 2 + line.count('\\') + line.count('"')
    
if __name__ == '__main__':
    part_1, part_2 = day_8()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
