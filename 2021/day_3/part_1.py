lines = open('input').read().strip().split('\n')

matrix = [[0]*12, [0]*12]
for line in lines:
  for pos, bit in enumerate(line):
    matrix[int(bit)][pos] += 1

gamma = ''.join(['1' if b1>b0 else '0' for b0,b1 in tuple(zip(matrix[0], matrix[1]))])
epsilon = gamma.translate({49: 48, 48: 49})

print(int(gamma, 2)*int(epsilon, 2))
