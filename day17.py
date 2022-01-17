from itertools import combinations, chain

DEFAULT_INPUT = 'day17.txt'

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        containers = list(map(int, f.readlines()))
    return sum(sum(pset) == 150 for pset in powerset(containers))

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        containers = list(map(int, f.readlines()))
    valid_containers = []
    min_required = 10**9
    for pset in powerset(containers):
        if sum(pset) == 150:
            valid_containers.append(pset)
            min_required = min(min_required, len(pset))
    return len([pset for pset in valid_containers if len(pset) == min_required])
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
