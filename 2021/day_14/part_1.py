from collections import Counter

input = open('input').read().strip().split('\n')
st = input[0]
rules = dict([l.split(' -> ') for l in input[2:]])

for step in range(10):
  newst = st[0]
  for i in range(len(st)-1):
    sub = st[i:i+2]
    newst += rules.get(sub, '') + sub[1]
  st = newst

counts = Counter(st).values()
print(max(counts)-min(counts))
