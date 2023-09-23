#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mydict={"I": 1,"V" :5,"X":10,"L" :50,"C" :100,"D" :500,"M":1000}
        res=0
        i=0
        while i < len(s) :
            if i+1 < len(s) and mydict[s[i]] < mydict[s[i+1]]:
                res-=mydict[s[i]]
            else :
                res+=mydict[s[i]]
            i+=1
        return res
        
# @lc code=end

