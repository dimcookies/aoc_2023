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

#for i in input:
#    print("".join(i))

for i in range(1, len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'O':
            landed = -1
            for k in range(i-1, -1, -1):
                if input[k][j] == '.':
                    landed = k                    
                else:
                    break
            if landed != -1:
                input[landed][j] = 'O'
                input[i][j] = '.'
# for i in input:
#     print("".join(i))
s = 0            
for i in range(0, len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'O':
            s += len(input) - i

print(s)
