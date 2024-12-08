#!/usr/bin/env python3
import sys
from itertools import combinations, chain

grid, nodemap = open(sys.argv[1]).read().strip().split('\n'), {}
for x,y,c in [(x,y,grid[y][x]) for y in range(len(grid)) for x in range(len(grid))]:
    if c != '.': nodemap[c] = nodemap.get(c, []) + [(x,y)]

bounds = lambda x, y: x in range(len(grid[0])) and y in range(len(grid))
nodepairs = lambda nodes: list(combinations(nodes, 2))
antinodes_pair = lambda n1, n2: list(chain(antinodes(n1, n2), antinodes(n2, n1)))
antinodes = lambda n1, n2: [cord for cord in [(n1[0]*2-n2[0], n1[1]*2-n2[1])] if bounds(*cord)]

solve_freq = lambda nodes: [antinodes_pair(*pair) for pair in nodepairs(nodes)]
solve_nodemap = lambda nodemap: set(chain(*[chain(*solve_freq(nodes)) for freq,nodes in nodemap.items()]))

print('Part 1:', len(solve_nodemap(nodemap)))

