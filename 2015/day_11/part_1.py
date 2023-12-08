import sys, re

current = open(sys.argv[1]).read().strip()

def invalid(s):
    if len(set(re.findall(r"[iol]", s))) > 0: return True
    if len(set(re.findall(r"((.)\2+)", s))) < 2: return True
    if not any((ord(s[i+1])-ord(s[i]), ord(s[i+2])-ord(s[i+1])) == (1, 1) for i in range(len(s)-2)): 
        return True
    return False

def inc(s, d=1):
    new = chr(ord(s[-d])+1)
    if new == '{':
        return inc(s[:-d] + 'a' + (s[-d+1:] if d != 1 else ''), d=d+1)
    return s[:-d] + new + (s[-d+1:] if d != 1 else '')

while invalid(current): current = inc(current)
print('Part 1: ', current)
current = inc(current)

while invalid(current): current = inc(current)
print('Part 2: ', current)
