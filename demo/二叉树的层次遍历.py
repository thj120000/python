#!@Author : Sanwat
#!@File : .py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            stack=[root]
            res =[]
            while len(stack) !=0:
                tmp=[]
                res_each=[]
                for i in stack:
                    res_each.append(i.val)
                    if i.left !=None:
                        tmp.append(i.left)
                    if i.right !=None:
                        tmp.append(i.right)
                stack=tmp
                res.insert(0,res_each)
            return res