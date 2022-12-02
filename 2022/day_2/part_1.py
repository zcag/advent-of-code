games = [game.split() for game in open('input').read().strip().split('\n')]
rules = {'A': 'CAB', 'B': 'ABC', 'C': 'BCA'}

def score_1(opponent, me):
  me = chr(ord(me)-23)
  hand_score = '.ABC'.index(me)
  outcome_score = rules[opponent].index(me)*3
  return hand_score + outcome_score

def score_2(opponent, outcome):
  me = rules[opponent]['XYZ'.index(outcome)]
  hand_score = '.ABC'.index(me)
  outcome_score = 'XYZ'.index(outcome)*3
  return hand_score + outcome_score

print('Part 1: ', sum(map(lambda args: score_1(*args), games)))
print('Part 2: ', sum(map(lambda args: score_2(*args), games)))
