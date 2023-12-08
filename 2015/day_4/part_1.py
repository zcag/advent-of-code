import sys, hashlib

input = open(sys.argv[1]).read().strip()

def solve(x, n, i=0):
    while not hashlib.md5((x+str(i)).encode()).hexdigest().startswith('0'*n): i += 1
    return i

print('Part 1: ', solve(input, 5), '\nPart 2: ', solve(input, 6))
