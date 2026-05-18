#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        
        
        def helper(n):
            rep=""
            while (n >0):
                rep+= n % 2
                n //=2
            return rep[::-1]
        comp="".join(["0" if i =="1" else "1" for i in helper(num).split()])
        print(comp)
        return int(comp,2)
# @lc code=end

