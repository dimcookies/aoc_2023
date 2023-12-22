import sys
import os

is_sample = True
file_input = "sample1" if is_sample else "input1"

def readlines(file_input):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x: x.strip(),f.readlines()))

def readlines_array(file_input, sep=" "):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x: list(map(lambda y: y.strip(), x.strip().split(sep))),f.readlines()))                

def readlines_str_array(file_input):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x:list(x.strip()),f.readlines()))                

def readlines_int(file_input):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x: int(x.strip()),f.readlines()))                

def readlines_int_safe(file_input, safe_value):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x: int(x.strip()) if x.strip() else safe_value,f.readlines()))    

def readlines_int_array(file_input, sep=" "):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x: list(map(lambda y: int(y.strip()), x.strip().split(sep))),f.readlines()))                

def readlines_int_array_single(file_input):
    with open(os.path.join(sys.path[1], file_input), "r") as f:
        return list(map(lambda x: list(map(lambda y: int(y.strip()), list(x.strip()))),f.readlines()))                
