import sys

input = [map(int, l.split('x')) for l in open(sys.argv[1]).read().strip().split('\n')]
ribbon = lambda l, w, h: (sum(sorted([l, w, h])[:2])*2) + (l*w*h)
print('Part 2: ', sum(map(ribbon, *zip(*input))))
