# !/usr/bin/python
# coding: utf8
# Time: 2020/5/12 10:12
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import sys

degree = "DCBAAE"
score = int(input("请输入分数："))
if score > 100 or score < 0:
    print("分数必须在0-100之间")
    sys.exit()
else:
    index = (score - 60) // 10
    if index >= 0:
        print(degree[index])
    else:
        print(degree[-1])

