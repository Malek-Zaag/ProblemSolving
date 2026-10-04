#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res=0
        for i in nums:
            if i == val: 
                res+=1
                nums[nums.index(i)] = "_"
        return len(nums) - res
# @lc code=end

sol = Solution()
print(sol.removeElement([3,2,2,3],3))
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))