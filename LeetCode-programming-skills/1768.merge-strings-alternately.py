#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLength= min(len(word1),len(word2))
        res=""
        for i in range(0,minLength):
            res+=word1[i]
            res+=word2[i]
        if len(word1) > minLength:
            return res+ word1[minLength:]
        else:  return res+word2[minLength:]
# @lc code=end

