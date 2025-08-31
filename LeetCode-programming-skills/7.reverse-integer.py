#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

class Solution:
    def reverse(self,x : int) -> int:
        if (x == 0 ) : return x
        pos=False
        if (x >= 0):
            pos=True
        num= str(abs(x))
        num=num[::-1]
        while(num[0] =="0"):
            num=num[1:]
        num= int(num)
        if pos: 
            if (num > pow(2,31)-1): 
                print("we are out of range" + str(num))
                return 0
            else: return num
        else : 
            if (-num < -pow(2,31)): return 0
            else: return -num       
# @lc code=end

