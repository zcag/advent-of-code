import sys, re

input, pos, dr = re.findall('([LR])(\d+)', open(sys.argv[1]).read()), (0, 0), 0

bound = lambda x, l, r: l if x>r else (r if x<l else x)
turn = lambda c, r: bound(c+(1 if r=='R' else -1), 0, 3)
walk = lambda x, y, d, s: [(x, y-s), (x+s, y), (x, y+s), (x-s, y)][d]

for r, s in input:
    dr = turn(dr, r)
    pos = walk(*pos, dr, int(s))

print('Part 1: ', sum(map(abs, pos)))
