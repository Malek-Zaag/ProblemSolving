import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    sum_l,sum_r=0,sum(nums)
    for i,j in enumerate(nums):
        sum_r-=j
        if sum_r == sum_l:
            return i
        sum_l+=j
    return -1



for _ in range(int(input())):
    print(solve())