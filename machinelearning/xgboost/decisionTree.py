from sklearn import datasets
# 加载乳腺癌数据
cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size =1/5.,random_state = 8)


from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn import metrics
# 决策树
clf = tree.DecisionTreeClassifier(max_depth=4)
# 训练模型
clf.fit(X_train,y_train)

# 预测
y_pred = clf.predict(X_test)

# 评估预测效果
print(classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
print(metrics.accuracy_score(y_test, y_pred))