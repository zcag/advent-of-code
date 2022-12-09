def move_node(dirs, node, rope, visits):
  for dir in dirs:
    if dir == 'R': rope[node][0] += 1
    elif dir == 'L': rope[node][0] -= 1
    elif dir == 'U': rope[node][1] += 1
    elif dir == 'D': rope[node][1] -= 1

  if node+1 == len(rope): visits.append([rope[node][0], rope[node][1]])
  else: catch_up(node+1, rope, visits)

def catch_up(node, rope, visits):
  rel = [rope[node][0] - rope[node - 1][0], rope[node][1] - rope[node - 1][1]]
  dirs = []
  if 2 in (map(abs, rel)):
    if rel[0] > 0: dirs.append('L')
    elif rel[0] < 0: dirs.append('R')
    if rel[1] > 0: dirs.append('D')
    elif rel[1] < 0: dirs.append('U')

  move_node(dirs, node, rope, visits)

def solve(size, ops):
  rope, visits = [[0, 0] for _ in range(size)], []
  for dir, i in ops:
    for _ in range(int(i)): move_node([dir], 0, rope, visits)
  return len(set(map(str, visits)))

ops = [line.split() for line in open('input').read().splitlines()]
print('Part 1: ', solve(2, ops))
print('Part 2:', solve(10, ops))
