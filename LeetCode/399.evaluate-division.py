#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=collections.defaultdict(dict)
        for (x,y),value in zip(equations,values):
            graph[x][y]=value
            graph[y][x]=1/value
        def dfs(x,y,visited):
            if x not in graph and y not in graph: return -1
            if y in graph[x]: return graph[x][y]
            for i in graph[x]:
                if i in visited:
                    continue
                visited.add(i)
                temp = dfs(i,y,visited)
                if temp == -1: continue
                else: return graph[x][i] * temp
            return -1          
        output=[]
        for x,y in queries:
            visited=set()
            output.append(dfs(x,y,visited))
        return output

# @lc code=end

