import sys, re, itertools

inpt = open(sys.argv[1]).read().strip().replace('turn off', '-1').replace('turn on', '1').replace('toggle', '2')
ops = [(int(l.split()[0]), *map(int, re.findall('[\s,](\d+)', l))) for l in inpt.split('\n')]

def incrange(x, y):
    ls = sorted([x, y])
    return range(ls[0], ls[1]+1)

grid = [[False for _ in range(1000)] for _ in range(1000)]
for op, x, y, x2, y2 in ops:
    for xx, yy in itertools.product(incrange(x, x2), incrange(y, y2)): 
        if not grid[xx][yy]+op == -1: grid[xx][yy] += op

print(sum(map(sum, grid)))
