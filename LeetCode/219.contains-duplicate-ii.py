#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        show={}
        for i in range(len(nums)):
            if nums[i] in show and abs(i - show[nums[i]]) <= k:
                return True
            else:
                show[nums[i]]=i        
        return False
# @lc code=end

