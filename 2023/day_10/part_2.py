import sys, itertools

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
ends = {up: down, down: up, left: right, right: left}
pipes = { '║': (up, down), '═': (left, right), '╚': (up, right), 
         '╝': (up, left), '╗': (left, down),   '╔': (right, down), ' ': () }

mapping = str.maketrans("|-LJ7F.", "║═╚╝╗╔ ")
inpt = open(sys.argv[1]).read().strip().translate(mapping)
world = list(map(list, inpt.split('\n')))
width, height = len(world[0]), len(world)
start = [(l.index('S'), y) for y, l in enumerate(world) if 'S' in l][0]

worldc = lambda x, y: world[y][x]
def move(x, y, dirx, diry):
    pipe, source_dir = pipes[worldc(x+dirx, y+diry)], ends[(dirx, diry)]
    if source_dir not in pipe: return None, None
    return ((x + dirx), (y + diry)), [end for end in pipe if end != source_dir][0]

for dr in (up, right):
    pos, path = start, [start]
    while True:
        pos, dr = move(*pos, *dr)
        path.append(pos)
        if not dr or (pos[0]+dr[0], pos[1]+dr[1]) == start: break
    if path[-1] != None: break

all_coords = [(x, y) for y in range(height) for x in range(width)]
for x, y in all_coords: world[y][x] = world[y][x] if (x, y) in path else ' '

closed = []
for x in range(width):
    inside, lcorner = False, ''
    for y in range(height):
        c = worldc(x, y)
        if c == ' ' and inside: closed.append((x,y))
        elif c == '═': inside = not inside
        elif c in '╔╗S': lcorner = c
        elif c == '╝' and lcorner in '╔S': inside = not inside
        elif c == '╚' and lcorner in '╗S': inside = not inside

print('Part 2:', len(closed))

# def printm(world, closed):
#     for y, row in enumerate(world):
#         for x, c in enumerate(row):
#             print('X' if (x, y) in closed else c, end='')
#         print()
#     print('-'*20)
#
