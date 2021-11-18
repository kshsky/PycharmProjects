from sklearn.datasets import load_iris

from sklearn.preprocessing import normalize

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import scale
from sklearn import metrics
from machinelearning.tools import mlTools
# iris_data = load_iris()
# print(iris_data)


# data = pd.read_csv('dataFile/iris.csv')
# print(data)

# iris_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', sep=",", names=['sepal_length','sepal_width','petal_length','petal_width','class'])
iris_data = pd.read_csv('dataFile/iris.data', sep=",", names=['sepal_length','sepal_width','petal_length','petal_width','class'])

print(iris_data)

#柱状图显示组平均数，可以从图上看出不同品种的属性特点
#把不同的品种分成不同的组，此数据为3组
grouped_data=iris_data.groupby("class")
#求组平均值
group_mean=grouped_data.mean()
#绘图
group_mean.plot(kind="bar")
plt.legend(loc="best")
plt.xticks(rotation=0)
plt.show()


def getAccuracy(testSet,predictions):
    correct = 0
    # 遍历每个测试样本，判断是否预测正确并进行统计
    for x in range(len(testSet)):
        if testSet[x] == predictions[x]:
            correct+=1
        # 计算并返回准确率
    return (correct/float(len(testSet))) * 100.0

# 生成一个随机数并选择小于0.8的数据
msk = np.random.rand(len(iris_data)) < 0.8
print(msk)
train_data_origin = iris_data[msk]
test_data_origin = iris_data[~msk]
# 将生成的训练集train_data和测试集test_data进行索引重置
train_data = train_data_origin.reset_index(drop=True)
test_data = test_data_origin.reset_index(drop=True)

# 训练集label、测试集label
train_label = train_data['class']
test_label = test_data['class']

# 训练集特征、测试集特征
train_fea = train_data.drop('class',1)
test_fea = test_data.drop('class',1)

#
train_norm = (train_fea - train_fea.min()) / (train_fea.max() - train_fea.min())
test_norm = (test_fea - test_fea.min()) / (test_fea.max() - test_fea.min())

from sklearn import neighbors
# 定义KNN模型
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(train_norm, train_label)
# 对测试集进行预测
predict = knn.predict(test_norm)
# 评估模型准确率
accuracy = getAccuracy(test_label, predict)
print("Accuracy:" + repr(accuracy) + "%")

print(metrics.accuracy_score(test_label,predict))

mlTools.classificationModel(test_label,predict)