import re

lines = [line.strip().split(":") for line in open('day2.txt').readlines()]


class Rule():
    def __init__(self, s: str) -> None:
        patt = re.compile(r"([0-9]+)\-([0-9]+) ([a-z])")
        groups = patt.findall(s)
        if not groups:
            raise IndexError(f"problem matching string {s}")
        self.low = int(groups[0][0])
        self.hi = int(groups[0][1])
        self.letter = groups[0][2]

    def validate_count(self, s: str) -> bool:
        times = s.count(self.letter)
        return self.low <= times <= self.hi

    def validate_position(self, s: str) -> bool:
        def _xor(a, b):
            return (a and not b) or (b and not a)

        return _xor(self.letter == s[self.low-1], self.letter == s[self.hi-1])


valid = []
invalid = []

for line in lines:
    rule = Rule(line[0].strip())
    pw = line[1].strip()

    if rule.validate_count(pw):
        valid.append(line)
    else:
        invalid.append(line)

print("Part 1", end='\n\t')
print(len(valid), "valid passwords", end='\n\t')
print(len(invalid), "invalid passwords")

p2_valid = []
p2_invalid = []
for line in lines:
    rule = Rule(line[0].strip())
    pw = line[1].strip()

    if rule.validate_position(pw):
        p2_valid.append(line)
    else:
        p2_invalid.append(line)

print("Part 2", end='\n\t')
print(len(p2_valid), "valid passwords", end='\n\t')
print(len(p2_invalid), 'invalid passwords')
