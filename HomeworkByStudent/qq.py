import sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
digits=load_digits
X,y=digits.data,digits.target
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=100)
gnb=GaussianNB().fit(Xtrain,ytrain)
acc_score=gnb.score(Xtest,ytest)
ypred=gnb.predict(Xtest)
from sklearn.metrics import confusion_matrix as CM
cm=CM(ytest,ypred)
print(cm)