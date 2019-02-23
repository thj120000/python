#!@Author : Sanwat
#!@File : .pyclass Solution:
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a=moves.count('U')
        b=moves.count ('D')
        c=moves.count ('L')
        d=moves.count('R')
        if (a==b)&(c==d):
            return  True
        else:
            return False
SOL = Solution()
print(SOL.judgeCircle('UDLRLRUD'))
