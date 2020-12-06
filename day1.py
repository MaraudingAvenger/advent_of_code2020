nums = {int(line.strip()) for line in open('day1.txt').readlines()}

for num in nums:
    if (check := (2020 - num)) in nums:
        print(num, 2020-num)
        print("Part one answer:", num * check)
        break

found = False
for num in nums:
    checks = {x for x in nums if x != num}
    for second in checks:
        if (third := 2020 - (num + second)) in checks:
            found = True
            print(num, second, third)
            print("Part two answer:", num * second * third)
            break
    if found:
        break
