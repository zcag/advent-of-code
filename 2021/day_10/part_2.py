import re

input = open('input').read().strip().split('\n')

def clean(st):
  replaced = re.sub(r'\(\)|\{\}|<>|\[\]', '', st)
  if st != replaced: replaced = clean(replaced)
  return replaced

char_points = {'}': 3, ')': 1, ']': 2, '>': 4}

point_list = []
for line in input:
  cleaned = clean(line)[::-1]
  if re.search('(\}|\)|\]|>)', cleaned) != None: continue

  points = 0
  for c in cleaned.translate(cleaned.maketrans('({[<', ')}]>')):
    points = (points*5)+char_points[c]
  point_list.append(points)

print(sorted(point_list)[int((len(point_list)/2))])
