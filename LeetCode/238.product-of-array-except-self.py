#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre =1 
        for i in range(n):
            res[i] = pre
            pre*= nums[i]
        suff = 1
        for i in range(n-1,-1,-1):
            res [i] *= suff
            suff *= nums[i]
        return res
# @lc code=end

