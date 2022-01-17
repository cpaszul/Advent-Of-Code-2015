DEFAULT_INPUT = 'day18.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    graph = {}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                graph[(x, y)] = cell == '#'
    for _ in range(100):
        graph = update_graph(graph, False)
    return sum(graph.values())

def adjacent(point: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = point
    return [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

def update_graph(graph: dict[tuple[int, int], bool], part_two = bool) -> dict[tuple[int, int], bool]:
    new_graph = {}
    for cell in graph:
        if part_two and cell in ((0, 0), (0, 99), (99, 0), (99, 99)):
            new_graph[cell] = True
        else:
            adjacent_on = len([adj for adj in adjacent(cell) if adj in graph and graph[adj]])
            if graph[cell]:
                new_graph[cell] = adjacent_on in (2, 3)
            else:
                new_graph[cell] = adjacent_on == 3
    return new_graph

def part_2(loc: str = DEFAULT_INPUT) -> int:
    graph = {}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                graph[(x, y)] = cell == '#' or (x, y) in ((0, 0), (0, 99), (99, 0), (99, 99))
    for _ in range(100):
        graph = update_graph(graph, True)
    return sum(graph.values())
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
