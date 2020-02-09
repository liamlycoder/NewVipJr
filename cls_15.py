# !/usr/bin/python
# coding: utf8
# Time: 2020/2/6 08:53
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

# 元组特点：定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的类型

# 定义多个数据的元组
t1 = (2, 3, 4)

# 定义单个数据的元组
t2 = (6, )

# 如果不加逗号
t3 = (6)


# 元组不支持修改，只支持查找
tuple1 = ('Baidu', 'Tencent', 'Alibaba', 'Google')
# 1. 下标
print(t1[2])

# 2. index()
print(tuple1.index('Alibaba'))

# 3. count()
print(tuple1.count('Tencent'))

# 4. len()
print(len(tuple1))


# 元组是不支持修改的，但如果元组里面有列表，则列表里面的数据是课修改的，故自觉很重要
tuple2 = ('Baidu', ['Tencent', 'Alibaba'], 'Google')
tuple2[1][0] = 'Microsoft'
print(tuple2)

