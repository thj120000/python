#!@Author : Sanwat
#!@File : .py
'''
#Definition for a Node.
class Node(object):
    def __int__(self, val, children):
        self.val= val
        self.children= children

'''

class Solution (object):
    def maxDepth(self,root):
        """
        :param root: Node
        :return: int
        """
        if root is None:
            return 0
        if not root.children :
            return 1
        return 1+max(self.maxDepth(i) for i in root.children)
       #return 1+max(list(map(self.maxDepth, root.children)))