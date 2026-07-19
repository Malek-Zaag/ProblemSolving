#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors=[]
        if  num % 2 != 0 : return False
        sum=0
        for i in range(1, num //2 + 1):
            if num % i ==0:
                sum+=i
        for i in divisors:
            sum+=i
        return True if sum == num else False
# @lc code=end

