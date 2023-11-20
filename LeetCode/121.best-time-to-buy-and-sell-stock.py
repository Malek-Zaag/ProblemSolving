#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l,r=0,0
        while r < (len(prices)):
            if prices[r] > prices[l]:
                profit=max(profit,prices[r] - prices[l])
            else : 
                l=r
            r+=1
        if profit < 0: return 0
        else : return profit
        
# @lc code=end

