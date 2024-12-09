#!/usr/bin/env python3
import sys

input = list(map(int, open(sys.argv[1]).read().strip()+"0"))
enumel_as_obj = lambda el: {'id': el[0], 'size': el[1][0], 'free': el[1][1]}
disk = list(map(enumel_as_obj, enumerate([input[i:i+2] for i in range(0, len(input), 2)])))

out, id = [], 0
while id < len(disk) :
    if len(out) and out[-1][0] == id: out[-1][1] += disk[id]['size']
    else: out.append([id, disk[id]['size']])
    disk[id]['size'] = 0
    while disk[id]['free']:
        if not disk[-1]['size']: break
        if disk[id]['free'] >= disk[-1]['size']:
            out.append([disk[-1]['id'], disk[-1]['size']])
            disk[id]['free'] -= disk[-1]['size']
            disk.pop()
        else:
            out.append([disk[-1]['id'], disk[id]['free']])
            disk[-1]['size'] -= disk[id]['free']
            break
    id += 1


pos, res = 0, 0
for id, size in out:
    for _ in range(size):
        res += pos * id
        pos += 1

print('Part 1:', res)
