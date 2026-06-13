#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root= math.sqrt(num)
        if root == int(root): return True 
        else : return False
        
# @lc code=end

