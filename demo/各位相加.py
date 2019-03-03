#!@Author : Sanwat
#!@File : .py
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (num>10):
            s = str(num)
            num=0
            for i in s:
                num+=int(i)
        return num
S=Solution()
print(S.addDigits(78))