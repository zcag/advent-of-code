import sys

input = open(sys.argv[1]).read()
print('Part 1: ', input.count('(') - input.count(')'))
