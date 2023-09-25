#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import string  
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) ==0 or len(s) == 1  : return True
        s=[i.lower() for i in s if i in string.ascii_lowercase or i in string.ascii_uppercase or i in string.digits]    
        print("".join(s))
        reversed=s[::-1]
        print("".join(reversed))
        if "".join(reversed) == "".join(s):
            return True
        else : return False
        
        
# @lc code=end

