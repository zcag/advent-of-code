import sys

opmap = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
input, pos, out = open(sys.argv[1]).read().strip().split('\n'), (1, 1), ''

for key_ops in input:
    for op in key_ops:
        pos = [min(max(n, 0), 2) for n in map(sum, zip(pos, opmap[op]))]
    out += '123 456 789'.split()[pos[1]][pos[0]]

print('Part 1: ', out)
