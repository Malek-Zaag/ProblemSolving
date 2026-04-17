#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neis={city: [] for city in range(n) }
        for a,b in connections:
            neis[a].append(b)
            neis[b].append(a)
        edges={(a,b) for a,b in connections}
        visited=set()
        visited.add(0)
        reverse=0
        
        def dfs(city): 
            nonlocal reverse,edges,neis
            for nei in neis[city]:
                if nei in visited:
                    continue
                if (nei,city) not in edges:
                    reverse+=1
                visited.add(nei)
                dfs(nei)
        dfs(0)
        return reverse
        
        

        
# @lc code=end

