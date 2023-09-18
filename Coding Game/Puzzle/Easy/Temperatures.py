import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)
else : 
    temps=input().split()
    result=int(temps[0])
    if len(temps) ==1 : print(result)
    else :
        for i in temps[1:]:
            t=int(i)        
            if abs(result) > abs(t):
                result=t
            elif abs(result) == abs(t) :
                result=max(result,t)
        print(result)





