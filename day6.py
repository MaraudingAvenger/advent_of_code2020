import re
groups = [set(re.sub("\s+", "", line))
          for line in open('day6.txt').read().split("\n\n")]

print('part 1:', sum(len(s) for s in groups))

resps = [line.split() for line in open('day6.txt').read().split('\n\n')]

print('part 2:', sum(len([letter for letter in resp[0] if all(
    letter in x for x in resp)]) for resp in resps))
