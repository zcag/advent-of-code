import collections,math

data = [(100, 'input'), (10, 'testinput')][0]
area = [[int(cell) for cell in '9'+row+'9'] for row in ('9'*data[0] + '\n' + open(data[1]).read().strip() + '\n' + '9'*data[0]).split('\n')]

get_adj = lambda x,y,ar: [ar[y-1][x], ar[y+1][x], ar[y][x-1], ar[y][x+1]]
mapvis = lambda ar: '\n'.join([''.join(['\033[91m'+str(c)+'\033[0m' if c > -1 else '\033[94m'+str(c*-1)[-1]+'\033[0m' for c in r[1:-1]]) for r in ar[1:-1]])

basin_index = -1
found_flag = True
while found_flag:
  found_flag = False
  for y, row in list(enumerate(area))[1:-1]:
    for x, cell in list(enumerate(row))[1:-1]:
      if cell > -1 and cell != 9:
        bigger_adj = list(filter(lambda n: n<=cell, get_adj(x,y,area)))
        if len(bigger_adj) == 0:
          area[y][x] = basin_index
          basin_index -= 1
          found_flag = True
      elif cell < 0:
        for cord in [(y-1, x), (y+1, x), (y, x-1), (y,x+1)]:
          if area[cord[0]][cord[1]] > -1 and area[cord[0]][cord[1]] != 9:
            area[cord[0]][cord[1]] = cell
            found_flag = True
  first_run = False

print(mapvis(area))
print(math.prod(sorted(list(collections.Counter(sum(area, [])).values()))[-4:-1]))
