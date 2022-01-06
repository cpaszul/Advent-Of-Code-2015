DEFAULT_INPUT = 'day3.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        moves = f.readline().rstrip()
    visited = set([(0, 0)])
    x = 0
    y = 0
    dirs = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}
    for move in moves:
        dx, dy = dirs[move]
        x += dx
        y += dy
        visited.add((x, y))
    return len(visited)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        moves = f.readline().rstrip()
    visited = set([(0, 0)])
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    dirs = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}
    first = True
    for move in moves:
        dx, dy = dirs[move]
        if first:
            x1 += dx
            y1 += dy
            visited.add((x1, y1))
        else:
            x2 += dx
            y2 += dy
            visited.add((x2, y2))
        first = not first
    return len(visited)
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
