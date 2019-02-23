#!@Author : Sanwat
#!@File : .py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        ret = []
        for leaf in root.children:
            ret += (self.postorder(leaf))
        ret.append(root.val)
        return ret
