#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total=0
        for i,j in enumerate(timeSeries[:-1]):
            if (j+duration) < timeSeries[i+1]:
                total+=duration
            else:
                total+=(timeSeries[i+1]-j)
        return total+duration
        
# @lc code=end

