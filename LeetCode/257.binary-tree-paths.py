#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        def dfs(node,path,l):
            if not node.right and not node.left:
                l.append(path+str(node.val))
            if (node.left):
                dfs(node.left, path + str(node.val) + "->",l)
            if (node.right):
                dfs(node.right, path + str(node.val) + "->",l)
        l=[]
        dfs(root,"",l)
        return l
# @lc code=end

