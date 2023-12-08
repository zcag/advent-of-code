import sys, re, itertools, math

inst, dirs = open(sys.argv[1]).read().strip().split('\n\n')
inst = list(map(int, inst.replace('R', '1').replace('L', '0')))
dirs = {c: (l,r) for c, l, r in [re.findall('[A-Z0-9]+', d) for d in dirs.split('\n')]}

positions = [d for d in dirs.keys() if d[-1] == 'A']
z_counts = []

for pos in positions:
    for i, d in enumerate(itertools.cycle(inst)): 
        pos = dirs[pos][d]
        if pos[-1] == 'Z':
            z_counts.append(i+1)
            break

print('Part 2: ', math.lcm(*z_counts))
