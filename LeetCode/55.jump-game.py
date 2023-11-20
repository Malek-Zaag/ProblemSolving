#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_power=nums[0]
        jumper=0
        while jump_power > 0 and jumper != len(nums)-1:
            jumper+=1
            jump_power-=1
            jump_power=max(jump_power, nums[jumper])
        if jumper ==len(nums) -1 : return True
        else : return False
            
# @lc code=end

