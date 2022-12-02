games = [game.split() for game in open('input').read().strip().split('\n')] # [[A,Y], [B,X], [C,Z]]
rules = {'A': 'CAB', 'B': 'ABC', 'C': 'BCA'} # opponent: 'Lose-Draw-Win',  A/B/C: Rock/Paper/Scissors
score = lambda me, outcome: '.ABC'.index(me) + 'XYZ'.index(outcome)*3 # Rock/Paper/Scissors: 1/2/3 + Win/Draw/Lose: 6/3/0

def part_1(opponent, me):
  me = chr(ord(me)-23) # XYZ to ABC
  outcome = 'XYZ'[rules[opponent].index(me)]
  return score(me, outcome)

def part_2(opponent, outcome):
  me = rules[opponent]['XYZ'.index(outcome)]
  return score(me, outcome)

print('Part 1: ', sum(map(lambda args: part_1(*args), games)))
print('Part 2: ', sum(map(lambda args: part_2(*args), games)))
