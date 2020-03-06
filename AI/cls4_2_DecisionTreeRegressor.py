# !/usr/bin/python
# coding: utf8
# Time: 2020/3/6 14:58
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

boston = load_boston()
# print(boston.DESCR)
"""
CRIM：城镇人均犯罪率；  　　　　　　　　　　　　ZN：住宅用地超过 25000 sq.ft. 的比例；
INDUS：城镇非零售商用土地的比例；　　　　　　　CHAS：查理斯河空变量（如果边界是河流，则为1；否则为0）；
NOX：一氧化氮浓度；　　　　　　　　　　　　　　RM：住宅平均房间数；
AGE：1940 年之前建成的自用房屋比例；　　　　　 DIS：到波士顿五个中心区域的加权距离；
RAD：辐射性公路的接近指数；　　　　　　　　　　TAX：每 10000 美元的全值财产税率；
PTRATIO：城镇师生比例；　　　　　　　　　　　　B：1000（Bk-0.63）^ 2，其中 Bk 指代城镇中黑人的比例。
LSTAT：人口中地位低下者的比例。
"""

X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=30)

# 建树三部曲
dtr = DecisionTreeRegressor(random_state=30, max_depth=6)
dtr.fit(X_train, y_train)
score = dtr.score(X_test, y_test)
print(score)

# 如何调参
import matplotlib.pyplot as plt
test = []
for i in range(10):
    dtr = DecisionTreeRegressor(random_state=30, max_depth=i+1)
    dtr.fit(X_train, y_train)
    score = dtr.score(X_test, y_test)
    test.append(score)
plt.plot(range(1, 11), test, color='red', label='max_depth')
plt.legend()
plt.show()





