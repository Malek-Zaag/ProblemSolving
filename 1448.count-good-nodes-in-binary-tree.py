#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right : return root.val
        return 1+ self.dfs(root.left,root.val) + self.dfs(root.right,root.val)
    
    def dfs(self,node,curr_max):
        if not node : return 0
        if node.val >= curr_max: 
            return 1+ self.dfs(node.left,node.val) + self.dfs(node.right,node.val)
        else : return self.dfs(node.left,curr_max) + self.dfs(node.right,curr_max)

        # @lc code=end

