import sys, re, functools

diff = lambda x1, x2: max(x1, x2) - min(x1, x2)
join_sets = lambda sets: functools.reduce(lambda x,y: x|y, sets, set())
beacons_on_plane = lambda sensors, y: set([pos[0] for pos in [s['beacon'] for s in sensors] if pos[1] == y])
sensor_range_on_plane = lambda pos, dist, y: set(range(pos[0]-(dist - diff(pos[1], y)), pos[0]+(dist - diff(pos[1], y))+1))
total_coverage_on_plane = lambda sensors, y: join_sets([sensor_range_on_plane(s['pos'], s['range'], y) for s in sensors])

coords = [list(map(int, re.findall('=(-*\d+)', l))) for l in open(sys.argv[1]).read().strip().split('\n')]
sensors = [{'pos': [sx, sy], 'beacon': [bx, by] ,'range': diff(sx, bx) + diff(sy, by)} for sx, sy, bx, by in coords]
print('Part 1:', len(total_coverage_on_plane(sensors, 2000000) - beacons_on_plane(sensors, 2000000)))
