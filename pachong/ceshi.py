# import requests
# import time
#
#
# def downloadFile(name, url):
#     headers = {'Proxy-Connection': 'keep-alive'}
#     r = requests.get(url, stream=True, headers=headers)
#     length = float(r.headers['content-length'])
#     f = open(name, 'wb')
#     count = 0
#     count_tmp = 0
#     time1 = time.time()
#     for chunk in r.iter_content(chunk_size=512):
#         if chunk:
#             f.write(chunk)
#             count += len(chunk)
#             if time.time() - time1 > 2:
#                 p = count / length * 100
#                 speed = (count - count_tmp) / 1024 / 1024 / 2
#                 count_tmp = count
#                 print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
#                 time1 = time.time()
#     f.close()
#
#
# def formatFloat(num):
#     return '{:.2f}'.format(num)

# import requests#引入requests库
# import time#引入time，计算下载时间
# start = time.time()
# size = 0
# path = "D:/pycharm project/xiazai/1.exe"#路径
# url = "https://dldir1.qq.com/qqtv/TencentVideo10.14.3360.0.exe"
# response = requests.get(url,stream = True)#stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
# chunk_size = 1024#每次块大小为1024
# content_size = int(response.headers['content-length'])#返回的response的headers中获取文件大小信息
# print("文件大小："+str(round(float(content_size/chunk_size/1024),4))+"[MB]")
# with open(path,'wb') as file:
#     for data in response.iter_content(chunk_size=chunk_size):#每次只获取一个chunk_size大小
#         file.write(data)#每次只写入data大小
#         size = len(data)+size
#         #'r'每次重新从开始输出，end = ""是不换行
#         print('\r'+"已经下载："+int(size/content_size*100)*"█"+" 【"+str(round(size/chunk_size/1024,2))+"MB】"+"【"+str(round(float(size/content_size)*100,2))+"%"+"】",end="")
# end = time.time()
# print("总耗时:"+str(end-start)+"秒")
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
categories = ['hello3']
context = ssl._create_unverified_context()


def daxiao(u):
    re = requests.get(u, stream=True, headers=headers).content
    image_b = io.BytesIO(re).read()
    size = len(image_b)
    return "{} Mb".format(size / 1e6)

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
# def zhengchang(wedq_list1, add):
#     for zai in wedq_list1:
#         try:
#             with open(add + '/%s' % (zai.strip().split('/')[-1]), 'r') as er:
#                 print("已存在,跳过")
#                 er.close()
#                 time.sleep(0.1)
#                 continue
#         except FileNotFoundError:
#             start = time.time()
#             size = 0
#             path = add + '/%s' % (zai.strip().split('/')[-1])  # 路径
#             response = requests.get(zai,
#                                     stream=True)  # stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
#             chunk_size = 1024  # 每次块大小为1024
#             content_size = int(response.headers['content-length'])  # 返回的response的headers中获取文件大小信息
#             print("文件大小：" + str(round(float(content_size / chunk_size / 1024), 4)) + "[MB]")
#             with open(path, 'wb') as file:
#                 for data in response.iter_content(chunk_size=chunk_size):  # 每次只获取一个chunk_size大小
#                     file.write(data)  # 每次只写入data大小
#                     size = len(data) + size
#                     # 'r'每次重新从开始输出，end = ""是不换行
#                     print('\r' + "已经下载：" + int(size / content_size * 100) * "█" + " 【" + str(
#                         round(size / chunk_size / 1024, 2)) + "MB】" + "【" + str(
#                         round(float(size / content_size) * 100, 2)) + "%" + "】", end="")
#             end = time.time()
#             print("总耗时:" + str(end - start) + "秒")
#
#
#
# def yichang(wedq_list2, sdd):
#     for zai in wedq_list2:
#         try:
#             with open(sdd + '/%s' % (zai.strip().split('/')[-1]), 'r') as er:
#                 print("已存在,跳过")
#                 er.close()
#                 time.sleep(0.1)
#                 continue
#         except FileNotFoundError:
#             start = time.time()
#             size = 0
#             path = sdd + '/%s' % (zai.strip().split('/')[-1])  # 路径
#             response = requests.get(zai,
#                                     stream=True)  # stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
#             chunk_size = 1024  # 每次块大小为1024
#             content_size = int(response.headers['content-length'])  # 返回的response的headers中获取文件大小信息
#             print("文件大小：" + str(round(float(content_size / chunk_size / 1024), 4)) + "[MB]")
#             with open(path, 'wb') as file:
#                 for data in response.iter_content(chunk_size=chunk_size):  # 每次只获取一个chunk_size大小
#                     file.write(data)  # 每次只写入data大小
#                     size = len(data) + size
#                     # 'r'每次重新从开始输出，end = ""是不换行
#                     print('\r' + "已经下载：" + int(size / content_size * 100) * "█" + " 【" + str(
#                         round(size / chunk_size / 1024, 2)) + "MB】" + "【" + str(
#                         round(float(size / content_size) * 100, 2)) + "%" + "】", end="")
#             end = time.time()
#             print("总耗时:" + str(end - start) + "秒")

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
                kaishi = urllib.request.urlopen(page1, timeout=120, context=context)

                with open(path, 'wb') as f:
                    f.write(kaishi.read())

                    f.close()
                print("下载成功")
            except OSError:  # 错误文件名
                print("错误文件名")
                with open(path_error, 'wb') as f:
                    f.close()
                continue
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
                    f.write(urllib.request.urlopen(page1, timeout=120, context=context).read())

                    f.close()

                print("下载成功,大小为", daxiao(zai))
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
                        f.write(urllib.request.urlopen(page1, timeout=120, context=context).read())
                        f.close()
                    print("异常超时下载成功,大小为", daxiao(zai))

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
        for shu, wed1 in enumerate(urls):
            wedq_list.append(wed1)
        add = ('D:/pycharm project/xiazai/日本邪恶漫画大全：魚骨工造 大和抚子')


        #
        zhengchang(wedq_list, add)



if __name__ == '__main__':
    ma()