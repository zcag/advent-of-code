#!/usr/bin/env python3
import sys

grid = [list(map(int, r)) for r in open(sys.argv[1]).read().strip().split("\n")]
coords = [(x,y) for y in range(len(grid)) for x in range(len(grid[0]))]
level_coords = {level:{(x,y) for x,y in coords if grid[y][x] == level} for level in range(10)}

bounds = lambda x, y: x in range(len(grid[0])) and y in range(len(grid))
neighs = lambda x, y: {(x,y) for x,y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if bounds(x,y)}
valid_neighs = lambda x, y, level: neighs(x, y) & level_coords[level+1]

def walk(x, y, level):
    if (x,y) in level_coords[9]: return 1
    return sum([walk(*neigh, level+1) for neigh in valid_neighs(x, y, level)])

print('Part 2:', sum([walk(x, y, 0) for x,y in level_coords[0]]))
