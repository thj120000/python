#!@Author : Sanwat
#!@File : .py



class Solution (object):
    def transpose(self,A):
        '''
        :param A:list[list[int]]
        :return: list[list[int]]
        '''
        #方案一：
        return list (map (list, zip(*A)))
        #方案二：
        B=[[0 for i in range(len(A))] for i in range (len(A[0]))]
        for i in range (len(A)):
            for j in range (len(A[i])):
                B[j][i]=A[i][j]
        return B
S=Solution()
print(S.transpose([[1,2,3],[4,5,6],[7,8,9]]))