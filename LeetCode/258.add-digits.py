#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if (num < 10): return num
        while (num > 10):
            num=self.helper(num)
            print(num)
        return self.helper(num)
    
    def helper(self,num):
        sum=0
        while (num > 9):
            sum+=num % 10
            num=num // 10
        sum+=num
        return sum
        
        
# @lc code=end

