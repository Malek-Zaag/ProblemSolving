#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k % len(nums)
        rotate=nums[-k:]
        nums[:]=nums[:-k]
        nums[:]=rotate[:] + nums[:]
        
# @lc code=end

