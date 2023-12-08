import sys, re, itertools

inst, dirs, pos = *open(sys.argv[1]).read().strip().split('\n\n'), 'AAA'
inst = itertools.cycle(map(int, inst.replace('R', '1').replace('L', '0')))
dirs = {c: (l,r) for c, l, r in [re.findall('[A-Z]+', d) for d in dirs.split('\n')]}

for i, d in enumerate(inst): 
    pos = dirs[pos][d]
    if pos == 'ZZZ':
        print('Part 1: ', i+1)
        break
