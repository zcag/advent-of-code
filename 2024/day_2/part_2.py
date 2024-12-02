#!/usr/bin/env python3
import sys

input = [list(map(int,l.split(" "))) for l in open(sys.argv[1]).read().strip().split('\n')]
ordered = lambda l: sorted(l) == l or sorted(l)[::-1] == l
safe_dist = lambda l: all([0 < abs(l[i-1] - l[i]) < 4 for i in range(1, len(l))])
safe = lambda l: ordered(l) and safe_dist(l)
safeish = lambda l: any(map(safe, [l[:i]+l[i+1:] for i in range(len(l))]))
print('Part 1:', sum(map(safe, input)), '\nPart 2:', sum(map(safeish, input)))
