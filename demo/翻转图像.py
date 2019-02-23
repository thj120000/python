#!@Author : Sanwat
#!@File : .py
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range (len(A)):
            for j in range (len(A[0])):
                '''
                A[i][j]=1- int(A[i][j])
                '''
                A[i][j]=A[i][j]^1
            A[i]=A[i][::-1]
        return A

SOL = Solution()
print(SOL.flipAndInvertImage([[1,0,0],[1,1,0],[1,1,1]]))


