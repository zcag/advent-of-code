import sys, os
from itertools import cycle, product

offset = lambda x, y, ls: [[p[0]+x, p[1]+y] for p in ls]
extend_to = lambda grid, to: grid + [[1]+[0]*7+[1] for i in range(to-len(grid))]
collides = lambda grid, obj: any((grid[p[1]][p[0]] == 1 for p in obj))
highest = lambda grid: next((y for y in range(len(grid)-1, -1, -1) if 1 in grid[y][1:-1]))

def draw(grid, rock=[], clear=True, wait=True, bot_padding=-3):
  if clear: os.system('clear')
  rows, columns = os.popen('stty size', 'r').read().split()
  rows = int(rows) - (bot_padding+3)
  bot_row = len(grid)-rows+1 if len(grid) > rows else 0
  for y in range(len(grid)-1, bot_row-1, -1):
    for x, c in enumerate(grid[y]):
      if [x, y] in rock: print('#', end='')
      elif c == 1:
        if y == 0: print('-', end='')
        elif x == 0 or x == len(grid[0])-1: print('|', end='')
        else: print('#', end='')
      else: print('.', end='')
    print(' ', y)
  print('-'*40)
  if wait: input()

def jump_repeating(grid, resting, chunk_size=10):
  if len(grid) < chunk_size*2: return resting
  top = highest(grid)
  chunk = grid[top-chunk_size:top+1]
  for i in range(top-chunk_size, 0, -1):
    check = grid[i-1:i+chunk_size]
    if check == chunk:
      draw(grid, wait=False, bot_padding=-300)
      print('Found!: ', i, resting_history, top, resting_history.get(i))
      draw(chunk, clear=False)
  return resting

ops = cycle(['<.>'.index(c)-1 for c in open(sys.argv[1]).read().strip()])
rocks = cycle([list(zip(range(4),[0]*4)), list(zip([1,1,1,0,2],[2,0,1,1,1])), list(zip([0,1,2,2,2],[0,0,0,1,2])),
               list(zip([0]*4,range(4))), list(product(*([[0,1]]*2)))])

grid, resting, resting_history, limit = [[1]*9], 0, {}, 1000000000000
while resting < limit:
  if [1]*9 == grid[highest(grid)] and len(grid) > 10:
    print(resting)
    print(len(grid))
    quit()

  spawn_height = highest(grid)+4
  grid, rock = extend_to(grid, spawn_height+4), offset(3, spawn_height, next(rocks)[::])
  while True:
    op_attempt = offset(next(ops), 0, rock)
    if not collides(grid, op_attempt): rock = op_attempt

    fall_attempt = offset(0, -1, rock)
    if not collides(grid, fall_attempt):
      rock = fall_attempt
    else:
      for p in rock: grid[p[1]][p[0]] = 1
      resting += 1
      resting_history[highest(grid)] = resting
      resting = jump_repeating(grid, resting)
      break
print('Part 2:', highest(grid))

