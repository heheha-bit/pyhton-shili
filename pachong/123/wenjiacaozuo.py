categories ='yichang2'
with open('%s.txt' % categories, 'r') as file1:
    urls = file1.readlines()  # 计数行数
    file1.close()  # 关闭文件
with open('%s.txt' % categories, 'w+') as file2:
    for i in range(2, len(urls)):
        file2.write(urls[i])
    file2.close()  # 关闭文件
# import re
# zai='http://img.lifanacgmh.cc/uploads/allimg003/20181209/Scan065.jpg'
# zai2='http://img.lifanacgmh.cc/uploads/allimg002/20180528/STARS_18054_003.jpg'
# zai1='http://img.lifanacgmh.cc/uploads/allimg002/20180706/Cuid_007.jpg'
#
# for t in range(len(zai) - 1, -1, -1):  # 链接切片位置计算
#     if zai[t] == '.':
#         endflag = t
#     if zai[t] == '/':
#         staflag = t + 1
#         break
# p1 = zai[0:staflag]
#
# z = zai[staflag:endflag]
# p2 = zai[endflag:len(zai)]
# shu0 = str(re.sub("\D", "", zai[staflag:endflag]))
# c = str(z.replace(shu0, ""))
# ti=zai
#
# for i in range(100, 110):
#
#         if ti[-5] == shu0[len(shu0)-1]:
#
#             if shu0[0] == '0' and shu0[1]=='0':
#                 if i >= 10 and i < 100:
#
#                     zui = str(p1  +c + str(shu0[0:len(shu0) - 2])+ str(i) +  p2)
#
#
#                 elif i >= 100:
#
#                     zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))]) + str(i) + p2)
#
#
#                 else:
#                     zui = str(p1 + c +  str(shu0[0:len(shu0) - 1])  +str(i) + p2)
#             elif shu0[0] == '0':
#                 if i >= 10 and i < 100:
#
#                     zui = str(p1 + c + str(shu0[0:len(shu0) - 2]) + str(i) + p2)
#
#
#                 elif i >= 100 and int(shu0)<10:
#
#                     zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))-1]) + str(i) + p2)
#                 elif i >= 100 and int(shu0)>=10:
#
#                     zui = str(p1 + c + str(shu0[0:len(shu0) - len(str(i))-3]) + str(i) + p2)
#
#
#                 else:
#                     zui = str(p1 + c + str(shu0[0:len(shu0) - 1]) + str(i) + p2)
#             else:
#                 zui = str(p1 + c + str(i) + p2)
#         else:
#             if shu0[0] == '0' and shu0[1]=='0':
#                 if i >= 10 and i < 100:
#
#                     zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)
#
#
#                 elif i >= 100:
#
#                     zui = str(p1 +str(shu0[0:len(shu0) - len(str(i))]+ str(i)) + c + p2)
#
#
#                 else:
#                     zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)
#             elif shu0[0] == '0':
#                 if i >= 10 and i < 100:
#
#                     zui = str(p1  + str(shu0[0:len(shu0) - 2])+ str(i) + c + p2)
#
#
#                 elif i >= 100:
#
#                     zui = str(p1 +str(shu0[0:len(shu0) - len(str(i))-1]+ str(i)) + c + p2)
#
#
#                 else:
#                     zui = str(p1 +  str(shu0[0:len(shu0) - 1])  +str(i)+ c + p2)
#             else:
#                 zui = str(p1 + c + str(i) + p2)
#
#
#         print("--------------------------------------->", zui, "<---------------------------------------------")




