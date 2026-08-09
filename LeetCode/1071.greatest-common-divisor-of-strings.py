#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
            
        
# @lc code=end

sol = Solution()
print(sol.gcdOfStrings("ABCABC","ABC"))
print(sol.gcdOfStrings("ABABAB","ABAB"))
print(sol.gcdOfStrings("LEET","CODE"))
print(sol.gcdOfStrings("AAAAAB","AAA"))
