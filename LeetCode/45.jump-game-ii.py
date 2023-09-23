#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0  or len(nums) ==1 : return 0
        rest=len(nums)-1 - nums[0]
        if rest <= 0:
            return 1
        i=1
        count=1
        jump_power=nums[0]
        while rest > 0 and i < len(nums)-1:
            jump_power-=1
            if nums[i] < jump_power:
                i+=1
            else :
                jump_power=max(jump_power,nums[i])
                rest=rest - jump_power
                count+=1
                i+=1           
        return count   
# @lc code=end

