DEFAULT_INPUT = 'day16.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    all_data = {'children': 3,
                'cats': 7,
                'samoyeds': 2,
                'pomeranians': 3,
                'akitas': 0,
                'vizslas': 0,
                'goldfish': 5,
                'trees': 3,
                'cars': 2,
                'perfumes': 1}
    with open(loc) as f:
        for line in f.readlines():
            line = line.rstrip()
            first_colon = line.index(':')
            lhs, rhs = line[:first_colon], line[first_colon + 2:]
            number = int(lhs.split(' ')[1])
            sue_dict = {item.split(': ')[0]: int(item.split(': ')[1]) for item in rhs.split(', ')}
            if all(all_data[key] == value for key, value in sue_dict.items()):
                return number

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        for line in f.readlines():
            line = line.rstrip()
            first_colon = line.index(':')
            lhs, rhs = line[:first_colon], line[first_colon + 2:]
            number = int(lhs.split(' ')[1])
            sue_dict = {item.split(': ')[0]: int(item.split(': ')[1]) for item in rhs.split(', ')}
            if part_2_valid(sue_dict):
                return number

def part_2_valid(sue_dict: dict[str: int]) -> bool:
    all_data = {'children': 3,
                'cats': 7,
                'samoyeds': 2,
                'pomeranians': 3,
                'akitas': 0,
                'vizslas': 0,
                'goldfish': 5,
                'trees': 3,
                'cars': 2,
                'perfumes': 1}
    for key, value in sue_dict.items():
        if key in ('cats', 'trees') and value <= all_data[key]:
            return False
        if key in ('pomeranians', 'goldfish') and value >= all_data[key]:
            return False
        if key not in ('cats', 'trees', 'pomeranians', 'goldfish') and value != all_data[key]:
            return False
    return True
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
