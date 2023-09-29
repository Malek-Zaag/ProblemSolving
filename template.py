############################################ Libraries #####################################################

import bisect
import sys
import math
import os
import time
from queue import PriorityQueue
from io import BytesIO, IOBase
from collections import defaultdict, Counter
from bisect import bisect_right
# import sys

# sys.stdin=open('./in.txt',"r")
########################################### Definitions ###################################################

INF = sys.maxsize
BUFSIZE = 4096

############################################# Inputs ######################################################

# def inp(): return sys.stdin.readline().rstrip("\r\n")  # read line as string
# def inp_int(): return int(inp())  # read input as integer. '1' -> 1
# def inp_int_list(): return list(map(int, inp().split()))
# def inp_str_list(): return list(inp())

############################################# Solution ######################################################

import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    n = list(map(int, input().split()))
    res = 0
    print(res)


for _ in range(int(input())):
    solve()