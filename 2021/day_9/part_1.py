area = [[int(cell) for cell in '9'+row+'9'] for row in ('9'*100 + '\n' + open('input').read().strip() + '\n' + '9'*100).split('\n')]

get_adj = lambda x,y,ar: [ar[y-1][x], ar[y+1][x], ar[y][x-1], ar[y][x+1]]

total_risk = 0
for y, row in list(enumerate(area))[1:-1]:
  for x, cell in list(enumerate(row))[1:-1]:
    bigger_adj = list(filter(lambda n: n<=cell, get_adj(x,y,area)))
    if len(bigger_adj) == 0: total_risk += cell+1

print(total_risk)
