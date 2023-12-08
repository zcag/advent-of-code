import sys, re

turn = lambda dir, op: (dir + {'L': -1, 'R': 1}[op]) % 4
step = lambda x, y, dir: (x + [1, 0, -1, 0][dir], y + [0, 1, 0, -1][dir])
wrap = lambda grid, x, y, dir: (x%len(grid[y%len(grid)]), y%len(grid))
score = lambda x, y, dir: ((x+1)*4)+((y+1)*1000)+dir

def next_pos(grid, pos, dir):
  x, y = wrap(grid, *step(*pos, dir), dir)
  if grid[y][x] == ' ': return next_pos(grid, [x, y], dir)
  return x, y

def draw(grid, pos, dir):
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if (x, y) == pos: print('>v<^'[dir], end='')
      else: print(grid[y][x], end='')
    print()
  print('-'*10)

def solve(grid, ops):
  dir, y, x = 0, 0, grid[0].index('.')
  for op in ops:
    if op in 'LR':
      dir = turn(dir, op)
      continue
    for _ in range(int(op)):
      next_x, next_y = next_pos(grid, [x, y], dir)
      if grid[next_y][next_x] != '#': x, y = next_x, next_y
      else: break
  return x, y, dir


plane, ops = open(sys.argv[1]).read().split('\n\n')
ops, plane = re.split('([RL])', ops.strip()), plane.split('\n')
size = min([len(l.strip()) for l in plane])
sides = []

for y in range(0, len(plane), size):
  for x in range(0, len(plane[y]), size):
    x2, y2 = x+size, y+size
    side = [l[x:x2] for l in plane[y:y2]]
    print(side)
    input()


# print(size)

# print('Part 1:', score(*solve(grid, ops)))
