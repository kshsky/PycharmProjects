from sklearn.linear_model import Ridge
import pandas as pd
import numpy as np

path=r'D:\git\机器学习实战\Ch08'
data = np.loadtxt(path+'/abalone.txt',delimiter='\t')

x=data[:,:-1]
y=data[:,-1]
alpha=1

ridge = Ridge(alpha=1,fit_intercept=False)
ridge.fit(x,y)
print(ridge.coef_)
# print(ridge.intercept_)

def ridgeps(x,y,alpha=1):
    x = np.mat(x)
    y = np.mat(np.array(y).reshape(-1,1))
    w = (x.T*x + alpha * np.eye(x.shape[1])).I*x.T*y
    return w

w = ridgeps(x,y)
print(w.A.ravel())
x1 = np.c_[[1]*x.shape[0],x]

ridge.fit(x1,y)
print(ridge.coef_)
w = ridgeps(x1,y)
print(w.A.ravel())