from string import ascii_lowercase

DEFAULT_INPUT = 'day11.txt'

def day_11(loc: str = DEFAULT_INPUT) -> tuple[str, str]:
    with open(loc) as f:
        password = f.readline().rstrip()
    part_1_res = None
    while True:
        password = increment(password)
        if valid_password(password) and part_1_res:
            return part_1_res, password
        if valid_password(password):
            part_1_res = password

def increment(s: str) -> str:
    i = 0
    rev_s = list(s[::-1])
    while True:
        if rev_s[i] == 'z':
            rev_s[i] = 'a'
            i += 1
        else:
            index = ascii_lowercase.index(rev_s[i])
            rev_s[i] = ascii_lowercase[index + 1]
            break
    return ''.join(rev_s[::-1])

def valid_password(password: str) -> bool:
    return has_triple(password) and has_two_pairs(password) and not any(ch in password for ch in 'iol')

def has_triple(password: str) -> bool:
    for a, b, c in zip(password, password[1:], password[2:]):
        if ascii_lowercase.index(a) + 2 == ascii_lowercase.index(b) + 1 == ascii_lowercase.index(c):
            return True
    return False

def has_two_pairs(password: str) -> bool:
    return len([ch for ch in ascii_lowercase if ch + ch in password]) >= 2
    
if __name__ == '__main__':
    part_1, part_2 = day_11()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
