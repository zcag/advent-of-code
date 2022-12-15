import sys, re

def diff(x1, x2):
  return max(x1, x2) - min(x1, x2)

def coverage_ranges_for_plane(sensors, y):
  for s in sensors:
    new_dist = (s['range'] - diff(s['pos'][1], y))
    if new_dist > 0: yield [s['pos'][0]-new_dist, s['pos'][0]+new_dist]

def missing(ranges):
  ranges = sorted(ranges, key=lambda r: r[0])
  total = ranges[0]
  for start, end in ranges[1:]:
    if start <= total[1]: total = (total[0], max(total[1], end))
    else: return total[1] + 1

def find_beacon(sensors, limit):
  for y in range(limit+1):
    breaking = missing(coverage_ranges_for_plane(sensors, y))
    if breaking: return (breaking*4000000)+y

coords = [list(map(int, re.findall('=(-*\d+)', l))) for l in open(sys.argv[1]).read().strip().split('\n')]
sensors = [ {'pos': [sx, sy], 'range': diff(sx, bx) + diff(sy, by) } for sx, sy, bx, by in coords]
print('Part 2:', find_beacon(sensors, 4000000))
