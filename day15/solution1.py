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

input = my_input.readlines(file_input)

def hash(input):
    s = 0
    for i in input:
        s+=ord(i)
        s*=17
        s=s%256
    return s

print(sum([hash(i) for i in input[0].strip().split(",")]))