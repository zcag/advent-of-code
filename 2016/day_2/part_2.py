import sys

opmap = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
pad = ['XX1XX', 'X234X', '56789', 'XABCX', 'XXDXX']
input, x, y, out = open(sys.argv[1]).read().strip().split('\n'), 0, 2, ''

for key_ops in input:
    for op in key_ops:
        new_x, new_y = [min(max(n, 0), 4) for n in map(sum, zip([x, y], opmap[op]))]
        if pad[new_y][new_x] != 'X': x, y = new_x, new_y
    out += pad[y][x]

print('Part 2: ', out)
