# !/usr/bin/python
# coding: utf8
# Time: 2020/1/22 09:05
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import bs4
import requests

gushi = requests.get("https://www.gushiwen.org/")
html_doc = """
    <html><head><title>The Dormouse‘s story</title></head> 
    <body> 
    <p class=“title”><b>The Dormouse‘s story</b></p> 
    <p class=“story”>
    Once upon a time there were three little sisters; and their names were: 
    <a href=“http://example.com/elsie” class=“sister” id=“link1”>Elsie</a>, 
    <a href=“http://example.com/lacie” class=“sister” id=“link2”>Lacie</a> and  
    <a href=“http://example.com/tillie” class=“sister” id=“link3”>Tillie</a>,
    and they lived at the bottom of a well.</p> 
    <p class=“story”>...</p> 
"""
soup = bs4.BeautifulSoup(gushi.text, "html.parser")
res = soup.find_all("div", {"class": "contson"})
for i in res:
    print(i.strings)
    print("*"*55)


