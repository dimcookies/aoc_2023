import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
from collections import Counter

i_s = False
i_puzzle = 2
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

s = 0
input = my_input.readlines(file_input)

inst = input[0]

dct = {}
for i in input[2:]:
    dct[i[0:3]] = (i[7:10], i[12:15])

cnt = 0

state = [i for i in dct.keys() if i[-1] == 'A']
print(state)
cond = ['Z'] * len(inst)
while True:
    if [i[-1] for i in state] == cond:
        break
    i = inst[cnt%len(inst)]
    state = [dct[st][0] if(i=='L') else dct[st][1]  for st in state]
    #print(cnt, state)
    if(cnt %100000==0):
        print(cnt)
    cnt +=1
print(cnt)