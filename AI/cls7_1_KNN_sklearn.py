'''
@Author: Liam
@E-mail: luyu.real@qq.com
@Date: 2020-04-17 21:24:05
@LastEditTime: 2020-04-18 09:17:16
@Software: Visual Studio Code
'''
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

 
# 加载 sklearn 中的 datasets 数据中的digits（手写字体数据）
digits = datasets.load_digits()
x = digits.data
y = digits.target
# 使用 train_test_split 进行模型建立和测试的分离,加zhiqian是因为没有进行
# 归一化处理
X_train_zhiqian, X_test_zhiqian, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)
# 使用 StandardScaler进行归一化处理
"""为什么使用X_train_zhiqian进行归一化处理的均值和方差进行对X_test的归一化呢？
是因为要服从现实情况，如果只有一个数据进行预测，就没有办法得出均值和方差
"""
s = StandardScaler()
s.fit(X_train_zhiqian)
X_train = s.transform(X_train_zhiqian)
X_test = s.transform(X_test_zhiqian)
knn_clf = KNeighborsClassifier()
# 使用网格搜索的方法进行对超参数的选取
# 超参数是指在算法进行时对不确定的参数进行调整以使得算法的预测准确率最高
params = [{
    "weights": ["uniform"],
    "n_neighbors": [k for k in range(1, 11)]
}, {
    "weights": ["distance"],
    "n_neighbors": [k for k in range(1, 11)],
    "p": [k for k in range(1, 6)]
}
]
# n_jobs 这个参数是使用计算机的几个核，赋值为-1表示全都使用
gridsearch = GridSearchCV(knn_clf, params, n_jobs=-1)
gridsearch.fit(X_train, y_train)
print("best_score", gridsearch.best_score_)
print("best_params", gridsearch.best_params_)
# 将最好的赋值给knn_clf
knn_clf = gridsearch.best_estimator_
print(knn_clf.score(X_test, y_test))
