import sys, re, functools, operator

input = [map(int, m.split()) for m in re.findall(':((?:\s+\d+)+)', open(sys.argv[1]).read())]
solve = lambda time, record: sum([t*(time-t) > record for t in range(time)])
print('Part 1: ', functools.reduce(operator.mul, map(solve, *input)))
