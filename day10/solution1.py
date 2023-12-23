import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
from collections import Counter
import time

i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

s = 0
input = my_input.readlines_str_array(file_input)
print(input)

start = ()
for i in range(0, len(input)):
    for j in range(0,len(input[i])):
        if(input[i][j]=='S'):
            start = (i,j)

def move(current, dct):
    steps = 1
    while True:
        #print(current)
        dct[current] = steps
        steps +=1
        s = input[current[0]][current[1]]
        #print(s)
        next = []
        if s=='F':
            next = [(current[0]+1, current[1]), (current[0], current[1]+1)]
        elif s=='-':
            next = [(current[0], current[1]-1), (current[0], current[1]+1)]
        elif s=='7':
            next = [(current[0], current[1]-1), (current[0]+1, current[1])]
        elif s=='|':
            next = [(current[0]+1, current[1]), (current[0]-1, current[1])]
        elif s=='L':
            next = [(current[0]-1, current[1]), (current[0], current[1]+1)]
        elif s=='J':
            next = [(current[0]-1, current[1]), (current[0], current[1]-1)]
        elif s=='S':
            return
        elif(s=='.'):
            raise Exception("invalid")
        ar = [i for i in next if i not in dct.keys()]
        if not ar:
                return
        current = ar[0]
    print(dct)
           
        

print(start)
dct1 = {start:0}
move((start[0], start[1]+1), dct1)
print(dct1)

dct2 = {start:0}
move((start[0]+1, start[1]), dct2)
print(dct2)

dct={}
for i in dct1.keys():
    dct[i] = min(dct1[i], dct2[i])
print(dct)
print(max(dct.values()))