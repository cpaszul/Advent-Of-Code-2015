DEFAULT_INPUT = 'day1.txt'

def day_1(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        nums = [1 if ch == '(' else -1
                for ch in f.readline().rstrip()]
    current = 0
    for index, value in enumerate(nums):
        current += value
        if current < 0:
            return sum(nums), index + 1
    
if __name__ == '__main__':
    part_1, part_2 = day_1()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
