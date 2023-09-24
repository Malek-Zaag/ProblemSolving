#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:     
        count=0
        jump_power=0
        end_jump=0
        for i in range(len(nums) -1):
            jump_power=max(jump_power,i+nums[i])
            if jump_power >= len(nums) -1:
                count+=1
                break           
            if i == end_jump :
                end_jump=jump_power
                count+=1
        return count   
# @lc code=end

