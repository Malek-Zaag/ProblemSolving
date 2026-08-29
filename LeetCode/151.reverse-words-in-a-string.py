#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(reversed(words))
    
sol = Solution()
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("  hello world  "))
print(sol.reverseWords("a good   example"))

# @lc code=end

