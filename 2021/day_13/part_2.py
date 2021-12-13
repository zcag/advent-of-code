dots, cmds = open('input').read().strip().split("\n\n")
dots = [[int(i) for i in l.split(',')] for l in dots.split('\n')]
cmds = [l.split(' ')[-1].split('=') for l in cmds.split('\n')]
cmds = [[['x', 'y'].index(a), int(i)] for a,i in cmds]

for axis, line in cmds:
  for doti in range(len(dots)):
    if (dots[doti][axis] > line):
      dots[doti][axis] = line - (dots[doti][axis] - line)

for y in range(max(dot[1] for dot in dots)+1):
  for x in range(max(dot[0] for dot in dots)+1):
    print(u"\u2588" if [x,y] in dots else ' ', end='')
  print()
