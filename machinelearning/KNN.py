import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]

matrix = metrics.confusion_matrix(y_true,y_pred)
print(matrix)
print(metrics.accuracy_score(y_true,y_pred))
# Target is multiclass but average='binary'. Please choose another average setting, one of [None, 'micro', 'macro', 'weighted'].

print(metrics.precision_score(y_true,y_pred,average='macro'))
print(metrics.precision_score(y_true,y_pred,average='micro'))
print(metrics.precision_score(y_true,y_pred,average='weighted'))
print(metrics.precision_score(y_true,y_pred,average=None))

print(metrics.recall_score(y_true,y_pred,average=None))
print(metrics.roc_auc_score(y_true,y_pred,average='macro'))
print(metrics.precision_recall_curve(y_true,y_pred))
fpr,tpr,thresholds = metrics.roc_curve(y_true,y_pred)

print(fpr)
print(tpr)
print(thresholds)
print(metrics.auc(fpr,tpr))
