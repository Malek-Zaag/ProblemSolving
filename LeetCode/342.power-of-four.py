#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0: 
            return False
        if n == 1:
            return True
        if n % 4 ==0:
            return self.isPowerOfFour(n /4)
        else: 
            return False
# @lc code=end

