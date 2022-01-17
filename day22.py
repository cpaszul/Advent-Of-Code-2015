import heapq

DEFAULT_INPUT = 'day22.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        enemy_hp = int(f.readline().split(': ')[1])
        enemy_dam = int(f.readline().split(': ')[1])
    start = (50, enemy_hp, enemy_dam, 500, 0, 0, 0, True)
    h = [(0, start)]
    while h:
        mana_spent, current = heapq.heappop(h)
        php, ehp, edam, mana, stime, ptime, rtime, pturn = current
        if stime:
            stime -= 1
        if ptime:
            ptime -= 1
            ehp -= 3
        if rtime:
            rtime -= 1
            mana += 101
        if ehp <= 0:
            return mana_spent
        if pturn:
            if mana >= 53:
                heapq.heappush(h, (mana_spent + 53,
                                   (php, ehp - 4, edam, mana - 53, stime, ptime, rtime, False)))
            if mana >= 73:
                heapq.heappush(h, (mana_spent + 73,
                                   (php + 2, ehp - 2, edam, mana - 73, stime, ptime, rtime, False)))
            if stime == 0 and mana >= 113:
                heapq.heappush(h, (mana_spent + 113,
                                   (php, ehp, edam, mana - 113, 6, ptime, rtime, False)))
            if ptime == 0 and mana >= 173:
                heapq.heappush(h, (mana_spent + 173,
                                   (php, ehp, edam, mana - 173, stime, 6, rtime, False)))
            if rtime == 0 and mana >= 229:
                heapq.heappush(h, (mana_spent + 229,
                                   (php, ehp, edam, mana - 229, stime, ptime, 5, False)))
        else:
            if stime:
                php -= enemy_dam - 7
            else:
                php -= enemy_dam
            if php > 0:
                heapq.heappush(h, (mana_spent,
                                   (php, ehp, edam, mana, stime, ptime, rtime, True)))

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        enemy_hp = int(f.readline().split(': ')[1])
        enemy_dam = int(f.readline().split(': ')[1])
    start = (50, enemy_hp, enemy_dam, 500, 0, 0, 0, True)
    h = [(0, start)]
    while h:
        mana_spent, current = heapq.heappop(h)
        php, ehp, edam, mana, stime, ptime, rtime, pturn = current
        if pturn:
            php -= 1
        if php <= 0:
            continue
        if stime:
            stime -= 1
        if ptime:
            ptime -= 1
            ehp -= 3
        if rtime:
            rtime -= 1
            mana += 101
        if ehp <= 0:
            return mana_spent
        if pturn:
            if mana >= 53:
                heapq.heappush(h, (mana_spent + 53,
                                   (php, ehp - 4, edam, mana - 53, stime, ptime, rtime, False)))
            if mana >= 73:
                heapq.heappush(h, (mana_spent + 73,
                                   (php + 2, ehp - 2, edam, mana - 73, stime, ptime, rtime, False)))
            if stime == 0 and mana >= 113:
                heapq.heappush(h, (mana_spent + 113,
                                   (php, ehp, edam, mana - 113, 6, ptime, rtime, False)))
            if ptime == 0 and mana >= 173:
                heapq.heappush(h, (mana_spent + 173,
                                   (php, ehp, edam, mana - 173, stime, 6, rtime, False)))
            if rtime == 0 and mana >= 229:
                heapq.heappush(h, (mana_spent + 229,
                                   (php, ehp, edam, mana - 229, stime, ptime, 5, False)))
        else:
            if stime:
                php -= enemy_dam - 7
            else:
                php -= enemy_dam
            if php > 0:
                heapq.heappush(h, (mana_spent,
                                   (php, ehp, edam, mana, stime, ptime, rtime, True)))
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
