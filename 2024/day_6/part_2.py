#!/usr/bin/env python3
import sys, os, copy

grid = list(map(list, open(sys.argv[1]).read().strip().split('\n')))
x0, y0 = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '^'][0]
bounds = lambda x, y, grid: x in range(len(grid[0])) and y in range(len(grid))
get = lambda x, y, grid: grid[y][x] if bounds(x, y, grid) else '?'
walk = lambda x, y, dir: (x+[0,1,0,-1][dir], y+[-1,0,1,0][dir])

def run(x, y, grid):
    visits, dir = set(), 0
    while bounds(x, y, grid) and (x, y, dir) not in visits:
        visits.add((x, y, dir))
        while get(*walk(x, y, dir), grid) == '#': dir = (dir+1)%4
        x, y = walk(x, y, dir)
    return  False if bounds(x, y, grid) else {v[:2] for v in visits}

visits, loopstacles = run(x0, y0, grid), 0
for x, y in visits - {(x0,y0)}:
    grid[y][x] = '#'
    if not run(x0, y0, grid): loopstacles += 1
    grid[y][x] = '.'

print('Part 1:', len(visits), '\nPart 2:', loopstacles)
