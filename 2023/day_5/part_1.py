import sys, re

input = open(sys.argv[1]).read().strip().split('\n\n')
seeds = list(map(int, input[0].split()[1:]))
maps = [[list(map(int, l.split())) for l in i.split('\n')[1:]] for i in input[1:]]

def solve(val, values):
    if len(values) == 0: return val
    for r, l, n in values[0]:
        if l <= val < l+n: 
            return solve(r+(val-l), values[1:])
    return solve(val, values[1:])

print('Part 1: ', min([solve(seed, maps) for seed in seeds]))
