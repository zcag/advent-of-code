#!/usr/bin/env python3
import sys

input = list(map(int, open(sys.argv[1]).read().strip()+"0"))
enumel_as_obj = lambda el: {'id': el[0], 'size': el[1][0], 'free': el[1][1]}
disk = list(map(enumel_as_obj, enumerate([input[i:i+2] for i in range(0, len(input), 2)])))

diskrepr = lambda disk: ''.join([(str(d['id'])*d['size'])+'.'*d['free'] for d in disk])
print(diskrepr(disk))

out, id = [], 0
while id < len(disk) :
    if len(out) and out[-1]['id'] == id: out[-1]['size'] += disk[id]['size']
    else: out.append(disk[id])
    disk[id]['size'] = 0

    for attempt in disk[::-1]:
        if attempt == disk[id]: break
        if not attempt['size']: break
        if disk[id]['free'] >= attempt['size']:
            out.append(attempt)
            disk[id]['free'] -= attempt['size']
            disk.remove(attempt)
            break
            # out.append([disk[-1]['id'], disk[id]['free']])
            # disk[-1]['size'] -= disk[id]['free']
            # break
    # else: print(outrepr(out))
    print(diskrepr(out))
    id += 1



# pos, res = 0, 0
# for id, size in out:
#     for _ in range(size):
#         res += pos * id
#         pos += 1
#
# print('Part 2:', res)
