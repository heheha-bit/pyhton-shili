import io
import re
import sys
import urllib
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import time
import socket
import ssl
import os

from urllib3 import request

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}  # Chrome浏览器
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111'
}  # edge浏览器
wedq_list = []
categories = ['hello']
context = ssl._create_unverified_context()


def daxiao(u):
    re = requests.get(u, stream=True, headers=headers).content
    image_b = io.BytesIO(re).read()
    size = len(image_b)
    return "{} Mb".format(size / 1e6)

def re_py():
    pyt = sys.executable
    os.execl(pyt, pyt, *sys.argv)


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


def zhengchang(wedq_list1, add):
    for zai in wedq_list1:
        # conjishu = 1
        print(zai)
        dataq = time.time()

        print("开始")
        try:
            with open(add + '/%s' % (zai.strip().split('/')[-1]), 'r') as er:
                print("已存在,跳过")
                er.close()
                time.sleep(0.1)
                continue

        except FileNotFoundError:
            try:
                page1 = urllib.request.Request(zai, headers=headers1)
                kaishi = urllib.request.urlopen(page1, timeout=120, context=context)

                with open(add + '/%s' % (zai.strip().split('/')[-1]), 'wb') as f:

                    f.write(kaishi.read())

                    f.close()
                print("下载成功,大小为", daxiao(zai))

            except socket.timeout:
                print("超时下载开始")
                try:
                    page1 = urllib.request.Request(zai, headers=headers)
                    kaishi=urllib.request.urlopen(page1, timeout=120, context=context)

                    if kaishi.getcode() == 200:
                        with open(add + '/%s' % (zai.strip().split('/')[-1]), 'wb') as f:
                            f.write(kaishi.read())
                            f.close()
                        print("超时下载成功,大小为",  daxiao(zai))
                    else:
                        continue
                except socket.timeout:
                    print("超时")
                    continue
        time.sleep(1)
        dataw = time.time()
        print(dataw - dataq)


def yichang(wedq_list2, sdd):
    for zai in wedq_list2:

        print(zai)
        dataq = time.time()

        print("开始")
        try:
            with open(sdd + '/%s' % (zai.strip().split('/')[-1]), 'r') as er:
                print("已存在,跳过")
                time.sleep(0.1)
                er.close()
                continue
        except FileNotFoundError:
            try:
                page1 = urllib.request.Request(zai, headers=headers1)
                with open(sdd + '/%s' % (zai.strip().split('/')[-1]), 'wb') as f:
                    f.write(urllib.request.urlopen(page1, timeout=120, context=context).read())

                    f.close()

                print("下载成功,大小为", daxiao(zai))
            except socket.timeout:
                print("异常超时下载开始")
                try:
                    page1 = urllib.request.Request(zai, headers=headers)
                    with open(sdd + '/%s' % (zai.strip().split('/')[-1]), 'wb') as f:
                        f.write(urllib.request.urlopen(page1, timeout=120, context=context).read())
                        f.close()
                    print("异常超时下载成功,大小为", daxiao(zai))

                except socket.timeout:
                    print("异常超时")
                    continue
        time.sleep(1)
        dataw = time.time()
        print(dataw - dataq)


def ji_ye_shu(wed2):
    strhtml = requests.get(wed2, "lxml")
    strhtml.headers = headers1
    # urllib.request.Request(wed2, headers=headers)
    soup = BeautifulSoup(strhtml.text, "lxml")
    strhtml.close()

    data = soup.select('#mh_content > div:nth-child(1) > div > ul > li:nth-child(1) > a')
    for item in data:
        rts1 = {
            'title': item.get_text(),
        }

        rte = str(rts1.get('title'))
        zong = int(re.sub("\D", "", rte))
        return zong+1


