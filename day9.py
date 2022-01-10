from itertools import permutations
from collections import defaultdict

DEFAULT_INPUT = 'day9.txt'

def day_9(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    graph = defaultdict(dict)
    nodes = set()
    with open(loc) as f:
        for line in f.readlines():
            a, _, b, _, dist = line.rstrip().split(' ')
            graph[a][b] = int(dist)
            graph[b][a] = int(dist)
            nodes.add(a)
            nodes.add(b)
    shortest, longest = 10**9, -1
    for path in permutations(nodes):
        path_length = sum(graph[a][b] for a, b in zip(path, path[1:]))
        shortest = min(shortest, path_length)
        longest = max(longest, path_length)
    return shortest, longest
    
if __name__ == '__main__':
    part_1, part_2 = day_9()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
