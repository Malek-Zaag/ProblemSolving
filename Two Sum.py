import sys 



sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")


t=int(input())

for i in range(t):
    target=int(input())
    nums=input().split(",")
    nums=[int(num) for num in nums]
    for index,j in enumerate(nums):
        rest=target-j
        if rest in nums[index+1:]:
            newnums=nums[index+1:]
            if (rest== j):
                print(index,newnums.index(rest)+1+index)
            else :
                print(index,nums.index(rest))
            break
        