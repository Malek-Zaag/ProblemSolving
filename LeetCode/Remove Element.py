import sys 
import os 

sys.stdin=open("./LeetCode/in.txt","r")
sys.stdout=open("./LeetCode/out.txt","w")

n=int(input())

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val: nums[i]="_"
        c = nums.count("_")
        for i in range(c):
            nums.remove("_")
        print(nums)
    