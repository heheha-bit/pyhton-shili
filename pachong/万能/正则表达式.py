import re

list=['/',':','*','?','\"','<','>','|']
str="里番漫画[藤丸] ユアソング +/:*?\"<>|\\ 8P小冊子"

t=re.sub('[+/:*?\"<>|\\\]',' ', str)
print(t)


