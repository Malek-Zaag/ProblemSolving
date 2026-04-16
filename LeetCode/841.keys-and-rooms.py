#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
import numpy


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[0]
        visited=[False] * len(rooms)
        visited[0]=True
        while stack:
            node=stack.pop()
            for nei in rooms[node]:
                if visited[nei]== False:
                    visited[nei]=True
                    stack.append(nei)
        return all(visited)
        
        
# @lc code=end

