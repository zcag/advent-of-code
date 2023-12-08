import sys

input, output = open(sys.argv[1]).read().strip().split('\n'), 0

for game in input:
    limits = {'red': 0, 'green': 0, 'blue': 0}

    id = int(game.split(' ')[1][:-1])
    turns = game.split(': ')[1].split(';')
    for turn in turns:
        a = turn.strip().split(' ')
        for ball, num in zip(a[1::2], a[::2]):
            ball = ball.replace(',', '')
            if limits[ball] < int(num):
                limits[ball] = int(num)
    powa = limits['red'] * limits['green'] * limits['blue']
    output += powa

print('Part 2: ', output)
