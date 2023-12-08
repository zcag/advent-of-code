import sys

dirs = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}
input, pos, visits = [dirs[c] for c in open(sys.argv[1]).read().strip()], (0, 0), set()

for dir in input:
    visits.add(pos)
    pos = tuple(map(sum, zip(pos, dir)))

print('Part 1: ', len(visits))
