# !/usr/bin/python
# coding: utf8
# Time: 2020/7/19 19:03
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import random

scores = []
for i in range(60):
    scores.append(random.randint(0, 100))

nums = []
for i in range(0, 101):
    person = [i, scores.count(i)]
    nums.append(person)

nums.sort(key=lambda x: x[1], reverse=True)
for i, j in nums:
    print("分数为{}的人数有{}个".format(i, j))


