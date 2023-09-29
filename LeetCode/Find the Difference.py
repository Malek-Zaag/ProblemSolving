import sys 
import collections
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    # n = list(map(int, input().split()))
    s,t =input().split(",")
    dic=dict(collections.Counter(s))
    dic1=dict(collections.Counter(t))
    for i,j in enumerate(dic1):
        if j not in dic.keys() or dic1.get(j) != dic.get(j):
            print(j)
        
    
for _ in range(int(input())):
    solve()