#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 5 ==0:
            return self.isUgly(n / 5)
        elif n % 3 ==0:
            return self.isUgly( n /3 )
        elif n % 2==0:
            return self.isUgly(n /2 )
        else:
            return False  
# @lc code=end

