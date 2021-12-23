from bs4 import BeautifulSoup
from requests_html import HTMLSession, HTML
import urllib3
import time
import requests
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111'
}  # edge浏览器

url='https://www.xeacg520.com/shaonv/2021/0601/v8148.html'
t1=time.time()
http=HTMLSession()
d=http.get(url)
html=HTML(html=d.text)
print(html.links)
print(time.time()-t1)

# t2=time.time()
# strhtml = requests.get(url, "lxml")
# strhtml.headers = headers1
# soup = BeautifulSoup(strhtml.text, "lxml")
# strhtml.close()
# print(soup)
# print(time.time()-t2)

# t3=time.time()
# http=urllib3.PoolManager()
# d=http.request('GET',url)
# data=d.data.decode('UTF-8')
# print(data)
# print(time.time()-t3)