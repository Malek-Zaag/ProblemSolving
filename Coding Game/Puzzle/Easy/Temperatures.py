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
    for i in temps:
        t=int(i)        
        if abs(int(result)) > abs(t):
            result=t
        elif abs(int(result)) == abs(t):
            result=abs(t)
    print(result)




