#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h={}
        t=s.split(" ")
        if len(t) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in h and t[i] not in h.values():
                h[pattern[i]]= t[i]
                print(pattern[i],t[i])
            elif pattern[i] in h and t[i] == h[pattern[i]]:
                continue
            else:
                return False
        return True
# @lc code=end

