from functools import cmp_to_key
import os

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            return 0

scr_dir = os.path.dirname(__file__)
fp_input = open(os.path.join(scr_dir, './input/input06.txt'), 'r')

n = int(fp_input.readline())
data =[]
for i in range(n):
    name, score = fp_input.readline().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)