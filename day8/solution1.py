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

inst = input[0]

dct = {}
for i in input[2:]:
    dct[i[0:3]] = (i[7:10], i[12:15])

state = 'AAA'

cnt = 0
while state != 'ZZZ':
    i = inst[cnt%len(inst)]
    if(i=='L'):
        state = dct[state][0]
    else:
        state = dct[state][1]
    cnt +=1
print(cnt)