#!/usr/bin/env python3
import sys, os, copy

grid = list(map(list, open(sys.argv[1]).read().strip().split('\n')))
x0, y0 = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '^'][0]
bounds = lambda x, y, grid: x in range(len(grid[0])) and y in range(len(grid))
walk = lambda x, y, dir: (x+[0,1,0,-1][dir], y+[-1,0,1,0][dir])

def run(x, y, grid):
    visits, dir = set(), 0
    while bounds(x, y, grid):
        if (x, y, dir) in visits: return False
        visits.add((x, y, dir))

        front = walk(x, y, dir)
        if bounds(*front, grid) and grid[front[1]][front[0]] == '#': dir = (dir+1)%4
        x, y = walk(x, y, dir)

    return {v[:2] for v in visits}

visits, loopstacles = run(x0, y0, grid), 0
for x, y in visits - {(x0,y0)}:
    grid[y][x] = '#'
    if not run(x0, y0, grid): loopstacles += 1
    grid[y][x] = '.'

print('Part 1:', len(visits), '\nPart 2:', loopstacles)
