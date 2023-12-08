import sys, re, math

input = open(sys.argv[1]).read().strip().split('\n')

parse = lambda l: [set(i.split()) for i in re.findall('[:|]\s([\d\s]+)', l)]
output = sum([math.floor(2**(len(l&r)-1)) for l,r in map(parse, input)])

print('Part 1: ', output)
