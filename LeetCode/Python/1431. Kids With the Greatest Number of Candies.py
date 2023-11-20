import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    candies = list(map(int, input().split()))
    extraCandies=int(input())
    res=[]
    maxi=max(candies)
    for i in candies:
        if i + extraCandies >= maxi:
            res.append(True)
        else : res.append(False) 
    return res


for _ in range(int(input())):
    print(solve())