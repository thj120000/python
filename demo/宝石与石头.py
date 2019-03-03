#!@Author : Sanwat
#!@File : .py
class Solution:
    def numJewelsInStones(self, J, S):
        """
        方法一：
        a = 0
        for i in J:
            for j in S:
                if i == j:
                    a= a+1
        return a
        方法二：
        """
        sum = 0;
        for i in J:
            sum+=S.count(i)
        return sum
SOL= Solution()
print (SOL.numJewelsInStones('ew','fwoowei'))





