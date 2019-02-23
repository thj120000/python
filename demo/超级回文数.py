#!@Author : Sanwat
#!@File : .py
import math
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: strF
        :rtype: int
        """
        s=0
        a=int (L)
        b=int (R)
        for i in range (a,b):
            if str (i)== str(i)[:: -1]:
                j=math.sqrt(i).real
                if (j%1==0):
                    k=int (j)
                    if str(k)==str(k)[:: -1]:
                        print("超级回文数：", k * k)
                        s=s+1
        return s

SOL = Solution()
print(SOL.superpalindromesInRange('4', '1000'))


'''
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        s1=0
        s2=0
        a= int  (L)
        b= int(R)
        print(a,b)
        for i in range (a,b):
            if str (i)== str(i)[:: -1]:
                s1 = s1 + 1
                j=(math.sqrt(i).real)
                if (j % 1) == 0:
                    k=int(j)
                    if str(k)==str(k)[:: -1]:
                        print("超级回文数：",k*k)
                        s2=s2+1
            else:
                continue
        return s2


s=0
                        
        a=int (math.sqrt(int (L)).real)
        b=int (math.sqrt(int (R)).real)
        for i in range (a,b+1):
            j=i*i
            if (str (i)== str(i)[:: -1]) & (str (j)== str(j)[:: -1]) :
                print(j)
                s=s+1
        return s
'''