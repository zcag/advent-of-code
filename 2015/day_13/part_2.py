import sys, itertools

input = [l.replace('lose ', 'l -').split() for l in open(sys.argv[1]).read().strip().split('\n')]
inst = {(i[0], i[-1][:-1]): int(i[3]) for i in input}

points = []
for p in itertools.permutations(list(set(n[0] for n in inst.keys())) + ['me']):
    ppoint = 0
    for i in range(len(p)):
        l, r = [p[0] if n == len(p) else (p[len(p)-1] if n == -1 else p[n]) for n in [i-1, i+1]]
        if p[i] == 'me': continue
        ppoint += inst[(p[i], l)] if l != 'me' else 0
        ppoint += inst[(p[i], r)] if r != 'me' else 0
    points.append(ppoint)


print('Part 2: ', max(points))
