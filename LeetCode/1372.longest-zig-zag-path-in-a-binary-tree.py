#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest=0
        def dfs(node,curr,path):
            self.longest=max(self.longest,curr)
            if node.left:
                dfs(node.left,curr+1,"left") if path!="left" else dfs(node.left,1,"left")
            if node.right:
                dfs(node.right,curr+1,"right") if path!="right" else dfs(node.right,1,"right")
        dfs(root,0,"")
        return self.longest
# @lc code=end

