import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

for i in range(t):
    target=int(input())
    nums=[int(i) for i in input().split(",")]
    if len(nums) == 2: print([0,1])
    else:
        for i,j in enumerate(nums):
            if (target-j) in nums[i+1:]:
                print([i,nums.index(target-j,i+1)])
                break
            else: continue