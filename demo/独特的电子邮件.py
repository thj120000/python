#!@Author : Sanwat
#!@File : .py
class Solution:
    def numUniqueEmails(self,emails):
        '''
        :param emails:
        :return:
        '''
        rawemails = set()
        for email in emails:
            temp = email.split('@')
            first = temp[0].split('+')
            rawemails.add(first[0].replace('.','')+temp[1])
        return len(rawemails)
mail = Solution
print(mail.numUniqueEmails(''))