#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n ==0: return 0
        i=1
        while (n >= i):
            n-=i
            i+=1
        return i-1
        
# @lc code=end

