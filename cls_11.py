# !/usr/bin/python
# coding: utf8
# Time: 2020/1/19 12:40
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
for i in range(1, 10):
    line = ""
    for j in range(1, i+1):
        line += "{} x {} = {}\t".format(j, i, i*j)
    print(line)

