import sys, operator
from operator import add, sub, mul, floordiv, methodcaller

ops = {'+': add, '*': mul, '-': sub, '/': floordiv}
lines = map(methodcaller('split'), open(sys.argv[1]).read().strip().split('\n'))
d = { l[0][:-1]: ((l[1], ops[l[2]], l[3]) if len(l) > 2 else int(l[1])) for l in lines }

def bake(d, root='root'):
  value = d[root]
  if type(value) == int: return value
  if value == None: return None

  left, op, right = value
  solved_left = left if type(left) == int else bake(d, left)
  solved_right = right if type(right) == int else bake(d, right)
  d[root] = (solved_left or left, op, solved_right or right)

  if None in (solved_left, solved_right): return None
  if root == 'root': return solved_left == solved_right
  d[root] = op(solved_left, solved_right)
  return d[root]

def clean(d):
  return { k:v for k, v in d.items() if type(v) != int }

def solve(d, node='root', outcome=0):
  if node == 'humn': return outcome
  left, op, right = d[node]

  sub_node, number = (left, right) if type(right) == int else (right, left)
  if op == add: outcome = outcome - number
  elif op == mul: outcome = outcome / number
  elif op == sub: outcome = (outcome + number) if right == number else (number - outcome)
  elif op == floordiv: outcome = (outcome * number) if right == number else (number / outcome)

  return solve(d, sub_node, outcome)


d['root'], d['humn'] = (d['root'][0], sub, d['root'][2]), None
bake(d)
print('Part 2:', solve(clean(d)))