def bian_yi_lian_jie_he_cheng(p1, p2, c, w, shu0, wed1,ti):
    w.clear()
    for i in range(7, ji_ye_shu(wed1)):

        if ti[-5] == shu0[len(shu0)-1]:
            if shu0[0] == '0':
                if i >= 10 and i < 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - 2]) + str(i) + p2)


                elif i >= 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))]) + str(i) + p2)


                else:
                    zui = str(p1 + c + str(shu0[0:len(shu0) - 1]) + str(i) + p2)


            else:
                zui = str(p1 + c + str(i) + p2)
        else:

            if shu0[0] == '0':
                if i >= 10 and i < 100:

                    zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)


                elif i >= 100:

                    zui = str(p1 +str(shu0[0:len(shu0) - len(str(i))]+ str(i)) + c + p2)


                else:
                    zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)


            else:
                zui = str(p1 + c + str(i) + p2)

        w.append(zui)
        print("--------------------------------------->", i, "<---------------------------------------------")


def lian_jie_he_cheng(p1, p2, c, w, shu0, wed1,ti):
    w.clear()
    for i in range(2, ji_ye_shu(wed1)):

        if ti[-5] == shu0[len(shu0)-1]:
            if shu0[0] == '0':
                if i >= 10 and i < 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - 2]) + str(i) + p2)


                elif i >= 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))-1]) + str(i) + p2)



                else:
                    zui = str(p1 + c + str(shu0[0:len(shu0) - 1]) + str(i) + p2)


            else:
                zui = str(p1 + c + str(i) + p2)
        else:

            if shu0[0] == '0':
                if i >= 10 and i < 100:

                    zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)


                elif i >= 100:

                    zui = str(p1 +str(shu0[0:len(shu0) - len(str(i))]+ str(i)) + c + p2)


                else:
                    zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)


            else:
                zui = str(p1 + c + str(i) + p2)

        w.append(zui)
        print("--------------------------------------->", i, "<---------------------------------------------")

def ma():
    for category in categories:
        with open('%s.txt' % category, 'r') as file:
            urls = file.readlines()
            file.close()
            # 计算URL地址条数
            n_urls = len(urls)
            # 遍历链接地址下载图片
            for shu, wed1 in enumerate(urls):
                print(wed1)
                strhtml = requests.get(wed1, 'lxml',headers = headers1)

                soup = BeautifulSoup(strhtml.text, "lxml")
                data = soup.select('#imgshow > img')
                for item in data:
                    result = {
                        'title': item.get('alt'),
                        'src': item.get('src')
                    }
                r = str(result.get('title'))
                tu = str(result.get('src'))
                print(r[len(r) - 1])
                if r[len(r) - 1] == "?" or r[len(r) - 1] == "/" or r[len(r) - 1] == "':'" or r[len(r) - 1] == "'*'" or \
                        r[len(r) - 1] == "'<'" or r[len(r) - 1] == "'>'" or r[len(r) - 1] == "'|'":
                    r = r[0:len(r) - 2]
                for t in range(len(tu) - 1, -1, -1):  # 链接切片位置计算
                    if tu[t] == '.':
                        endflag = t
                    if tu[t] == '/':
                        staflag = t + 1
                        break
                pian1 = tu[0:staflag]
                z = tu[staflag:endflag]
                pian2 = tu[endflag:len(tu)]
                shu0 = str(re.sub("\D", "", tu[staflag:endflag]))
                ce = str(z.replace(shu0, ""))
                lian_jie_he_cheng(pian1, pian2, ce, wedq_list, shu0, wed1,tu)  # 计算合成图片链接
                #bian_yi_lian_jie_he_cheng(pian1, pian2, ce, wedq_list, shu0, wed1,tu)  # 变异计算合成图片链接

                print(wedq_list)
                add = ('D:/pycharm project/py_pic/' + str(r))
                sdd = 'D:/pycharm project/py_pic/00'

                try:
                    mkdir(add)
                    zhengchang(wedq_list, add)
                    strhtml.close()
                    print(wed1)
                    print("结束")

                except NotADirectoryError:  # 非法文件名
                    print("非法文件名")
                    yichang(wedq_list, sdd)
                    wedq_list.clear()
                    strhtml.close()
                    print(wed1)
                    print("结束")

                except OSError:  # 错误文件名
                    print("错误文件名")
                    print(wed1)
                    print("结束")
                    print("重启")
                    # sys.exit()
                    ma()
                except urllib.error.URLError:  # 链接断开
                    print("链接异常")
                    print(wed1)


ma()
