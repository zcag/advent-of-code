import sys, itertools

input = [l.replace('lose ', 'l -').split() for l in open(sys.argv[1]).read().strip().split('\n')]
inst = {(i[0], i[-1][:-1]): int(i[3]) for i in input}

points = []
for p in itertools.permutations(set(n[0] for n in inst.keys())):
    ppoint = 0
    for i in range(len(p)):
        l, r = [0 if n == len(p) else (len(p)-1 if n == -1 else n) for n in [i-1, i+1]]
        ppoint += inst[(p[i], p[l])] + inst[(p[i], p[r])]
    points.append(ppoint)


print('Part 1: ', max(points))
