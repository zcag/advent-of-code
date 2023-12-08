import sys

dirs = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}
input, visits = [dirs[c] for c in open(sys.argv[1]).read().strip()], {(0, 0)}

for inst, pos in [(input[::2], (0, 0)), (input[1::2], (0, 0))]:
    for dir in inst:
        pos = tuple(map(sum, zip(pos, dir)))
        visits.add(pos)

print('Part 2: ', len(visits))
