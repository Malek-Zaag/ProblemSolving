import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    if len(nums) ==1 : print(nums)
    odds , evens= [], []
    for i in nums:
        if i % 2 ==0 :
            odds.append(i)
        else : evens.append(i)
    nums[:]= odds[:] + evens[:]
    print(nums)


for _ in range(int(input())):
    solve()