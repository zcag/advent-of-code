nodes = {}
for l in open('input').read().strip().split('\n'):
  key, val = l.split('-')
  for key, val in [[key, val], [val, key]]:
    if key in nodes: nodes[key].append(val)
    else: nodes[key] = [val]

visitable = lambda n,ls: (n.upper() == n) or n not in ls
def find_paths(start='start', end='end', path = [], level = 1):
  path += [start]
  if start == end: return [path[:]]
  if start not in nodes: return []
  all_paths = []
  for node in nodes[start]:
    if visitable(node, path):
      for i in find_paths(node, end, path[:], level+1):
        all_paths.append(i)
  return all_paths

print(len(find_paths()))
