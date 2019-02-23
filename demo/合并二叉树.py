#!@Author : Sanwat
#!@File : .py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        elif t1 is None and t2 is not None:
            t1 = t2
        return t1
S=Solution()
a=TreeNode([2,3,4,5,6,7,8])
b=TreeNode([2,4,3,2,5,1,2])
print(S.mergeTrees(a,b))