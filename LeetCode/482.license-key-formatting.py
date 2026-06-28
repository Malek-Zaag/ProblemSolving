#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s= s.upper()
        s=s.replace("-","")
        n=len(s)
        if n <=k:
            return s
        res=""
        while (n > k):
            res=s[n-k:n] + "-"+ res
            n= n-k
        return s[:n]+"-" + res[:-1]
# @lc code=end

