import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
from collections import Counter

i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

s = 0
input = my_input.readlines(file_input)

vls = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
vls.reverse()


res = {}
for line in input:
    ar = line.split()
    cards = [j for j in ar[0]]
    amount = int(ar[1])
    dct = Counter(cards)
    vl = 1
    if(len(dct) == 1):
        vl = 7
    elif(len(dct) == 2):
        if 4 in dct.values():
            vl = 6
        else:
            vl = 5
    elif(len(dct) == 3):
        if 3 in dct.values():
            vl = 4
        else:
            vl = 3
    elif(len(dct) == 4):
        if 2 in dct.values():
            vl = 2
    res[ar[0]] = (amount, vl)

def comparator(item):
    main = item[1][1]
    secondary = "".join([hex(vls.index(i)+1) for i in item[0]]).replace("0x","")
    return str(main) + secondary


sorted_dict_by_values = dict(sorted(res.items(), key=comparator))

res = 0
cnt = 1
for i in sorted_dict_by_values.values():
    res +=cnt*i[0]
    cnt +=1

print(res)