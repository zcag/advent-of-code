import re

input = re.findall('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', open('input').read())

valid = lambda o: o[3].count(o[2]) in range(int(o[0]), int(o[1])+1)
print(len(list(filter(valid, input))))
