from functools import cmp_to_key

def compare(l, r):
  if type(l) != type(r): return compare([l] if type(l) == int else l, [r] if type(r) == int else r)
  if type(l) == int: return 1 if l < r else -1 if l > r else 0
  for i in range(max([len(l), len(r)])):
    if i >= len(l): return 1
    if i >= len(r): return -1
    res = compare(l[i], r[i])
    if res != 0: return res
  return 0

pairs = [list(map(eval, pair.split('\n'))) for pair in open('input').read().strip().split('\n\n')]
print('Part 1:', sum([i+1 for i, pair in enumerate(pairs) if compare(*pair) == 1]))

pairs = sorted(sum(pairs, []) + [[[2]], [[6]]], key=cmp_to_key(compare), reverse=True)
print('Part 2:', (pairs.index([[2]])+1)*(pairs.index([[6]])+1))
