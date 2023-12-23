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

input = my_input.readlines(file_input)
print(input)

dct = {"R":0, "D":0}
for i in input:
    d = i[0]
    l = int(i[2])
    if d in dct:
        dct[d]+=l
print(dct)
ar = []
for i in range(dct["D"]+1):
    ar.append(["."]*(dct["R"]+1))

pos = [0,0]
ar[pos[0]][pos[1]] = "#"
for cmd in input:
    print(pos)
    print(cmd)
    d = cmd[0]
    l = int(cmd[2])
    if d =='D':
        for i in range(l):
            pos[0]+=1
            ar[pos[0]][pos[1]] = "#"            
    elif d=='U':
        for i in range(l):
            pos[0]-=1
            ar[pos[0]][pos[1]] = "#"           
    elif d=='L':
        for i in range(l):
            pos[1]-=1
            ar[pos[0]][pos[1]] = "#"
    elif d=='R':
        for i in range(l):
            pos[1]+=1
            ar[pos[0]][pos[1]] = '#'        

for i in ar:
    print(i)

s = 0
for i in range(len(ar)):
    pending = 0
    in_block = False
    for j in range(len(ar[i])):
        if ar[i][j] == '#':
            s+=1
            if in_block:
                s+=pending            
            in_block = not in_block
        elif in_block:
                pending +=1
    #print(s)

print(s)                   