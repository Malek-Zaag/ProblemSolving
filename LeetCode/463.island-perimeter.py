#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        permiter=0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==  1:
                    permiter+=4
                    if (i < len(grid) -1 and grid[i+1][j] == 1): permiter-=2
                    if (j < len(grid[0]) - 1 and grid[i][j+1] ==1 ): permiter-=2
        return permiter
        
# @lc code=end

