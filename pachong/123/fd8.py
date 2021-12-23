
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
categories = ['hello8']
context = ssl._create_unverified_context()


def daxiao(u):
    re = requests.get(u, stream=True, headers=headers).content
    image_b = io.BytesIO(re).read()
    size = len(image_b)
    return "{} Mb".format(size / 1e6)
yeshu1 =0
def ji_ye_shu(wed2):
    strhtml = requests.get(wed2, "lxml")
    strhtml.headers = headers1
    soup = BeautifulSoup(strhtml.text, "lxml")
    strhtml.close()

    data = soup.select('#main > div:nth-child(2) > div.showpage > a:nth-child(1)')
    for item in data:
        rts1 = {
            'title': item.get_text(),
        }

        rte = str(rts1.get('title'))
        zong = int(re.sub("\D", "", rte))
        global yeshu1
        yeshu1 = zong+1
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
    for i in range(int(shu0), int(shu0)+ji_ye_shu(wed1)):

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
def zhengchang(wedq_list1, add):
    for zai in wedq_list1:
        try:
            with open(add + '/%s' % (zai.strip().split('/')[-1]), 'r') as er:
                print("已存在,跳过")
                er.close()
                time.sleep(0.1)
                continue
        except FileNotFoundError:
            try:
                start = time.time()
                size = 0
                path = add + '/%s' % (zai.strip().split('/')[-1])  # 路径
                response = requests.get(zai,
                                        stream=True)  # stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
                chunk_size = 1024  # 每次块大小为1024
                content_size = int(response.headers['content-length'])  # 返回的response的headers中获取文件大小信息
                print("文件%s/%d大小：" % (zai.strip().split('/')[-1], yeshu1) + str(
                    round(float(content_size / chunk_size / 1024), 4)) + "[MB]")
                with open(path, 'wb') as file:
                    for data in response.iter_content(chunk_size=chunk_size):  # 每次只获取一个chunk_size大小
                        file.write(data)  # 每次只写入data大小
                        size = len(data) + size
                        # 'r'每次重新从开始输出，end = ""是不换行
                        print('\r' + "已经下载：" + int(size / content_size * 100) * ">" + " 【" + str(
                            round(size / chunk_size / 1024, 2)) + "MB】" + "【" + str(
                            round(float(size / content_size) * 100, 2)) + "%" + "】", end="")
                end = time.time()
                print("总耗时:" + str(end - start) + "秒")
            except KeyError:
                print("当前下载文件不存在")
                continue


def yichang(wedq_list2, sdd):
    for zai in wedq_list2:
        try:
            with open(sdd + '/%s' % (zai.strip().split('/')[-1]), 'r') as er:
                print("已存在,跳过")
                er.close()
                time.sleep(0.1)
                continue
        except FileNotFoundError:
            start = time.time()
            size = 0
            path = sdd + '/%s' % (zai.strip().split('/')[-1])  # 路径
            response = requests.get(zai,
                                    stream=True)  # stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
            chunk_size = 1024  # 每次块大小为1024
            content_size = int(response.headers['content-length'])  # 返回的response的headers中获取文件大小信息
            print("文件大小：" + str(round(float(content_size / chunk_size / 1024), 4)) + "[MB]")
            with open(path, 'wb') as file:
                for data in response.iter_content(chunk_size=chunk_size):  # 每次只获取一个chunk_size大小
                    file.write(data)  # 每次只写入data大小
                    size = len(data) + size
                    # 'r'每次重新从开始输出，end = ""是不换行
                    print('\r' + "已经下载：" + int(size / content_size * 100) * "█" + " 【" + str(
                        round(size / chunk_size / 1024, 2)) + "MB】" + "【" + str(
                        round(float(size / content_size) * 100, 2)) + "%" + "】", end="")
            end = time.time()
            print("总耗时:" + str(end - start) + "秒")


def ma():
    for sort in categories:

        with open('%s.txt' % sort, 'r') as file:#读取文件内容到内存
            urls = file.readlines()#计数行数
            file.close()#关闭文件
            for shu, wed1 in enumerate(urls):#逐行遍历数据
                pa = re.compile('h.+l')  # 生成正则表达式
                wed1 = pa.findall(str(wed1))
                strhtml = requests.get(wed1[0], 'lxml',headers=headers)
                strhtml.encoding='gbk2312'

                soup = BeautifulSoup(strhtml.text, "lxml")
                data = soup.select('#imgString > img')

                for item in data:
                    result = {
                        'src': item.get('src'),


                        'title': item.get('alt')
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
                    lian_jie_he_cheng(pian1, pian2, ce, wedq_list, shu0, wed1[0], tu)  # 计算合成图片链接
                    print(wedq_list)
                    add = ('D:/pycharm project/xiazai/' + str(r))
                    sdd = 'D:/pycharm project/xiazai/00'

                    try:
                        mkdir(add)
                        zhengchang(wedq_list, add)
                        strhtml.close()

                        print(wed1)
                        print("结束")
                        with open('%s.txt' % categories[0], 'r') as file1:
                            urls = file1.readlines()  # 计数行数
                            file1.close()  # 关闭文件
                        with open('%s.txt' % categories[0], 'w+') as file2:
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

