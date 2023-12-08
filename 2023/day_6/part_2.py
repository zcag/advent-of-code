import sys, re

input = [int(''.join(re.findall('\d', l))) for l in open(sys.argv[1]).read().strip().split('\n')]
solve = lambda time, record: sum([t*(time-t) > record for t in range(time)])
print('Part 2: ', solve(*input))
