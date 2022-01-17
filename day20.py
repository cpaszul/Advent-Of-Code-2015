import math

DEFAULT_INPUT = 'day20.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        puzzle_input = int(f.readline()) // 10
    houses = [1] * (puzzle_input + 1)
    for i in range(1, len(houses)):
        for j in range(i, len(houses), i):
            houses[j] += i
    for i, house in enumerate(houses):
        if house >= puzzle_input:
            return i
        

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        puzzle_input = int(f.readline())
    houses = [0] * (math.ceil(puzzle_input / 11) + 1)
    for i in range(len(houses)):
        j = i
        for _ in range(50):
            if j >= len(houses):
                break
            houses[j] += i * 11
            j += i
    for i, house in enumerate(houses):
        if house >= puzzle_input:
            return i
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
