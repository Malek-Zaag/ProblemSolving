import string
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    k=int(input())
    s=input()
    l=r=0
    curr=maxi=0
    for r in range(len(s)):
        if r >= k:
                if s[r-k] in ['a','e','u','i','o']:
                    curr -= 1
        if s[r] in ['a','e','u','i','o']:
            curr+=1       
        maxi=max(maxi,curr)
    return maxi

for _ in range(int(input())):
    print(solve())