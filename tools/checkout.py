#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/6/18 17:05
# version: 0.1
import requests
from bs4 import BeautifulSoup
import json,sys,time,re,os

class download_mzt():
    def __init__(self):
        self.url_name='https://www.mzitu.com/'
        self.header={
            'Referer': 'https://www.mzitu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.title_list=[]

    # 获取首页所有连接的函数
    def get_list(self):
        rq=requests.get(url=self.url_name,headers=self.header)
        sp=BeautifulSoup(rq.text,'html.parser')
        text=sp.find_all('div',class_='postlist')[0].find_all('a',target='_blank')
        for i in text:
            title=i.get_text()
            url=i.get('href')
            if title :
                self.title_list.append({
                    'title':title,
                    'url':url
                })
        # for n in self.title_list:
        #     print(n)
    # 定义获取最大列表的函数
    def get_maxpage(self):
        for name in self.title_list:
            urls=name['url']
            rq = requests.get(url=urls, headers=self.header)
            sp = BeautifulSoup(rq.text, 'html.parser')
            text = sp.find_all('div', class_='pagenavi')[0].find_all('span')
            maxpag = text[-2].get_text()
            # print(maxpag)
            name['maxpag']=int(maxpag)
    # 获取套图的所有地址
    def get_ever_url(self,dic):
        print('下载:%s,\t 页数%s'%(dic['title'],dic['maxpag']))
        for i in range(1,dic['maxpag']):
            # print(i)
            page_url="%s/%s"%(dic['url'],i)
            rq=requests.get(url=page_url,headers=self.header)
            sp=BeautifulSoup(rq.text,'html.parser')
            text=sp.find_all('div',class_='main-image')[0].find_all('img')[0]
            pic_url=text.get('src')
            name=re.split('/',pic_url)[5]
            self.down_pic(pic_url,dic['title'],name)
            # print('\t\t下载第%s页,名字%s'%(i,name))
            # time.sleep(0.5)
            # print(pic_url,name)
            sys.stdout.write("\r")
            sys.stdout.write("%s%% | %s" %(int(i/dic['maxpag']*100),i*'|'))
            sys.stdout.flush()

    # 定义下载函数
    def down_pic(self,pic_url,title,name):
        if not os.path.exists(title):
            os.mkdir(title)
        rq=requests.get(url=pic_url,headers=self.header)
        with open("%s/%s"%(title,name),'wb') as f:
            f.write(rq.content)
            f.close()

if __name__=="__main__":
    dm=download_mzt()
    # dm.get_list()
    # dm.get_maxpage()

    # for dic in dm.title_list:
    #     print(dic)
    #     dm.get_ever_url(dic)
    dic={'title': 'test', 'url': 'https://www.mzitu.com/224623', 'maxpag': 78}
    dm.get_ever_url(dic)