#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix = [0]
        for value in arr:
            prefix.append(prefix[-1] ^ value)

        return [
            prefix[right + 1] ^ prefix[left]
            for left, right in queries
        ]
        
        
        
# @lc code=end


sol = Solution()
print(sol.xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))
print(sol.xorQueries([4,8,2,10],[[2,3],[1,3],[0,0],[0,3]]))