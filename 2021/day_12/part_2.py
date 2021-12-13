nodes = {}
for l in open('input').read().strip().split('\n'):
  key, val = l.split('-')
  for key, val in [[key, val], [val, key]]:
    if val == 'start': continue
    if key in nodes: nodes[key].append(val)
    else: nodes[key] = [val]

def visitable(n,ls):
  if n.upper() == n: return True
  if n not in ls: return True
  ls = list(filter(lambda x: x.lower() == x, ls))
  return len(set(ls)) == len(ls)

def find_paths(start='start', end='end', path = []):
  path += [start]
  if start == end: return [path[:]]
  if start not in nodes: return []
  all_paths = []
  for node in nodes[start]:
    if visitable(node, path):
      for i in find_paths(node, end, path[:]):
        all_paths.append(i)
  return all_paths

print(len(find_paths()))
