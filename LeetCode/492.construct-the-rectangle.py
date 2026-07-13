#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqroot= math.sqrt(area)
        w=sqroot
        for i in range(int(sqroot),0,-1):
            if area % i == 0:
                return [area//i, i]
# @lc code=end

