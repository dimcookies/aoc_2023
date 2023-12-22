import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
i_s = False
i_puzzle = 2
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

s = 0
input = my_input.readlines(file_input)
cnum = 1
cards = {}
cache = {}
for i in input:
    print(i)
    ar = i.split(":")
    id = int(ar[0].split(" ")[-1])
    ar = ar[1].strip().split(" | ")
    winning = set([int(j) for j in ar[0].strip().split(" ") if j])
    mine = [int(j) for j in ar[1].strip().split(" ") if j]
    cards[id] = (winning,mine)

my_cards =[i for i in range(1, len(cards)+1)]
print(my_cards)

total = 0
while len(my_cards) > 0:
    #print(my_cards)
    total +=1
    tmp = my_cards.pop()

    cnt = 0
    if tmp in cache:
        cnt = cache[tmp]
    else:
        tmp_card = cards[tmp]
        winning = tmp_card[0]
        mine = tmp_card[1]
        
        for i in mine:
            if i in winning:
                cnt +=1
        cache[tmp] = cnt
    #print(tmp, cnt)
    for i in range(tmp+1, tmp+1+cnt):
        my_cards.append(i)

print(total)