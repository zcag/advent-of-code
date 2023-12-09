import sys

input = [list(map(int, l.split())) for l in open(sys.argv[1]).read().strip().split('\n')]

seq = lambda l: [l[i+1] - l[i] for i in range(len(l)-1)]
seqs = lambda l: [l] if set(l) == {0} else [l, *seqs(seq(l))]
lsum = lambda l: sum([n*(-1 if i%2 else 1) for i, n in enumerate(l)])

print('Part 2: ', sum([lsum([s[0] for s in seqs(i)]) for i in input]))
