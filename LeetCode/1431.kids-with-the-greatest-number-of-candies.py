#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
import math
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res=[]
        for i in candies:
            if i+ extraCandies >= mx:
                res.append(True)
            else: res.append(False)
        return res
    
sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))
print(sol.kidsWithCandies([4,2,1,1,2],1))
        
# @lc code=end

