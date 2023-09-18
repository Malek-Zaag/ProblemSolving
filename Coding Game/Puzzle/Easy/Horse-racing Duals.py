import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
tab=[]
for i in range(n):
    pi = int(input())
    tab.append(pi)
tab.sort(reverse=True)
if len(tab)==1 : 
    print(tab[0])
else:
    res=tab[0]- tab[1]
    for i in range(1,len(tab)-1):
        if tab[i] - tab[i+1] < res:
            res=tab[i] - tab[i+1]
    print(res)          


