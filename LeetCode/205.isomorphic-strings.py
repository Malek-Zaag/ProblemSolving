#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        n =len(s)
        for i in range(n):
            if s[i] not in m1:
                m1[s[i]] = i
            if t[i] not in m2:
                m2[t[i]] = i
            if m1[s[i]] != m2[t[i]]:
                return False
        return True
        
        
# @lc code=end

