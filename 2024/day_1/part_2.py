#!/usr/bin/env python3
import sys

inl, inr = zip(*[map(int, l.split("   ")) for l in open(sys.argv[1]).read().strip().split('\n')])
print('Part 2:', sum([inr.count(i)*i for i in inl]))
