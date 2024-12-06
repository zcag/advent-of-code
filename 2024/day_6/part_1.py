#!/usr/bin/env python3
import sys

grid = open(sys.argv[1]).read().strip().split('\n')
pos = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '^'][0]

bounds = lambda x,y: 0 <= x < len(grid[0]) and 0 <= y < len(grid)
get = lambda x,y: grid[y][x] if bounds(x,y) else 'X'

diroffset = lambda dir: [(0,-1), (1, 0), (0, 1), (-1, 0)][dir]
walk = lambda x,y,dir: (x+diroffset(dir)[0],y+diroffset(dir)[1])

visits, dir = set(), 0
while(bounds(*pos)):
    visits.add(pos)
    front = walk(*pos, dir)
    if get(*front) == '#': dir = (dir+1)%4
    else: pos = front

print('Part 1:', len(visits))

