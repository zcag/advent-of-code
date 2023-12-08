import sys
from itertools import cycle, product

offset = lambda x, y, ls: [[p[0]+x, p[1]+y] for p in ls]
extend_to = lambda grid, to: grid + [[1]+[0]*7+[1] for i in range(to-len(grid))]
collides = lambda grid, obj: any((grid[p[1]][p[0]] == 1 for p in obj))
highest = lambda grid: next((y for y in range(len(grid)-1, -1, -1) if 1 in grid[y][1:-1]))

ops = cycle(['<.>'.index(c)-1 for c in open(sys.argv[1]).read().strip()])
rocks = cycle([list(zip(range(4),[0]*4)), list(zip([1,1,1,0,2],[2,0,1,1,1])), list(zip([0,1,2,2,2],[0,0,0,1,2])),
               list(zip([0]*4,range(4))), list(product(*([[0,1]]*2)))])

grid, resting = [[1]*9], 0
while resting < 2022:
  spawn_height = highest(grid)+4
  grid, rock = extend_to(grid, spawn_height+4), offset(3, spawn_height, next(rocks)[::])
  while True:
    op_attempt = offset(next(ops), 0, rock)
    if not collides(grid, op_attempt): rock = op_attempt

    fall_attempt = offset(0, -1, rock)
    if not collides(grid, fall_attempt): rock = fall_attempt
    else:
      for p in rock: grid[p[1]][p[0]] = 1
      break
  resting += 1
print('Part 1:', highest(grid))
