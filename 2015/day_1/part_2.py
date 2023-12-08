import sys

input, floor = open(sys.argv[1]).read(), 0
for i, c in enumerate(input):
    floor += 1 if c == '(' else -1
    if floor == -1: 
        print('Part 2: ', i+1)
        break
