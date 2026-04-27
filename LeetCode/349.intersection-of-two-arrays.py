#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1= set(nums1)
        s2= set(nums2)
        res=[i for i in s1 if i in s2]
        return res
        
# @lc code=end

