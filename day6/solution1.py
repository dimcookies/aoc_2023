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
time = [int(i.strip()) for i in input[0].split(": ")[-1].split()]
distance = [int(i.strip()) for i in input[1].split(": ")[-1].split()]
print(time)
print(distance)

res = 1
for i in range(len(time)):
    t = time[i]
    d = distance[i]
    cnt = 0
    for j in range(1,t):
        remain = t-j
        dst = j*remain
        if dst >d:
            cnt +=1
    print(i, cnt)
    res = res * cnt
print(res)