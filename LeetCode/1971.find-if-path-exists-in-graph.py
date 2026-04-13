#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start

from asyncio import graph
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        
        
        def dfs(node,visited):
            if (node == destination):
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor,visited):
                        return True
            return False      
        visited=set()
        return dfs(source,visited)  
# @lc code=end

