import sys, itertools

input = [list(map(int, l.split())) for l in open(sys.argv[1]).read().strip().split('\n')]
valid = lambda t: all(sum(oe for oei, oe in enumerate(t) if oei != ei) > e for ei, e in enumerate(t))
print('Part 1: ', sum(map(valid, input)))
