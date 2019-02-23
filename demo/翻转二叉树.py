#!@Author : Sanwat
#!@File : .py
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return root
        root.left, root.right = root.right, root.left
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
S=Solution()
T=TreeNode([2,3,4,5,6,7,8])
print(S.invertTree(T))