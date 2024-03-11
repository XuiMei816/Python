#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :pa_text.py
# Author:PWJ
# Date  :2024/3/7
import requests,sys
from bs4 import BeautifulSoup
import time
#url = 'http://www.biqg.cc/book/4088/'

'''
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/105'}
url1='https://www.biqg.cc/book/4088/20.html'
r=requests.get(url=url1, headers=head)
#r.encoding ='GBK'
html=r.text
soup = BeautifulSoup(html,'html.parser')
#print(soup)
texts = soup.find_all('div',id="chaptercontent")#class_ ='Readarea ReadAjax_content'
#print(texts)
#print(type(texts)) #<class 'bs4.element.ResultSet'>
texts=texts[0].text.replace('\u3000','\n') #\xa0:半角（&nbsp);\u3000:全角
#texts=str(texts)
#texts=texts.split('\n')
print(texts)
with open('G:\Lun.txt', 'a', encoding='utf-8') as f:
    f.writelines(texts[0].text.replace('\n',''))
'''
url_s=list(range(3960))
for i in range(len(url_s)):
    url_s[i]='https://www.biqg.cc/book/4088/'+str(i)+'.html'
#print(url_s[1])
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/105'}
for i in range(1,20):
    url_n=url_s[i]
    r = requests.get(url=url_n, headers=head)
    r.encoding = 'GBK'
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.find_all('div', id="chaptercontent")
    with open('G:\Lun.txt', 'a', encoding='utf-8') as f:
        f.writelines(texts[0].text.replace('\n', ''))
    #print(texts[0].text.replace('\u3000','\n'))
    time.sleep( 10)

'''
target='https://www.biqg.cc/book/4088/'
req=requests.get(url=target)
html=req.text
div_bf=BeautifulSoup(html,'html.parser')
div=div_bf.find_all('div',class_ ='listmain')
print(div[0].text)
'''

'''server='https://www.biqg.cc/'
target='https://www.biqg.cc/book/4088/'
req=requests.get(url=target)
html=req.text
div_bf=BeautifulSoup(html,features='html.parser')
div=div_bf.find_all('div',class_ ='listmain')
a_bf=BeautifulSoup(str(div[0]),features='html.parser')
a=a_bf.find_all('a')
for each in a:
    print((each.string,server+each.get('href')))
'''
'''class downloader(object):
    def __init__(self):
        self.server='https://www.biqg.cc/'
        self.target='https://www.biqg.cc/book/4088/'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/105'}
        self.names=[]
        self.urls=[]
        self.nums=0

    def get_download_url(self):
        req = requests.get(url=self.target,headers=self.headers)
        html = req.text
        div_bf = BeautifulSoup(html, features='html.parser')
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]),features='html.parser')
        a = a_bf.find_all('a')
        self.nums=len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append('https://www.biqg.cc'+each.get('href'))

    def get_contents(self,url_1):
        req = requests.get(url=url_1, headers=self.headers)
        #req.encoding = 'GBK'
        html = req.text
        bf=BeautifulSoup(html, features='html.parser')
        texts=bf.find_all('div',class_ ='Readarea ReadAjax_content')
        texts=texts[0].text.replace('\r\n','')
        return texts

    def writer(self,name,path,text):
        write_flag=True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《轮回乐园》开始下载：')
    for i in range(dl.nums):
        g=dl.urls[i]
        dl.writer(name=dl.names[i],path='G:\Lun.txt',text=dl.get_contents(g))
    sys.stdout.write("已下载：%.3f%%" % float(i/dl.nums)+'\r')
    sys.stdout.flush()
    print('《轮回乐园》下载完成')
'''

























