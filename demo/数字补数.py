#!@Author : Sanwat
#!@File : .py
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        方法一
        a=bin (num)[2:]
        b='1'*len(a)
        c=int (b,2)
        result= c^num
        return result
        方法二：
        """
        a=bin (num)[2:]
        b=''
        for i in a:
            if(i=='1'):
                b+='0'
            else:
                b+='1'
        result = int (b,2)
        return result
S=Solution()
print(S.findComplement(39))