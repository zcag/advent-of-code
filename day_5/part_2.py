input = open('input').read().strip().split('\n')

direction = lambda x,y: bool(x < y) - bool(x > y)

all_points = []
for line in input:
  cords = [[int(n) for n in i.split(',')] for i in line.split(' -> ')]
  dirs = [direction(cords[0][0], cords[1][0]), direction(cords[0][1], cords[1][1])]

  pos = [cords[0][0], cords[0][1]]
  new_points = [[cords[0][0], cords[0][1]]]

  while pos != [cords[1][0], cords[1][1]]:
    pos = [pos[i] + (1*dirs[i]) for i in [0,1]]
    new_points += [pos[:]]
  all_points += new_points

d = { (i[0], i[1]):all_points.count(i) for i in all_points }
print(len([v for v in d.values() if v > 1]))
