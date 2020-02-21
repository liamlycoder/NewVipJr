# !/usr/bin/python
# coding: utf8
# Time: 2020/2/16 03:21
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
# print(iris.data.shape, iris.target.shape)
# 四个特征：花萼长度(cm)、花萼宽度(cm)、花瓣长度(cm)、花瓣宽度(cm)
# 三个分类：山鸢尾花(Iris Setosa)、变色鸢尾花(Iris Versicolor)、维吉尼亚鸢尾花(Iris Virginica)

X = iris.data[:, [2, 3]]
y = iris.target  # 标签已经转换成0，1，2了

"""数据分割"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# test_size : 测试集所占的比例，如果输入为float类型，代表测试集在总集中所占的比例，默认为0.25；
# 如果为int类型，代表测试集中包含多少条样例；如果不输入的话，不指定train的大小就是0.25，否则是train的补集

"""将特征使用最大最小值法缩放"""
mc = MinMaxScaler()
mc.fit(X_train)
X_train_mm = mc.transform(X_train)
X_test_mm = mc.transform(X_test)

"""开始训练"""
model = LogisticRegression()
model.fit(X_train_mm, y_train)

"""模型评估"""
result = model.score(X_test_mm, y_test)
print(result)

"""数据可视化"""
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
pd_iris = pd.DataFrame(iris.data, columns=names)
scatter_matrix(pd_iris, alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.show()


