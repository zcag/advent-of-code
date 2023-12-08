import sys, re, itertools

inpt = open(sys.argv[1]).read().strip().split('\n')
ops = [(l.replace('turn', '').split()[0], *map(int, re.findall('\d+', l))) for l in inpt]

def incrange(x, y):
    ls = sorted([x, y])
    return range(ls[0], ls[1]+1)

grid = [[False for _ in range(1000)] for _ in range(1000)]
for op, x, y, x2, y2 in ops:
    for xx, yy in itertools.product(incrange(x, x2), incrange(y, y2)): 
        grid[xx][yy] = True if op == 'on' else (False if op == 'off' else not grid[xx][yy])
print(sum(map(sum, grid)))
