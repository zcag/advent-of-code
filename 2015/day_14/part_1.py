import sys, re

solve = lambda v,f,r: (int(2503/(f+r))*v*f) + min(f, 2503-int(2503/(f+r))*(f+r))*v
out = [solve(*map(int, re.findall('\d+', l))) for l in open(sys.argv[1]).read().strip().split('\n')]
print('Part 1: ', max(out))
