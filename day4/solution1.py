import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

s = 0
input = my_input.readlines(file_input)
for i in input:
    ar = i.split(":")
    ar = ar[1].strip().split(" | ")
    winning = [int(j) for j in ar[0].strip().split(" ") if j]
    mine = [int(j) for j in ar[1].strip().split(" ") if j]
    cnt = 0
    for j in mine:
        if j in winning:
            cnt+=1
    
    s+=pow(2,cnt-1) if cnt>0 else 0
print(s)
