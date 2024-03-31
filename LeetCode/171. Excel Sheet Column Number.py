import sys 
import string
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")

def solve():
        nums = list(input().split())
        res=0
        #print(nums)
        nums[:] = nums[::-1]
        for i in range(len(nums)):
                res+= (string.ascii_uppercase.index(nums[i])+1) * pow(26,i)
        print(res)    

    
    
for _ in range(int(input())):
    solve()