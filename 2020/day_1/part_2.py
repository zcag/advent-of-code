import itertools

input = list(map(int, open('input').read().strip().split('\n')))

for c in itertools.combinations(input, 3):
  if sum(c) == 2020: print(c[0]*c[1]*c[2])
