import sys

def move_node(dirs, node, rope, visits):
  for dir in dirs:
    if dir == 'R': rope[node][0] += 1
    elif dir == 'L': rope[node][0] -= 1
    elif dir == 'U': rope[node][1] += 1
    elif dir == 'D': rope[node][1] -= 1

  if node+1 == len(rope): visits.add(str(rope[node]))
  else: catch_up(node+1, rope, visits)

def catch_up(node, rope, visits):
  diff = [rope[node][0] - rope[node - 1][0], rope[node][1] - rope[node - 1][1]]
  dirs = []
  if 2 in (map(abs, diff)):
    if diff[0] > 0: dirs.append('L')
    elif diff[0] < 0: dirs.append('R')
    if diff[1] > 0: dirs.append('D')
    elif diff[1] < 0: dirs.append('U')

  move_node(dirs, node, rope, visits)

def solve(size, ops):
  rope, visits = [[0, 0] for _ in range(size)], set()
  for dir, i in ops:
    for _ in range(int(i)): move_node([dir], 0, rope, visits)
  return len(visits)

ops = [line.split() for line in open(sys.argv[1]).read().splitlines()]
print('Part 1:', solve(2, ops))
print('Part 2:', solve(10, ops))
