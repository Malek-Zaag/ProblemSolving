#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output=""
        while (columnNumber >0):
            columnNumber-=1
            output= chr(columnNumber%26 + ord('A'))+ output
            columnNumber//=26
        return output
# @lc code=end

