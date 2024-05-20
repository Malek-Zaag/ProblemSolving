#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lower=int(n/2)+1
        factors=[]
        for i in range(1,lower):
            if n % i ==0:
                factors.append(i)
        factors.append(n)
        print(factors,len(factors))
        return -1 if k > len(factors) else factors[k-1]
# @lc code=end

