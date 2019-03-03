#!@Author : Sanwat
#!@File : .py
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=bin (x)
        b=bin (y)
        print(a)
        print(b)
        return bin(x^y).count('1')
SO= Solution()
print(SO.hammingDistance(1,4))