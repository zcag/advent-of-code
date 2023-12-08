import sys

limits = {'red': 12, 'green': 13, 'blue': 14}

input, output = open(sys.argv[1]).read().strip().split('\n'), 0

for game in input:
    nop = False
    id = int(game.split(' ')[1][:-1])
    turns = game.split(': ')[1].split(';')
    for turn in turns:
        a = turn.strip().split(' ')
        for ball, num in zip(a[1::2], a[::2]):
            ball = ball.replace(',', '')
            if limits[ball] < int(num):
                nop = True
    if not nop: output += id

print('Part 1: ', output)
