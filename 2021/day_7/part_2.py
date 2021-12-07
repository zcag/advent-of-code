input = [int(i) for i in open('input').read().strip().split(',')]

lowest = 9999999999999
for dist in range(min(input), max(input)+1):
  cost = sum([sum(range(abs(i-dist)+1)) for i in input])
  if cost < lowest: lowest = cost

print(lowest)
