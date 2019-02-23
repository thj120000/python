#!@Author : Sanwat
#!@File : .py

class student:
    def __init__(self,name):
        self.name = name

class Zhanglaoshi :
    def __init__(self,num,lt):
        self.num=num
        self.lt = lt

    def add(self,student):
        self.lt.append(student)
    def remove(self,student):
        self.lt.remove(student)
  #  def dayin(self,student):
   #     return self.name

    def see(self):
        print("Zhaolaoshi的学生：")
        for i in range (len(self.lt)):
           print("姓名：",self.lt[i].name)

xuesheng1 = student ("唐化江")
xuehseng2 = student("雷鹏宇")
xuesheng3 = student("占俊坚")
xuesheng4 = student("郭子涵")
test = Zhanglaoshi(9301,[])
test.add(xuesheng1)
test.add(xuehseng2)
test.add(xuesheng3)
test.add(xuesheng4)

test.see()
#test.dayin()