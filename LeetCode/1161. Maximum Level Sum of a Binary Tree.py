# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return None
        if root.right == None and root.right== None:
            return 1
        m,curr,idx,m_idx=root.val,root.val,1,1
        q=[]
        q.append(root)
        while (q):
            print(q[0].val)
            curr=0
            for i in range(len(q)):         
                node = q.pop(0)
                curr+=node.val
                if (node.left != None): q.append(node.left)
                if (node.right != None): q.append(node.right)     
            if curr > m:
                m=curr
                m_idx=idx
            idx+=1
        return m_idx
