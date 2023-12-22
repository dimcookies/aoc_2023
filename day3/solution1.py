import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
for i in input:
    print(i)

for i in range(len(input)):
    line = input[i]
    result = [j for j in re.split(r'\D+', line) if j]
    print(result)
#    for j in results:
#        pass