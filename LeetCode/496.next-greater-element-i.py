#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            j = nums2.index(i)
            found = False
            for l in nums2[j + 1:]:
                if l > i:
                    ans.append(l)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
# @lc code=end

