from string import ascii_uppercase
from collections import defaultdict
import re

DEFAULT_INPUT = 'day19.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    rules = defaultdict(list)
    with open(loc) as f:
        for line in f.readlines():
            if m := re.match(r'(\w+) => (\w+)', line):
                rules[m.group(1)].append(m.group(2))
            elif m := re.match(r'\w+', line):
                starting_molecule = line.rstrip()
    starting_molecule = split_molecule(starting_molecule)
    new_molecules = set()
    for i, m in enumerate(starting_molecule):
        for replacement in rules[m]:
            new_molecule = starting_molecule.copy()
            new_molecule[i] = replacement
            new_molecules.add(''.join(new_molecule))
    return len(new_molecules)
        

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        for line in f.readlines():
            if m := re.match(r'\w+', line):
                molecule = line.rstrip()
    molecule = split_molecule(molecule)
    return len(molecule) - (molecule.count('Rn') + molecule.count('Ar')) - (2 * molecule.count('Y')) - 1
                
def split_molecule(m: str) -> list[str]:
    spl = []
    current = ''
    for ch in m:
        if ch in ascii_uppercase and current:
            spl.append(current)
            current = ch
        else:
            current += ch
    spl.append(current)
    return spl
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
