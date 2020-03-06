# !/usr/bin/python
# coding: utf8
# Time: 2020/2/29 01:47
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd

# 导入数据
wine = load_wine()  # 加载葡萄酒数据集
pd_wine = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)  # 拼接成表格方便查看数据
# print(pd_wine)
# print(wine.feature_names, wine.target_names)

# 给定中文的名称
feature_names = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类',
                '花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']
target_names = ['琴酒', '雪莉', '贝尔摩德']

# 数据分割
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=30)
# print(X_train.shape)

# 三步走流程
clf = tree.DecisionTreeClassifier(criterion="entropy", random_state=30, splitter='random')
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)

print(score)  # 打印得分
# print(clf.feature_importances_)
print([*zip(feature_names, clf.feature_importances_)])  # 打印每个特征的重要性程度


"""
# 决策树可视化
import graphviz
dot_data = tree.export_graphviz(clf
                               ,feature_names = feature_name
                               ,class_names = ["琴酒","雪莉","贝尔摩德"]
                               ,filled = True    # 是否填充颜色
                               ,rounded = True)  # 框的形状

graph = graphviz.Source(dot_data)
print(graph)
"""


