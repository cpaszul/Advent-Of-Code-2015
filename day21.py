from collections import namedtuple
from itertools import product

DEFAULT_INPUT = 'day21.txt'

Char = namedtuple('Char', ['hp', 'damage', 'armor'])
Item = namedtuple('Item', ['cost', 'damage', 'armor'])

def day_21(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        enemy_hp = int(f.readline().split(': ')[1])
        enemy_dam = int(f.readline().split(': ')[1])
        enemy_arm = int(f.readline().split(': ')[1])
        enemy = Char(enemy_hp, enemy_dam, enemy_arm)
    weapons = (Item(8, 4, 0), Item(10, 5, 0), Item(25, 6, 0),
               Item(40, 7, 0), Item(74, 8, 0))
    armor = (Item(0, 0, 0), Item(13, 0, 1), Item(31, 0, 2),
             Item(53, 0, 3), Item(75, 0, 4), Item(102, 0, 5))
    rings = (Item(0, 0, 0), Item(25, 1, 0), Item(50, 2, 0), Item(100, 3, 0),
             Item(20, 0, 1), Item(40, 0, 2), Item(80, 0, 3))
    lowest_win = 10 ** 9
    highest_loss = -1
    all_items = product(weapons, armor, rings, rings)
    for items in all_items:
        if items[2] == items[3] and items[2].cost != 0:
            continue
        player = Char(100, sum(item.damage for item in items), sum(item.armor for item in items))
        cost = sum(item.cost for item in items)
        winner = battle(player, enemy)
        if winner == 1:
            lowest_win = min(cost, lowest_win)
        else:
            highest_loss = max(cost, highest_loss)
    return lowest_win, highest_loss

def battle(char_one: Char, char_two: Char) -> int:
    char_one_turn = True
    char_one_hp = char_one.hp
    char_two_hp = char_two.hp
    while True:
        if char_one_turn:
            char_two_hp -= max(1, char_one.damage - char_two.armor)
            if char_two_hp <= 0:
                return 1
        else:
            char_one_hp -= max(1, char_two.damage - char_one.armor)
            if char_one_hp <= 0:
                return 2
        char_one_turn = not char_one_turn
        
if __name__ == '__main__':
    part_1, part_2 = day_21()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
