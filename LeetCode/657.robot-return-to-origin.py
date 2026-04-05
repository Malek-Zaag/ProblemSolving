#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for i in moves:
            match i:
                case "U":
                    y+=1
                case "D":
                    y-=1
                case "L":
                    x-=1
                case _:
                    x+=1
        if (x == y ==0): return True
        else: return False
# @lc code=end

