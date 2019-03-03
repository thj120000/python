#!@Author : Sanwat
#!@File : .py
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        方法一
        M = []
        N = []
        for i in range(len(A)):
            if A[i] % 2 == 1:
                M.append(A[i])
            else:
                N.append(A[i])
        res = []
        for i in range(len(A)):
            if i % 2 == 0:
                res.append(N[i // 2])
            else:
                res.append(M[i // 2])
        return res
        方法二
        """
        A_len, i, j = len(A), 0, 1
        result = [0] * A_len
        for a in A:
            if a & 1 == 0:
                result[i] = a
                i += 2
            else:
                result[j] = a
                j += 2

        return result
S=Solution()
print(S.sortArrayByParityII([2,4,7,5]))