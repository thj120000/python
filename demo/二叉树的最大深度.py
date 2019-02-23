#!@Author : Sanwat
#!@File : .py
import math
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            l_deep = self.maxDepth(root.left)
            r_deep = self.maxDepth(root.right)
        return max(l_deep, r_deep) + 1
S=Solution()
print(S.maxDepth([3,9,20,null,null,15,7]))