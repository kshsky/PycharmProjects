import numpy as np


'''
    李航-统计学习方法
    p159-adaboost例子
    最终结果由两部分构成：分类器系数alpha+{分类器阈值:分类器标记值}

'''
x = np.arange(10)
y = np.array([1] * 3 + [-1] * 3 + [1] * 3 + [-1])
# 节点域 r
r = np.arange(0.5, 10, 1)
print('x：',x)
print('y:',y)
print('r:',r)
print('=============================')
#分类器
# G(a,b,threh)  <=threh则a，否则b
def build_adaboost(x, y, r):

    # 初始化权值分布
    w = np.array([0.1] * len(x))
    print('w:', w)
    thr = 0
    g = 0

    # g的系数
    alpha_list = []

    # threshold 阈值list ,分类器是基于阈值的
    thr_list = []

    # 误差率,中间变量，最小误差率更新g系数alpha
    # 迭代err
    err_ist_tmp = []

    # (left,right)
    y_list = []
    y_list_tmp = []
    i=0
    flag = True

    while flag:
        i = 1
        err_ist_tmp.clear()
        y_list_tmp.clear()
        # 获取当前w下最小分类错误率对应的阈值
        for v in r:
            # 基本分类器
            #确定分类结果的位置  -1,r,1 或者 1,r,-1
            g1 = [1 if t > v else -1 for t in x]
            g2 = [-1 if t > v else 1 for t in x]
            err1 = np.sum((g1 != y) * w)
            err2 = np.sum((g2 != y) * w)
            print('err1,err2',err1,err2)
            min_err = 0
            if (err1 < err2):
                min_err = err1
                err_ist_tmp.append(round(min_err, 4))
                y_list_tmp.append((-1, 1))
            else:
                min_err = err2
                err_ist_tmp.append(round(min_err, 4))
                y_list_tmp.append((1, -1))

            print(round(v, 2), '时错误率：{}'.format(round(min_err, 4)))

        index = np.argmin(err_ist_tmp)

        # 获取分类器的分类值
        left,right=y_list_tmp[index][0],y_list_tmp[index][1]
        y_list.append(y_list_tmp[index])

        thr_value = r[index]
        thr_list.append(thr_value)

        # 当前最小错误率
        e = err_ist_tmp[index]

        # 更新alpha
        alpha = round((np.log((1 - e) / e)) / 2, 4)
        alpha_list.append(alpha)

        print('最小错误率:{}；分类阈值：{}；g系数：{}'.format(np.min(err_ist_tmp), r[np.argmin(err_ist_tmp)], alpha))

        # 更新分类树
        for i in range(0, len(alpha_list)):
            left, right = y_list[i][0], y_list[i][1]
            print('重新分类：',[right if t > thr_list[i] else left for t in x])
            g += np.array(alpha_list[i]) * np.array([right if t > thr_list[i] else left for t in x])
            print('g : ',g)
        print('分类器叠加结果：{}'.format(np.sign(g)))

        if  (np.sign(g) == y).all():
            print('第{}次迭代结束，预测结果{}'.format(i + 1, (np.sign(g) == y).all()))
            flag = False
            break

        # 更新权值系数w,下一w只与当前g有关
        cur_g=[right if i > thr_value else left for i in x]
        w = (w * np.exp(-alpha * y * cur_g)) / np.sum(w * np.exp(-alpha * y * cur_g))
        print('w:',w)
        print('第{}次迭代结束，'
              '分类错误的点还有{}个,'
              '预测结果{},进入下次迭代，'
              '更新权值系数为{}'.format(i + 1,len(x) - sum(np.sign(g) == y),(np.sign(g) == y).all(),w))
        # 本次迭代完毕，进入下次迭代
        i += 1
    return alpha_list,dict(zip(thr_list,y_list))


def ababoost_pred(xx):
    alpha,thr=build_adaboost(x,y,r)
    #使用阈值进行分离
    print([np.where(np.array(xx)>i,thr.get(i)[1],thr.get(i)[0]) for i in thr.keys()])
    #整合
    print(np.array([np.where(np.array(xx)>i,thr.get(i)[1],thr.get(i)[0]) for i in thr.keys()]).T)
    #乘以分类器系数
    print('乘以分类器系数')
    print(np.array(alpha)*np.array([np.where(np.array(xx)>i,thr.get(i)[1],thr.get(i)[0]) for i in thr.keys()]).T)
    #叠加
    print(np.sum(np.array(alpha) * np.array([np.where(np.array(xx) > i, thr.get(i)[1], thr.get(i)[0]) for i in thr.keys()]).T,axis=1))
    #添加sign
    print(np.sign(np.sum(np.array(alpha) * np.array([np.where(np.array(xx) > i, thr.get(i)[1], thr.get(i)[0]) for i in thr.keys()]).T,axis=1)))

xx=[3,6,9]
ababoost_pred(xx)




