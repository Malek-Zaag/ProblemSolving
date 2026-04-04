#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        cycle=[]
        while (n != 1):
            s= helper(n)
            if (s in cycle): 
                return False
            cycle.append(s)
            n = s
        return True
    
def helper(n):
    while(n >9):
        return pow((n % 10),2) + helper(n//10)
    return pow(n,2)
# @lc code=end

        