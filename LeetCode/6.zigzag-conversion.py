#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        g = [[] for _ in range(numRows)]
        i,k =0, 1
        for j in s:
            g[i].append(j)
            if (i ==0):
                k=1
            elif (i == numRows-1):
                k=-1
            i+=k
        
        res=""
        return "".join("".join(row) for row in g)
                
            
        
# @lc code=end

