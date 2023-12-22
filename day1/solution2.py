import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
i_s = False
i_puzzle = 2
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)

num_dct = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

sum=0
for i in input:
    tmp = {}
    for j in num_dct.keys():
        for k in [m.start() for m in re.finditer(j, i)]:
            tmp[k] = num_dct[j]
    for j in range(1,10):
        for k in [m.start() for m in re.finditer(str(j), i)]:
            tmp[k] = j
    r1 = tmp[min(tmp.keys())]
    r2 = tmp[max(tmp.keys())]
    sum += int(str(r1)+str(r2))
#input = res 
print(sum)
#res = [[j for j in i if j.isdigit()] for i in input]
#print([int(i[0] + (i[-1] if len(i)>1 else i[0])) for i in res if len(i)>0]) 
#print(sum([int(i[0] + (i[-1] if len(i)>1 else i[0])) for i in res if len(i)>0]))     