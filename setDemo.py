# !/usr/bin/python
# coding: utf8
# Time: 2020/8/1 13:19
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
hobby1 = {'玩游戏', '看电视', '听音乐'}
hobby2 = {'唱歌', '购物', '看电视'}
hobby3 = {'玩游戏', '听音乐'}

print(hobby1)

lst = [
    {'姓名': 's1', '爱好': hobby1},
    {'姓名': 's2', '爱好': hobby2},
    {'姓名': 's3', '爱好': hobby3},

]

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i]['爱好'] & lst[j]['爱好']:
            print(lst[i]['姓名'] + "和" + lst[j]['姓名'] + "会成为好朋友")

