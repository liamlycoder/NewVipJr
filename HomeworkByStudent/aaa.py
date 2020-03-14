from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.model_selection impott train_test_split
from sklearn.datasets import land_leaf
leaf=land_leaf()
x_train,x_test,y_train,y_test=train_test_split(leaf.data,leaf.target)
dtr=DecisionTreeRegressor(random_state=30,max_depth=i+1)
dtr.fit(x_train,y_train)
score=dtr.fit(x_test,y_test)
print(score)
text=[]
for i in range(10):
    dtr=DecisionTreeRegressor(random_state=30,max_depth=i+1)
    dtr.fit(x_train,y_train)
    score=dtr.fit(x_test,y_test)
    test.append(score)
plt.plot(range(1,11),test,color='red',label='max_depth')
plt.legrnd()
plt.show()
