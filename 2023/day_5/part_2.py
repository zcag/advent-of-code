import sys, re

input = open(sys.argv[1]).read().strip().split('\n\n')

sin = list(map(int, input[0].split()[1:]))
seeds = [range(sin[i], sin[i]+sin[i+1]) for i in range(0, len(sin), 2)]

bake = lambda d,s,r: (range(s, s+r), d-s)
maps = [[bake(*list(map(int, l.split()))) for l in i.split('\n')[1:]] for i in input[1:]]

def apply_map(seeds, mapping):
    shifted = []
    unshifted = [*seeds]
    for m, offset in mapping:
        for seed in unshifted[:]:
            if seed.stop <= m.start or seed.start >= m.stop: continue
            intersect = range(max(seed.start, m.start), min(seed.stop, m.stop))
            left, right = range(seed.start, intersect.start), range(intersect.stop, seed.stop)
            
            intersect = range(intersect.start+offset, intersect.stop+offset)
            shifted.append(intersect)
            unshifted.remove(seed)
            if left: unshifted.append(left)
            if right: unshifted.append(right)

    return shifted + unshifted

for mapping in maps: seeds = apply_map(seeds, mapping)
print(min([seed.start for seed in seeds]))
