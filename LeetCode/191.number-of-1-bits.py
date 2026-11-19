#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res =0
        while (n > 0):
            bit = n % 2 
            if bit ==1: res+=1
            n = n //2 
        return res 
            
        
# @lc code=end

sol = Solution()

print(sol.hammingWeight(11))
print(sol.hammingWeight(128))
print(sol.hammingWeight(2147483645))
