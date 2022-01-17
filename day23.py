DEFAULT_INPUT = 'day23.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    i = 0
    registers = {'a': 0, 'b': 0}
    while 0 <= i < len(instructions):
        spl = instructions[i].split(' ')
        op = spl[0]
        if op == 'hlf':
            registers[spl[1]] //= 2
        elif op == 'tpl':
            registers[spl[1]] *= 3
        elif op == 'inc':
            registers[spl[1]] += 1
        elif op == 'jmp':
            i += int(spl[1]) - 1
        elif op == 'jie':
            r = spl[1][0]
            if registers[r] % 2 == 0:
                i += int(spl[2]) - 1
        else:
            r = spl[1][0]
            if registers[r] == 1:
                i += int(spl[2]) - 1
        i += 1
    return registers['b']

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    i = 0
    registers = {'a': 1, 'b': 0}
    while 0 <= i < len(instructions):
        spl = instructions[i].split(' ')
        op = spl[0]
        if op == 'hlf':
            registers[spl[1]] //= 2
        elif op == 'tpl':
            registers[spl[1]] *= 3
        elif op == 'inc':
            registers[spl[1]] += 1
        elif op == 'jmp':
            i += int(spl[1]) - 1
        elif op == 'jie':
            r = spl[1][0]
            if registers[r] % 2 == 0:
                i += int(spl[2]) - 1
        else:
            r = spl[1][0]
            if registers[r] == 1:
                i += int(spl[2]) - 1
        i += 1
    return registers['b']
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
