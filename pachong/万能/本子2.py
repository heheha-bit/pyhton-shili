import io
import string

from bs4 import BeautifulSoup
import requests
import re
import os
import time
from urllib.request import urlretrieve
import socket
import urllib
import ssl
from urllib.parse import quote
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}  # Chrome浏览器
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111'
}  # edge浏览器

def mkdir(path):
    path = path.strip()

    path = path.rstrip("\\")

    isExists = os.path.exists(path)

    if not isExists:
        print(path + ' 创建成功')
        os.makedirs(path)
        return True
    else:

        print(path + ' 目录已存在')
        return False

def get_url(url):
    weblist = []
    weblist.append(url)
    strhtml = requests.get(url, "lxml")
    strhtml.headers = headers1
    soup = BeautifulSoup(strhtml.text, "lxml")
    strhtml.close()
    data = soup.select('#mh_content > div:nth-child(1) > div > ul > li:nth-child(1) > a')
    for item in data:
        rts1 = {
            'title': item.get_text(),
        }
        rte = str(rts1.get('title'))
        yeshu1 = int(re.sub("\D", "", rte))
    ye = re.search(".html", url).span()[0]
    print("当前文件有" + str(yeshu1) + "页")
    for i in range(2, yeshu1):
        url1 = url[0:ye] + '_' + str(i) + ".html"
        weblist.append(url1)
    return weblist

def get_src(weblist):

    srclist=[]

    for url in weblist:
        strhtml = requests.get(url, "lxml")
        strhtml.headers = headers1
        soup = BeautifulSoup(strhtml.text, "lxml")
        strhtml.close()
        data = soup.select('#imgshow > img')
        for item in data:
            rt = {
               'src': item.get('src'),
               'alt': item.get('alt'),
            }
        srcdit = {'src': "", 'alt': ""}
        srcdit['src']=str(rt.get('src'))
        srcdit['alt']=str(rt.get('alt'))
        srclist.append(srcdit)
    return srclist

def daxiao(u):
    re = requests.get(u, stream=True, headers=headers).content
    image_b = io.BytesIO(re).read()
    size = len(image_b)
    return "{} Mb".format(size / 1e6)

def zhengchang(wedq_list1, add):
    for zai in wedq_list1:
        print(zai['src'])
        dataq = time.time()

        print("开始")
        try:
            if daxiao(zai['src']) == 0:
                raise Exception("FileNotFoundError")
            with open(add + '/%s' % (zai['src'].strip().split('/')[-1]), 'r') as er:
                print("已存在,跳过")
                er.close()
                time.sleep(0.1)
                continue

        except FileNotFoundError:
            try:
                s = quote(zai['src'], safe=string.printable)

                page1 = urllib.request.Request(s, headers=headers1)
                kaishi = urllib.request.urlopen(page1, timeout=120, context=context)

                with open(add + '/%s' % (zai['src'].strip().split('/')[-1]), 'wb') as f:

                    f.write(kaishi.read())

                    f.close()
                print("下载成功,大小为", daxiao(zai['src']))

            except socket.timeout:
                print("超时下载开始")
                try:
                    page1 = urllib.request.Request(zai['src'], headers=headers)
                    kaishi=urllib.request.urlopen(page1, timeout=120, context=context)

                    if kaishi.getcode() == 200:
                        with open(add + '/%s' % (zai['src'].strip().split('/')[-1]), 'wb') as f:
                            f.write(kaishi.read())
                            f.close()
                        print("超时下载成功,大小为",  daxiao(zai['src']))
                    else:
                        continue
                except socket.timeout:
                    print("超时")
                    continue
            except UnicodeEncodeError:
                s=quote(zai['src'],safe=string.printable)
                page1 = urllib.request.Request(s, headers=headers1)
                kaishi = urllib.request.urlopen(page1, timeout=120, context=context)

                with open(add + '/%s' % (zai['src'].strip().split('/')[-1]), 'wb') as f:

                    f.write(kaishi.read())

                    f.close()
                print("下载成功,大小为", daxiao(s))
            except urllib.error.HTTPError:
                continue

        dataw = time.time()
        print(dataw - dataq)


def 读链接():
    for category in categories:
        with open('%s.txt' % category, 'r') as file:
            urls = file.readlines()
            file.close()
            return urls


def mai(url):
    weblist = get_url(url)
    srclist = get_src(weblist)
    dire = srclist[0]['alt']
    t = re.sub('[+/:*?\"<>|\\\]', ' ', dire).replace(" ", "")
    mkdir(add + t)
    zhengchang(srclist, add + t)
    print(srclist)

def 跳过(url):
    with open('已下载.txt', 'r') as f:
        urls = f.readlines()
    f.close()
    for u in urls:
        if u==url:
            return False
    return True

if __name__ == '__main__':
    # www.xeacg520.com
    context = ssl._create_unverified_context()
    categories = ['hello2']
    alt=""
    add = ('D:/pycharm project/xiazai/')
    sdd = 'D:/pycharm project/xiazai/00'
    yeshu1=0
    for url in 读链接():
        print("加载中。。。。")
        with open('hello2.txt', 'r') as f:
            urls = f.readlines()
        f.close()
        if 跳过(url):
            print("加载中。。。。")
            mai(url)
        else:
            print("已存在跳过")
            continue
        with open('已下载.txt', 'a') as f1:
            f1.write(url)
        f1.close()
