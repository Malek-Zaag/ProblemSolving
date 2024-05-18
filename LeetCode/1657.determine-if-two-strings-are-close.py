#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start

import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) : return False
        count1, count2=collections.Counter(word1),collections.Counter(word2)
        return True if sorted(list(count1.keys()))==sorted(list(count2.keys())) and sorted(list(count1.values()))==sorted(list(count2.values())) else False
        
        
        
# @lc code=end

