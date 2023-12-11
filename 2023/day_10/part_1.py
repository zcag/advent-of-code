import sys

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
ends = {up: down, down: up, left: right, right: left}
pipes = { '|': (up, down), '-': (left, right), 'L': (up, right), 
         'J': (up, left), '7': (left, down),   'F': (right, down), '.': () }

world = open(sys.argv[1]).read().strip().split('\n')
width, height = len(world[0]), len(world)
start = [(l.index('S'), y) for y, l in enumerate(world) if 'S' in l][0]

def move(x, y, dirx, diry):
    pipe, source_dir = pipes[world[y + diry][x + dirx]], ends[(dirx, diry)]
    if source_dir not in pipe: return None, None
    return [(x + dirx), (y + diry)], [end for end in pipe if end != source_dir][0]

for dr in (up, right):
    pos, path = start, [start]
    while True:
        pos, dr = move(*pos, *dr)
        path.append(pos)
        if not dr or (pos[0]+dr[0], pos[1]+dr[1]) == start: break
    if path[-1] != None: break

print('Part 1: ', int(len(path)/2))
