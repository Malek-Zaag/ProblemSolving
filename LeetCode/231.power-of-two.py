#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n ==1): 
            return True 
        if (n == 0 ): return False
        if (n % 2 == 0 ):
            return self.isPowerOfTwo(n // 2)
        else: 
            return False
        
# @lc code=end

