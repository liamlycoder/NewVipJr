# !/usr/bin/python
# coding: utf8
# Time: 2020/2/9 17:42
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")  # 屏蔽警告信息

# 线性回归模型
from sklearn import linear_model
X = [[6], [8], [10], [14], [18]]   # 匹萨的直径
y = [[7], [9], [13], [17.5], [18]]  # 匹萨的价格
model = linear_model.LinearRegression()  # 创建一个线性回归模型的对象
model.fit(X, y)   # 用线性回归模型进行数据
a = model.predict([[12]])   # 预测一下直径为12的匹萨价格多少吧
print("一张12英寸的匹萨价格是: {:.2f}".format(a[0][0]))

# 模型评估
x_test = [[7], [15], [21], [25], [26]]
y_test = [[8.3], [16], [23], [28.5], [30]]
print(model.predict(x_test))  # 用我们的模型预测出来的价格
print(model.score(x_test, y_test))  # 计算R值






import matplotlib.pyplot as plt  # 导库
from matplotlib.font_manager import FontProperties  # 字体库
# font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)  # Windows
font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Medium.ttc", size=10)  # macOS
def runplt():   # 用于绘制图像的函数
    plt.title('匹萨价格与直径数据', fontproperties=font)  # 设置图标题
    plt.xlabel('直径(英寸)', fontproperties=font)  # 设置横轴标题
    plt.ylabel('价格(美元)', fontproperties=font)  # 设置纵轴标题
    plt.axis([0, 25, 0, 25])  # 设置刻度
    plt.grid(True)  # 显示网格
    return plt
plt = runplt()
plt.plot(X, y, 'ro')  # 绘图
plt.show()  # 显示图像
