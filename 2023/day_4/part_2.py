import sys, re, math, functools

input = open(sys.argv[1]).read().strip().split('\n')

parse = lambda l: [set(i.split()) for i in re.findall('[:|]\s([\d\s]+)', l)]
cards = [len(input)] + [len(l&r) for l,r in map(parse, input)]

@functools.cache
def calc(x):
    return sum([calc(i) for i in range(x+1, x+1+cards[x])]) + 1

print('Part 2: ', calc(0) - 1)
