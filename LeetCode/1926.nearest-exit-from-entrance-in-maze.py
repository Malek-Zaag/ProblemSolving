#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue= deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        
        while queue:
            row, col, distance = queue.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < rows and 0<= nc < cols and maze[nr][nc] == ".":
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return distance + 1
                    maze[nr][nc] = "+"
                    queue.append((nr, nc, distance + 1))
        return -1
        
        
# @lc code=end

