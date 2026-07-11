#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        neg=False
        if not s:
            return 0
        if (s[0] == "-"):
            neg=True
            s=s[1:]
        elif (s[0] == "+"):
            s=s[1:]
        if not s:
            return 0
        start = 0
        while start < len(s) and s[start] == "0":
            start += 1
        s=s[start:]
        if not s:
            return 0
        for i,j in enumerate(s):
            if not j.isdigit():
                s=s[:i]
                break
        if not s:
            return 0
        if len(s) > 10:
            return -(2**31) if neg else 2**31 - 1
        res = int(s) if neg==False else -int(s)
        if res < -(2**31):
            return -(2**31)
        if res > 2**31 - 1:
            return 2**31 - 1
        return res
        
# @lc code=end
