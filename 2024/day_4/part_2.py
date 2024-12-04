#!/usr/bin/env python3
import sys

offsets = [ [[1,1], [0,0], [-1, -1]], [[-1,1], [0,0], [1,-1]] ]
grid = open(sys.argv[1]).read().strip().split('\n')
coords = [(x,y) for y in range(len(grid)) for x in range(len(grid[0]))]

valid = lambda x,y: 0 <= y < len(grid) and 0 <= x < len(grid[0])
get = lambda x,y,xo,yo: grid[y+yo][x+xo] if valid(x+xo, y+yo) else '.'

getword = lambda x,y,ls: ''.join([get(x,y,*coord) for coord in ls])
getwords = lambda x,y: [getword(x,y,offset) for offset in offsets]

ismas = lambda word: word in ['MAS', 'SAM']
print('Part 2:', sum([all(map(ismas, getwords(*coord))) for coord in coords]))

