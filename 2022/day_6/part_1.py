chars = open('input').read().strip()
unique = lambda chunk: len(set(chunk)) == len(chunk)
marker_generator = lambda size: ( i+size for i in range(len(chars)-size) if unique(chars[i:i+size]) )
print('Part 1:', next(marker_generator(4)), '\nPart 2: ', next(marker_generator(14)))
