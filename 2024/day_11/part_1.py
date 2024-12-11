#!/usr/bin/env python3
import sys, itertools, memoization

stones = open(sys.argv[1]).read().strip().split()
split = lambda st: (str(int(st[:len(st)//2])), str(int(st[len(st)//2:])))

@memoization.cached
def blink(stone, it):
    if it == 0: return len(stone) if type(stone) != str else 1
    if type(stone) != str: return sum([blink(el, it) for el in stone])
    if stone == '0': return blink('1', it-1)
    if len(stone) % 2 == 0: return blink(split(stone), it-1)
    return blink(str(int(stone) * 2024), it-1)

print('Part 1:', blink(stones, 25))
print('Part 2:', blink(stones, 75))
