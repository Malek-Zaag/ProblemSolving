#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2 : return False
        li1,li2=[], []
        self.getLeafValues(root1,li1)
        self.getLeafValues(root2,li2)
        if len(li1) != len(li2) : return False
        for i,j in zip(li1,li2):
            if i != j: return False
        return True

    def getLeafValues(self,root,li):
        if not root : return
        if not root.left and not root.right : li.append(root.val)
        self.getLeafValues(root.left,li)
        self.getLeafValues(root.right,li)
# @lc code=end

