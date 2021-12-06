input = open('input').read().strip()

nums = input.split('\n')[0].split(',')
boards = [[list(filter(None, l.split(' '))) for l in i.split('\n')] for i in input.split('\n\n')[1:]]

combinations = lambda a: list(map(list, zip(*a[::-1])))+a

result = None
for num in nums:
  boards = [[['X' if num==c else c for c in row] for row in board] for board in boards]
  for board in boards:
    if ['X']*5 in combinations(board):
      result = sum([int(n) for n in sum(board, []) if n != 'X'])*int(num)
      break
  if result: break

print(result)
