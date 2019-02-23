#!@Author : Sanwat
#!@File : .py
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            j=i+1
            if A[j]>A[i]:
                i=i+1
            else:
                break
        return i
S=Solution()
print(S.peakIndexInMountainArray([0,1,2,3,4,3]))