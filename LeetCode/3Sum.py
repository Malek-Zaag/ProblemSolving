import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())


for i in range(t):
    nums=[int(i) for i in input().split(",")]
    nums.sort()
    res=[]
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        s=nums[i]+nums[l]+nums[r]
        while l<r :
            if s <0:
                l+=1
            elif s > 0:
                r+=1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l < r and nums[l] == nums[l+1]:
                        l += 1
                while l < r and nums[r] == nums[r-1]:
                        r -= 1
                l += 1; r -= 1          
    print(res)