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
#print(input)
seed = [int(i) for i in input[0].split(": ")[-1].split()]
#print(seed)

dt = []
ar1 = []
for i in input[2:]:
    if i.find("map:") != -1:
        continue

    if not i.strip():
        dt.append(ar1)
        #print(dct)
        ar1 = []
        continue

    ar = [int(j) for j in i.strip().split()]
    ar1.append(ar)
    #print(ar)
dt.append(ar1)
print(dt)


res = []
for val in seed:
    print(val)
    for ar in dt:
        for i in ar:
            to = i[0]
            fr = i[1]
            range = i[2]

            if val >= fr and val <= fr + range:
                val = to + abs(fr-val)
                break
                
        
        print("\t", val)
    res.append(val)
print(min(res))