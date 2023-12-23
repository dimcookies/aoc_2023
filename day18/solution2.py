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
input = my_input.readlines_int_array(file_input)

my_s = 0
for line in input:
    print(line)
    all = [line]    
    while True:
        res = []
        for i in range(0,len(line)-1):
            res.append(line[i+1]-line[i])
        #print(res)
        all.append(res)
        line=res
        if len(set(res)) == 1 and res[0] == 0:
            break
    s=0
    for i in range(len(all)-2, -1, -1):
       #print(all[i][0], s)
       s=all[i][0] - s
       #print(s)
    print(s)
    my_s +=s
print(my_s)