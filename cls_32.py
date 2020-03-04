# !/usr/bin/python
# coding: utf8
# Time: 2020/3/4 18:40
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

# 上节课作业
"""
user = input("用户名：")
with open("database.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i % 2 == 0 and lines[i].strip('\n') == user:
            password = input("密码：")
            if lines[i+1].strip('\n') == password:
                print("登陆成功")
            else:
                print('密码错误')
            break
    else:
        print('该用户没有注册')
"""


import time
ticks = time.time()
print(ticks)

localtime = time.localtime()
print(localtime)

ltime = time.asctime()
print(ltime)

print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

t0 = time.perf_counter()
sum = 0
for i in range(999999):
    sum += i
t1 = time.perf_counter()
print("用时：{:.2}".format(t1-t0))

