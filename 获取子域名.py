import requests  # 导入requests库
import re
# url = "http://www.baidu.com/s?wd=site:qq.com" #设定url请求

match = "style=\"text-decoration:none;\">(.*?)&nbsp;"
stack = []
for i in range(48):
    i = i*10
    url = "http://www.baidu.com/s?wd=site:hevttc.edu.cn&cl=3&pn=%s" %i
    response = requests.get(url).content  # get请求,content是获得返回包正文
    lists = re.findall(match, response)
    stack += lists
site = list(set(stack))#set()实现去重

lists = []
for i in site:
    i = i.strip()
    if i.find('//')!=-1:
        i = i.split('//')[1]
    i = i.split('/')[0]
    lists.append(i)

lists = list(set(lists))

for str in lists:
    print str

# print response