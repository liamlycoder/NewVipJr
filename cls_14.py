# !/usr/bin/python
# coding: utf8
# Time: 2020/1/15 12:52
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import random

# 回顾
questions = [
    '三国演义的作者是谁？',
    '贾宝玉出自哪部名著？'
]
yourQuestion = ['明世隐是什么类型的英雄？', '林黛玉怎么死的？']
# newQuestion = input("请输入您要添加的问题：")
# questions.append(newQuestion)
# questions.extend(yourQuestion)
# questions.insert(1, newQuestion)
# print(questions)

# del questions[0]
questions.remove("贾宝玉出自哪部名著？")
# print(questions)

# 这节课
arr = []
for i in range(10):
    arr.append(random.randint(1, 5))
print('随机数组：', arr)
arr.sort()
print(arr)
arr2 = []
for i in arr:
    for j in arr2:
        if arr.count(i) == int(j[2]):
            break
    else:
        if str(i) + '_' + str(arr.count(i)) not in arr2:
            arr2.append(str(i) + '_' + str(arr.count(i)))
print('统计结果', arr2)


