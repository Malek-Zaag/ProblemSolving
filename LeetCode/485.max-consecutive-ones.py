#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        counter=0
        i=0
        while (i < len(nums)):
            if (nums[i] ==1):
                counter+=1           
            else :
                m=max(m,counter)
                counter=0
            i+=1
        m=max(m,counter)
        return m
        
# @lc code=end

