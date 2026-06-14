#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        if len (s) == 0: return 0
        l=s.split('')
        return len(l)
# @lc code=end

