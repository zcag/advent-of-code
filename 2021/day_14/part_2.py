from collections import Counter, defaultdict

input = open('input').read().strip().split('\n')
pairs = Counter([input[0][i:i+2] for i in range(len(input[0])-1)])
rules = dict([l.split(' -> ') for l in input[2:]])

outd = dict(pairs)
res = defaultdict(lambda: 0)
for step in range(40):
  d = {}
  for pair, count in list(outd.items()):
    res[rules.get(pair)] += count
    for new_pair in [pair[0]+rules.get(pair), rules.get(pair)+pair[1]]:
      if new_pair in d: d[new_pair] += count
      else: d[new_pair] = count
  outd = d
for i in input[0]: res[i] += 1

counts = list(res.values())
print(max(counts)-min(counts))
