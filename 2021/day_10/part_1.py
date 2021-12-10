import re

input = open('input').read().strip().split('\n')

def clean(st):
  replaced = re.sub(r'\(\)|\{\}|<>|\[\]', '', st)
  if st != replaced: replaced = clean(replaced)
  return replaced

char_points = {'}': 1197, ')': 3, ']': 57, '>': 25137}
points = 0
for line in input:
  matched = re.search('(\}|\)|\]|>)', clean(line))
  if matched != None: points += char_points[matched.group(1)]

print(points)
