import re

input = re.findall('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', open('input').read())

valid = lambda o: [o[3][int(o[0])-1], o[3][int(o[1])-1]].count(o[2]) == 1
print(len(list(filter(valid, input))))
