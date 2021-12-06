import pandas as pd

input = open('input').read().strip().split('\n')

direction = lambda x,y: bool(x < y) - bool(x > y)

d = dict()
for line in input:
  cords = [[int(n) for n in i.split(',')] for i in line.split(' -> ')]
  dirs = [direction(cords[0][0], cords[1][0]), direction(cords[0][1], cords[1][1])]

  start_pos = tuple(cords[0])
  d[start_pos] = d.get(start_pos, 0) + 1

  pos = [cords[0][0], cords[0][1]]
  while pos != [cords[1][0], cords[1][1]]:
    pos = [pos[i] + (1*dirs[i]) for i in [0,1]]
    d[tuple(pos)] = d.get(tuple(pos), 0) + 1

print(len([v for v in d.values() if v > 1]))
