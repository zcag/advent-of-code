#!/usr/bin/env python3
import sys, os, copy

def draw(pos, dir, visits, obstacles, grid, info=""):
    os.system('clear')
    print(info)
    print()
    visit_chars = {}
    for x,y,dir in visits:
        if (x,y) not in visit_chars: visit_chars[(x,y)] = '|-|-'[dir]
        elif visit_chars[(x,y)] != '|-|-'[dir]: visit_chars[(x,y)] = '+'

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x,y) in obstacles: print('O', end='')
            elif (x,y) in visit_chars: print(visit_chars[(x,y)], end='')
            elif (x,y) == pos: print('^>v<'[dir], end='')
            else: print(grid[y][x], end='')
        print()
    input()


grid = list(map(list, open(sys.argv[1]).read().strip().split('\n')))
initial_pos = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '^'][0]

bounds = lambda x,y, grid: 0 <= x < len(grid[0]) and 0 <= y < len(grid)
get = lambda x,y, grid: grid[y][x] if bounds(x,y, grid) else 'X'

walk = lambda x,y,dir: (x+[0,1,0,-1][dir],y+[-1,0,1,0][dir])
turn = lambda dir: (dir+1)%4

def with_obstacle(obstacle):
    out = copy.deepcopy(grid)
    if obstacle is not None and bounds(*obstacle, out):
        out[obstacle[1]][obstacle[0]] = '#'
    return out

runs = 0

def run(start_pos, start_dir, obstacle=None):
    global runs
    runs += 1

    visits, loobstacles, pos, dir, grid = set(), set(), start_pos[::], start_dir, with_obstacle(obstacle)

    while(bounds(*pos, grid)):
        if (*pos, dir) in visits: return loobstacles, 'loops'
        visits.add((*pos, dir))

        # if not add_obstacles: draw(pos, dir, visits, loobstacles, grid)
        # draw(pos, dir, visits, loobstacles, grid, add_obstacles)

        if get(*walk(*pos, dir), grid) == '#': dir = turn(dir)

        front = walk(*pos, dir)
        if obstacle is None and front != initial_pos and run(start_pos, start_dir, front)[-1] == 'loops':
            loobstacles.add(front)


        pos = walk(*pos, dir)
    return loobstacles, 'ends'


# print('Part 1:', len(run(start_pos, 0, True)[0]))
print('Part 2:', len(run(initial_pos, 0)[0]))
print("runs: ", runs)
