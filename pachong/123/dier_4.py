
import io
import socket
import time
import urllib

import requests
import ssl
import os
import re
from bs4 import BeautifulSoup

headers = {

    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}  # Chrome浏览器
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
}  # edge浏览器
wedq_list = []
categories = ['duoxian4']
context = ssl._create_unverified_context()


def daxiao(u):
    re = requests.get(u, stream=True, headers=headers).content
    image_b = io.BytesIO(re).read()
    size = len(image_b)
    return "{} Mb".format(size / 1e6)
yeshu=0
def ji_ye_shu(wed2):
    strhtml = requests.get(wed2, "lxml")
    strhtml.headers = headers1
    # urllib.request.Request(wed2, headers=headers)
    soup = BeautifulSoup(strhtml.text, "lxml")
    strhtml.close()

    data = soup.select('#LayoutDiv1 > div.mainbox > div.list-box > div.dede_pages_all > div.dede_pages > ul > li:nth-child(1) > a')
    for item in data:
        rts1 = {
            'title': item.get_text(),
        }

        rte = str(rts1.get('title'))
        zong = int(re.sub("\D", "", rte))
        global yeshu
        yeshu=zong+1
        return zong+1

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

def lian_jie_he_cheng(p1, p2, c, w, shu0, wed1,ti):
    w.clear()
    for i in range(1, ji_ye_shu(wed1)):

        if ti[-5] == shu0[len(shu0)-1]:

            if shu0[0] == '0' and shu0[1]=='0':
                if i >= 10 and i < 100:

                    zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)


                elif i >= 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))]) + str(i) + p2)


                else:
                    zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)
            elif shu0[0] == '0':
                if i >= 10 and i < 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - 2]) + str(i) + p2)


                elif i >= 100:

                    zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))-1]) + str(i) + p2)



                else:
                    zui = str(p1 + c + str(shu0[0:len(shu0) - 1]) + str(i) + p2)
            else:
                zui = str(p1 + c + str(i) + p2)
        else:
            if shu0[0] == '0' and shu0[1]=='0':
                if i >= 10 and i < 100:

                    zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)


                elif i >= 100:

                    zui = str(p1 +str(shu0[0:len(shu0) - len(str(i))]+ str(i)) + c + p2)


                else:
                    zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)
            elif shu0[0] == '0':
                if i >= 10 and i < 100:

                    zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)


                elif i >= 100:

                    zui = str(p1 +str(shu0[0:len(shu0) - len(str(i))-1]+ str(i)) + c + p2)


                else:
                    zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)
            else:
                zui = str(p1 + c + str(i) + p2)

        w.append(zui)
        print("--------------------------------------->", i, "<---------------------------------------------")


def zhengchang(wedq_list1, add):

    for zai in wedq_list1:
        path=add + '/%s' % (zai.strip().split('/')[-1])
        path_error=add + '/%s' % (zai.strip().split('/')[-1])
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
                kaishi = urllib.request.urlopen(page1, timeout=10, context=context)

                with open(path, 'wb') as f:
                    f.write(kaishi.read())

                    f.close()
                print("下载成功%s/%d张"% (zai.strip().split('/')[-1],yeshu))
            except OSError:  # 错误文件名
                print("错误文件名")
                with open(path_error, 'wb') as f:
                    f.close()
                continue
            except socket.timeout:
                print("超时下载开始")
                try:
                    page1 = urllib.request.Request(zai, headers=headers)
                    kaishi=urllib.request.urlopen(page1, timeout=10, context=context)

                    if kaishi.getcode() == 200:
                        with open(add + '/%s' % (zai.strip().split('/')[-1]), 'wb') as f:
                            f.write(kaishi.read())
                            f.close()
                        print("超时下载成功%s/%d"% (zai.strip().split('/')[-1],yeshu))
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
        path=sdd + '/%s' % (zai.strip().split('/')[-1])
        path_error=sdd + '/%s' % (zai.strip().split('/')[-1])
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
                with open(path, 'wb') as f:
                    f.write(urllib.request.urlopen(page1, timeout=10, context=context).read())

                    f.close()

                print("下载成功%s/%d"% (zai.strip().split('/')[-1],yeshu))
            except OSError:  # 错误文件名
                print("错误文件名")
                with open(path_error, 'wb') as f:
                    f.close()
                continue
            except socket.timeout:
                print("异常超时下载开始")
                try:
                    page1 = urllib.request.Request(zai, headers=headers)
                    with open(sdd + '/%s' % (zai.strip().split('/')[-1]), 'wb') as f:
                        f.write(urllib.request.urlopen(page1, timeout=10, context=context).read())
                        f.close()
                    print("异常超时下载成功%s/%d"% (zai.strip().split('/')[-1],yeshu))

                except socket.timeout:
                    print("异常超时")
                    continue
        time.sleep(1)
        dataw = time.time()
        print(dataw - dataq)
def ma():
    for sort in categories:

        with open('%s.txt' % sort, 'r') as file:#读取文件内容到内存
            urls = file.readlines()#计数行数
            file.close()#关闭文件
            for shu, wed1 in enumerate(urls):#逐行遍历数据
                pa = re.compile('h.+l')  # 生成正则表达式
                wed1 = pa.findall(str(wed1))
                strhtml = requests.get(wed1[0], 'lxml',headers=headers)

                strhtml.encoding = 'gbk2312'
                soup = BeautifulSoup(strhtml.text, "lxml")
                data = soup.select('#LayoutDiv1 > div.mainbox > div.list-box > div.pic > img')
                data_title = soup.select('#LayoutDiv1 > div.mainbox > div.wz-title')
                for item in data:
                    result = {
                        'src': item.get('src')

                    }
                    pattern =re.compile('>(.+)<')#生成正则表达式
                    r = pattern.findall(str(data_title))#使用正则表达式
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
                    lian_jie_he_cheng(pian1, pian2, ce, wedq_list, shu0, wed1[0], tu)  # 计算合成图片链接
                    print(wedq_list)
                    add = ('D:/pycharm project/xiazai/' + str(r[0]))
                    sdd = 'D:/pycharm project/xiazai/00'

                    try:
                        mkdir(add)
                        zhengchang(wedq_list, add)
                        strhtml.close()
                        print(wed1)
                        print("结束")
                        with open('%s.txt' % sort, 'r') as file1:
                            urls = file1.readlines()  # 计数行数
                            file1.close()  # 关闭文件
                        with open('%s.txt' % sort, 'w+') as file2:
                            for i in range(1, len(urls)):
                                file2.write(urls[i])
                            file2.close()  # 关闭文件

                    except NotADirectoryError:  # 非法文件名
                        print("非法文件名")
                        yichang(wedq_list, sdd)
                        wedq_list.clear()
                        strhtml.close()
                        print(wed1)
                        print("结束")


                    except urllib.error.URLError:  # 链接断开
                        print("链接异常")
                        print(wed1)







if __name__ == '__main__':
    ma()

