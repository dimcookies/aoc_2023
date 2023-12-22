import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)

limit = {'red':12,'green':13, 'blue':14}

res = 0
for line in input:
    ar=line.split(':')
    id = int(ar[0].split(" ")[-1])
    print(id)
    wrong = False
    for j in ar[1].split(';'):
        if wrong == True:
            break
        for k in j.split(","):
            ar2 = k.strip().split(" ")
            print(ar2)          
            if limit[ar2[1].strip()] < int(ar2[0]):
                wrong = True
                break
    if not wrong:
        res+=id

print(res)
