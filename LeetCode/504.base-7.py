#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start


class Solution:
    def convertToBase7(self, num: int) -> str:
        base=abs(num)
        if num ==0: return "0"
        output=""
        while (base > 0):
            output = str(base % 7) + output 
            base//=7
        return "-" + output if num < 0 else output

solution = Solution()
print(solution.convertToBase7(10))
# @lc code=end

