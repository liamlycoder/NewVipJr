# !/usr/bin/python
# coding: utf8
# Time: 2020/2/16 03:26
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from sklearn import datasets
from sklearn import linear_model
diabetes = datasets.load_diabetes()

with open("data.txt", "w") as f:
    f.write(str(diabetes))


#数据前十列数值为生理数据，分别表示
#年龄，性别，体质指数，血压，S1,S2,S3,S4,S5,S6(六种血清的化验数据)
# print(diabetes.data[0])

model = linear_model.LinearRegression()
x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]
model.fit(x_train, y_train)




