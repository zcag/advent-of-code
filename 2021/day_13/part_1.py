dots, cmds = open('input').read().strip().split("\n\n")
dots = [[int(i) for i in l.split(',')] for l in dots.split('\n')]
cmds = [l.split(' ')[-1].split('=') for l in cmds.split('\n')]
axis, line = [[['x', 'y'].index(a), int(i)] for a,i in cmds][0]

for doti in range(len(dots)):
  if (dots[doti][axis] > line): dots[doti][axis] = line - (dots[doti][axis] - line)
print(len(set(map(tuple, dots))))
