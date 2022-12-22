import sys, operator

ops = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}
lines = map(operator.methodcaller('split'), open(sys.argv[1]).read().strip().split('\n'))
d = { l[0][:-1]: ((l[1], ops[l[2]], l[3]) if len(l) > 2 else int(l[1])) for l in lines }

def solve(d, root='root'):
  value = d[root]
  if type(value) == int: return value
  left, op, right = value
  return op(solve(d, left), solve(d, right))

print('Part 1:', solve(d))
