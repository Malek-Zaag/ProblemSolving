#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.capitalize() == word: return True
        if word.islower() : return True
        if word.isupper(): return True
        return False
    
sol = Solution()
print(sol.detectCapitalUse("USA"))
print(sol.detectCapitalUse("FlaG"))
# @lc code=end

