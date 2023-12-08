import sys, re, math

grid = open(sys.argv[1]).read().strip()
width, grid = re.search(r"\n", grid).span()[0], grid.replace('\n', '')

index_to_point = lambda i: ((i%width), math.floor(i/width))
sym_to_coord = lambda s: index_to_point(s.span()[0])
num_to_coord = lambda n: [n.group(), list(map(index_to_point, range(*n.span())))]

symbols = set(map(sym_to_coord, re.finditer(r"[^\d\.\n]", grid)))
nums = map(num_to_coord, re.finditer(r"\d+", grid))

neighbours = lambda x,y: [(x+x1, y+x2) for x1, x2 in zip([*[-1]*3, *[0]*3, *[1]*3], [-1, 0, 1]*3)]

res = []
for num, coords in nums:
    nes = [neighbours(x, y) for x, y in coords]
    nes = {y for x in nes for y in x}
    if len(nes & symbols) > 0: res.append(int(num))


print('Part 1: ', sum(res))
