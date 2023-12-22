import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import functools
i_s = False
i_puzzle = 2
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)

limit = {'red':12,'green':13, 'blue':14}

res = 0
for line in input:
    ar=line.split(':')
    id = int(ar[0].split(" ")[-1])
    print(id)
    tmp = {}
    for j in ar[1].split(';'):
        for k in j.split(","):
            ar2 = k.strip().split(" ")
            print(ar2)          
            t1 = int(ar2[0])
            if ar2[1] in tmp:
                tmp[ar2[1]] = max(tmp[ar2[1]],t1)
            else:
                tmp[ar2[1]] = t1

    res += functools.reduce(lambda x,y: x*y, tmp.values())
print(res)
    