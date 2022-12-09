from glom import assign, Path

def create_tree(ops):
  tree = { } # { 'a': 1234, 'b': {'c': 234, 'd': {}} }
  cwd = []
  for op in ops:
    if op == '$ cd ..': cwd.pop()
    elif op.startswith('$ cd '): cwd.append(op.split()[-1])
    elif op[0].isnumeric(): assign(tree, Path(*cwd, op.split()[1]), int(op.split()[0]), missing=dict)
  return tree

def dir_size(root, size_list=[]):
  total = 0
  for node, content in root.items():
    if type(content) == int: total += content
    else:
      size, _ = dir_size(content, size_list)
      total += size
      size_list.append(size)
  return total, size_list

root_size, dirs = dir_size(create_tree(open('input').read().splitlines()))

print('Part 1:', sum(dir for dir in dirs if dir <= 100000))
print('Part 2:', next((dir for dir in sorted(dirs) if dir >= 30000000 - (70000000 - root_size))))
