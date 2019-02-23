#!@Author : Sanwat
#!@File : .py
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        keyset=['qwertyuiop','asdfghjkl','zxcvbnm']
        for keys in keyset:
            for word in words:
                line=set(word.lower())
                if line.issubset(set(keys)):
                    res.append(word.lower())
        return res
S=Solution()
print(S.findWords(['ADSA','WQERQWW','TVTDR']))
