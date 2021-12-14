board = [[int(c) for c in l] for l in open('simpletestinput').read().strip().split('\n')]
size = len(board)

def neighbours(x,y):
  points = [[x-1,y-1],[x, y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y]]
  return list(filter(lambda p: (max(p) < size) and (min(p) > -1), points))

total = 0
flashed = []
def flash(x, y):
  global total
  if board[y][x] > 9 and (x,y) not in flashed:
    flashed.append((x,y))
    total += 1
    for x2,y2 in neighbours(x,y):
      board[y2][x2] += 1
      flash(x2, y2)
    board[y][x] = 0

for step in range(3):
  print('\n------- Step', step, '-------')
  for i in board: print(*i)
  for y in range(size):
    for x in range(size):
      board[y][x] += 1
      flash(x, y)

print(total)
