#!@Author : Sanwat
#!@File : .py
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        k=0
        for  i in range (left,right+1,1):
            a=str(i)
            if '0'  not in a:
                b=list(a)
                for j in b:
                    if i % int(j)!=0 :
                        break
                    else:
                        k=k+1
                        if (j==b[-1] ) &( k==len(b)):
                            res.append(i)
                k=0
        return res
S=Solution()
print(S.selfDividingNumbers(47,85))



