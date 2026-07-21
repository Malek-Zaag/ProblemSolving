#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        timer = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 1:
                        fresh-=1
                        grid[nr][nc] =2 
                        queue.append((nr,nc))
            timer += 1
        return timer if fresh == 0 else -1
    
    
sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

        
        
        
# @lc code=end

