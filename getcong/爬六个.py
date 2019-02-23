#!@Author : Sanwat
#!@File : .py

import requests
import json
import urllib

n = 0
m = 0
def getSogouImag(length,path):
    global m
    n = length
    #requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='
    #            +cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    imgs = requests.get('http://pic.sogou.com/pics?query=%CB%AE%C4%AB%BB%AD&mode=1&start='+str(n)+'&reqType=ajax&tn=0&reqFrom=detail')
    jd = json.loads(imgs.text)
    jd = jd['items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['thumbUrl'])
    for img_url in imgs_url:
            print('No.'+str(m)+'.jpg '+' is  Downloading...')
            urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            m = m + 1
while n < 20:
    getSogouImag(n,'C:\workspace\pachong\image-haizei/')
    n+=1
else:
    print('Download complete!')
