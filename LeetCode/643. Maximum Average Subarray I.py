import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    k = int(input())  
    if k == 1: return max(nums)
    maxi =curr_som=sum(nums[:k])
    for i in range(k,len(nums)):
        curr_som+= nums[i] - nums[i-k]
        maxi=max(curr_som, maxi)
    return (maxi / k)


for _ in range(int(input())):
    print(solve())