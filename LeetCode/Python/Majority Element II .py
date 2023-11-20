
import sys 
import collections
import math
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    if len(nums) ==0 or len(nums)==1 : return  nums  
    n=math.floor(len(nums) /3 )
    res=[]
    count=collections.Counter(nums)
    for i in count:
        if count[i] > n : res.append(i)
    return res
            


for _ in range(int(input())):
    print(solve())