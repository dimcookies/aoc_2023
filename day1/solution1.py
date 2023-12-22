import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)
pr(i_s, input)


res = [[j for j in i if j.isdigit()] for i in input]
print(sum([int(i[0] + (i[-1] if len(i)>1 else i[0])) for i in res if len(i)>0]))     