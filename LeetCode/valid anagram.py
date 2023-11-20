import sys 
from collections import Counter
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

for i in range(t):
    s,t=input().split(",")
    dict1,dict2=Counter(s),Counter(t)
    if dict1== dict2:
        print(True)
    else : print(False)
    
    
    