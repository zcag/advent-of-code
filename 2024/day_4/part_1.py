#!/usr/bin/env python3
import sys

offsets = [
        [[0,i] for i in range(4)], [[0,i*-1] for i in range(4)],
        [[i,0] for i in range(4)], [[i*-1, 0] for i in range(4)],
        [[i,i] for i in range(4)], [[i*-1,i*-1] for i in range(4)],
        [[i,i*-1] for i in range(4)], [[i*-1,i] for i in range(4)]
        ]
grid = open(sys.argv[1]).read().strip().split('\n')
coords = [(x,y) for y in range(len(grid)) for x in range(len(grid[0]))]

valid = lambda x,y: 0 <= y < len(grid) and 0 <= x < len(grid[0])
get = lambda x,y,xo,yo: grid[y+yo][x+xo] if valid(x+xo, y+yo) else '.'

getword = lambda x,y,ls: ''.join([get(x,y,*coord) for coord in ls])
getwords = lambda x,y: [getword(x,y,offset) for offset in offsets]

solve_coord = lambda coord: getwords(*coord).count('XMAS')
print('Part 1:', sum(map(solve_coord, coords)))

