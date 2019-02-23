#!@Author : Sanwat
#!@File : .py

def countchar(strr):
    strr=strr.lower()
    result=[]
    letter='abcdefghijklmnopqrstuvwxyz'
    for i in range(0,26):
        curcount=0
        for j in range(0,len(strr)):
            if letter[i]==strr[j]:
                curcount+=1
        result.append(curcount)
    return result
if __name__ == "__main__":
    strr = input()
    print(countchar(strr))