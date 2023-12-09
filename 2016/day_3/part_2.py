import sys, itertools

input = sum(map(list, zip(*[list(map(int, l.split())) for l in open(sys.argv[1]).read().strip().split('\n')])), [])
input = [input[i: i+3] for i in range(0, len(input), 3)]

valid = lambda t: all(sum(oe for oei, oe in enumerate(t) if oei != ei) > e for ei, e in enumerate(t))
print('Part 2: ', sum(map(valid, input)))
