from collections import defaultdict
from itertools import permutations
import re

DEFAULT_INPUT = 'day13.txt'

def day_13(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    graph = defaultdict(dict)
    names = set()
    pattern = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units? by sitting next to (\w+)\.')
    with open(loc) as f:
        for line in f.readlines():
            m = pattern.match(line)
            graph[m.group(1)][m.group(4)] = int(m.group(3)) * (1 if m.group(2) == 'gain' else -1)
            names.add(m.group(1))
            names.add(m.group(4))
    max_happiness_p1 = -1
    for perm in permutations(names):
        happiness = 0
        for a, b in zip(perm, perm[1:]):
            happiness += graph[a][b]
            happiness += graph[b][a]
        happiness += graph[perm[0]][perm[-1]]
        happiness += graph[perm[-1]][perm[0]]
        max_happiness_p1 = max(max_happiness_p1, happiness)
    for name in names:
        graph[name]['s'] = 0
        graph['s'][name] = 0
    names.add('s')
    max_happiness_p2 = -1
    for perm in permutations(names):
        happiness = 0
        for a, b in zip(perm, perm[1:]):
            happiness += graph[a][b]
            happiness += graph[b][a]
        happiness += graph[perm[0]][perm[-1]]
        happiness += graph[perm[-1]][perm[0]]
        max_happiness_p2 = max(max_happiness_p2, happiness)
    return max_happiness_p1, max_happiness_p2
    
if __name__ == '__main__':
    part_1, part_2 = day_13()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
