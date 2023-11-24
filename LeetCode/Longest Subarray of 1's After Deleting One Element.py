import collections
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    # res =[]
    # first= False
    # maxi=len(res)
    # if nums[0] == 0 : nums[::] = nums[1:]
    # for i in nums:
    #     if i == 1 :
    #         res.append(i)
    #         maxi=max(len(res),maxi)
    #     elif i == 0 and first == False:
    #         first=True
    #         continue
    #     elif i ==0 and first == True : 
    #         res=[]
    #         first=False
    #         maxi=max(0,maxi)
    # if maxi == len(nums) : return maxi-1
    # return maxi
    n = len(nums)
    left = 0
    zeros = 0
    ans = 0
    for right in range(n):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        ans = max(ans, right - left + 1 - zeros)
    return ans - 1 if ans == n else ans
    
for _ in range(int(input())):
    print(solve())