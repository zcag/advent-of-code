lines = open('input').read().strip().split('\n')

depth, hpos, aim = 0, 0, 0
for line in lines:
  cmd, val = line.split(" ")
  val = int(val)

  if cmd == 'forward':
    hpos += val
    depth += aim * val
  elif cmd == 'down':
    aim += val
  else:
    aim -= val

print(hpos*depth)
