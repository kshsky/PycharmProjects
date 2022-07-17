from sklearn.metrics import confusion_matrix as cm
print(cm([0,1,0,1],[1,1,1,0]))

from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]


print(confusion_matrix(y_true, y_pred))
# array([[2, 0, 0],
#        [0, 0, 1],
#        [1, 0, 2]])

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
print(confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"]))
# array([[2, 0, 0],
#        [0, 0, 1],
#        [1, 0, 2]])
#


tn, fp, fn, tp = confusion_matrix([0, 1, 0, 1], [1, 1, 1, 0]).ravel()
print(tn, fp, fn, tp)
# (0, 2, 1, 1)