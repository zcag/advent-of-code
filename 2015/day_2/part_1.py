import sys

input = [map(int, l.split('x')) for l in open(sys.argv[1]).read().strip().split('\n')]
paper = lambda l, w, h: 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print('Part 1: ', sum(map(paper, *zip(*input))))
