import sys
import math
import string
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
res=""
for i in range(h):
    row = input()
    # print(row[26*4 :26*4 + 4])
    for j in t:
        if j in string.ascii_uppercase:
            res+=row[(ord(j) - 65) *l:(ord(j) - 65) *l + l]
        elif j in string.ascii_lowercase :
            res+=row[(ord(j) - 97) *l:(ord(j) - 97) *l + l]
        else:
            res+=row[26*l :26*l + l]
    res+="\n"
print(res)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)