import sys

def line_coords(x1, y1, x2, y2):
  dir = 0 if y1 == y2 else 1
  bounds = [[x1, x2], [y1, y2]][dir]
  if bounds[0] < bounds[1]: points = range(bounds[0], bounds[1]+1)
  else: points = range(bounds[1], bounds[0]+1)

  if dir: return [[x1, y] for y in points]
  else: return [[x, y1] for x in points]

def possibilities(grid, sand):
  positions = [[sand[0], sand[1]+1], [sand[0]-1, sand[1]+1], [sand[0]+1, sand[1]+1]]
  return [pos for pos in positions if grid[pos[1]][pos[0]] == '.']

def solve(lines, abyss=True):
  max_x, max_y = 1000, max([pos[1] for line in lines for pos in line])
  if not abyss: max_y, lines = max_y+2, lines + [[[0, max_y+2], [max_x-1, max_y+2]]]
  grid = [['.' for x in range(max_x)] for y in range(max_y+1) ]

  for line in lines:
    for i, part in enumerate(line[:-1]):
      for pos in line_coords(*part, *line[i+1]):
        grid[pos[1]][pos[0]] = '#'

  sand_count = 0
  sand = [500, 0]
  while True:
    if abyss and sand[1] == max_y: return sand_count
    possible_positions = possibilities(grid, sand)
    if len(possible_positions) != 0: sand = possible_positions[0]
    else:
      grid[sand[1]][sand[0]] = 'o'
      sand_count += 1
      if (not abyss) and sand == [500, 0]: return sand_count
      sand = [500, 0]

input = open(sys.argv[1]).read().strip().split('\n')
lines = [[list(map(int,pos.split(','))) for pos in row.split(' -> ')] for row in input]

print('Part 1:', solve(lines))
print('Part 2:', solve(lines, False))
