#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    count=0
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        isConnected=matToAdj(isConnected)
        n = len(isConnected)
        print(isConnected)
        visited=set()
        for i in range(n):
            if i not in visited:
                self.count+=1
                self.dfs(i,isConnected,visited)
        return self.count

                    
    def dfs(self,node,isConnected,visited):      
        print(node)
        if node == len(isConnected):
            return
        visited.add(node)
        for nei in isConnected[node]:
            if nei not in visited:
                self.dfs(nei,isConnected,visited)
    
    
def matToAdj(mat):
    adj = []   
    V = len(mat)
    for i in range(V):
        row = []
        for j in range(V):
            if mat[i][j] == 1:
                row.append(j)
        adj.append(row)
    return adj

# @lc code=end

