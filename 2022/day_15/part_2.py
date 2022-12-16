import sys, re
from shapely.geometry import Polygon
from shapely.ops import unary_union

diff = lambda x1, x2: max(x1, x2) - min(x1, x2)
square = lambda side: Polygon([[0, 0], [0, side], [side, side], [side, 0]], [])
xy_from_bounds = lambda bounds: [bounds[2]-1, bounds[1]+1]
tuning = lambda x, y: int((x*4000000)+y)

coords = [list(map(int, re.findall('=(-*\d+)', l))) for l in open(sys.argv[1]).read().strip().split('\n')]
sensors = [ [sx, sy, diff(sx, bx) + diff(sy, by)] for sx, sy, bx, by in coords]
coverage = unary_union([Polygon([[x, y+d], [x+d, y],[x, y-d], [x-d, y]],[]) for x, y, d in sensors])
print('Part 2:', tuning(*xy_from_bounds((square(4000000) - coverage).bounds)))
