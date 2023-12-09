import sys, re

input, pos, dr = re.findall('([LR])(\d+)', open(sys.argv[1]).read()), (0, 0), 0

bound = lambda x, l, r: l if x>r else (r if x<l else x)
turn = lambda c, r: bound(c+(1 if r=='R' else -1), 0, 3)
walk = lambda x, y, d: [(x, y-1), (x+1, y), (x, y+1), (x-1, y)][d]

visits = []
for r, s in input:
    dr = turn(dr, r)
    for i in range(int(s)):
        pos = walk(*pos, dr)
        if pos in visits: 
            print('Part 2:', sum(map(abs, pos)))
            quit()
        visits.append(pos)
