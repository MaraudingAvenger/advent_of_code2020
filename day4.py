import re

dicts = [dict(g.split(':') for g in l.split(','))for l in [re.sub(
    '\s+', ',', s.strip())for s in open('day4.txt').read().split('\n\n')]]

keys = ['byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = [d for d in dicts if all(k in d for k in keys)]

print("Part 1:", len(valid), "valid passports")


def hgt(x) -> bool:
    '''height validator func'''
    if not any(l.isalpha() for l in x):
        return False
    patt = re.compile("([0-9]{2,3})(cm|in)")
    m = patt.match(x)
    if not len(m.groups()) == 2:
        return False
    if m.group(2) == 'in':
        return 59 <= int(m.group(1)) <= 76
    elif m.group(2) == 'cm':
        return 150 <= int(m.group(1)) <= 193
    else:
        return False


new_valid = [
    d for d in valid
    if 1920 <= int(d['byr']) <= 2002 and # birth year validator
    2010 <= int(d['iyr']) <= 2020 and # issue year validator
    2020 <= int(d['eyr']) <= 2030 and # exp year validator
    hgt(d['hgt']) and # height validator
    re.search('#[0-9a-f]{6}', d['hcl']) and # hair clr validator
    d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and # eye clr validator
    all(x.isdigit() for x in d['pid']) and len(d['pid']) == 9 # pid validator
]

print("part 2:", len(new_valid), 'valid passports')
