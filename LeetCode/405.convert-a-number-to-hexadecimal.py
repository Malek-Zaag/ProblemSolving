#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hexdigits="0123456789abcdef"
        res=""
        if num <0:
            num = (1 << 32) + num
        while num >0:
            temp=num / 16
            digit=hexdigits[temp]
            res=digit + res
            num=num //16
        return res        
# @lc code=end

