import re

ds = [dict(g.split(':') for g in l.split(','))for l in [re.sub(
    '\s+', ',', s.strip())for s in open('day4.txt').read().split('\n\n')]]

ks = ['byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = [d for d in ds if all(k in d for k in ks)]

print("Part 1:", len(valid), "valid passports")


def hgt(x):
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
    if 1920 <= int(d['byr']) <= 2002 and
    2010 <= int(d['iyr']) <= 2020 and
    2020 <= int(d['eyr']) <= 2030 and
    hgt(d['hgt']) and
    re.search('#[0-9a-f]{6}', d['hcl']) and
    d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
    all(x.isdigit() for x in d['pid']) and len(d['pid']) == 9
]

print("part 2:", len(new_valid), 'valid passports')
