#!@Author : Sanwat
#!@File : .py

import requests
import json
import urllib
#example_table > tbody > tr:nth-child(2) > td:nth-child(4) > a > img

def getSogouImag(category,length,path):
    n = length
    cate = category
    imgs = requests.get('https://pic.sogou.com/pics?query=%C3%C0%C5%AE&w=05009900&p=&_asf=pic.sogou.com&_ast=1540275417&sc=index&sut=2318&sst0=1540275417414'
                        +cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len=4'+str())
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['pic_url'])
    m = 0
    for img_url in imgs_url:
            print('***** '+str(m)+'.jpg *****'+'   Downloading...')
            urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            m = m + 1
    print('Download complete!')

getSogouImag('壁纸',2000,'C:/workspace/pachong/bizhi/')