# !/usr/bin/python
# coding: utf8
# Time: 2020/1/20 20:27
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import requests
import bs4
url = "https://so.gushiwen.org/mingju/"
req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, "html.parser")
lst = soup.find_all('a', {'target': "_blank"})
for i in range(1, len(lst)):
    if i % 2 == 0:
        with open("result.txt", 'a') as f:
            f.write("          ---" + str(lst[i].contents[0]) + "\n")
    else:
        with open("result.txt", 'a') as f:
            f.write(lst[i].contents[0] + "\n")







