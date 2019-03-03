#!@Author : Sanwat
#!@File : .py

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        list1=[]
        list2=[]
        for i in A:
            a= str(bin(i))
            if (a[-1]=='0'):
                list1.append(i)
            else:
                list2.append(i)
        return  list1+list2

SOL= Solution()
print (SOL.sortArrayByParity([2,3,4,5]))
