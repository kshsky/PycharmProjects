import numpy as np
from decimal import *

'''
    李航-统计学习方法
    p159-adaboost例子
    最终结果由两部分构成：分类器系数alpha+{分类器阈值:分类器标记值}

'''
x = np.arange(10)
y = np.array([1] * 3 + [-1] * 3 + [1] * 3 + [-1])
# 节点域 r
threshold = np.arange(0.5, 10, 1)
print('x：',x)
print('y:',y)
print('threshold:',threshold)
print('=============================')

# 修改为： {(threh,flagA,flagB):err_rate}
def build_adaboost(x, y, threshold):
    # 分类器字典,存储{(threshold,flagA,flagB):alpha}
    G = {}
    # 初始化权值分布
    w = np.array([0.1] * len(x))
    print('w:', w)
    # g的系数
    alpha_list = []
    flag = True
    k = 1
    #分类器temp字典，存储{(threshold,flagA,flagB):error_rate}
    G_temp={}
    while flag:
        print('=================================================')
        g=0
        G_temp.clear()
        # 获取当前w下最小分类错误率对应的阈值
        for r in threshold:
            # 基本分类器{(threhflageA,flagB):err_rate]}
            #确定分类结果的位置  -1,r,1 或者 1,r,-1
            g1 = [1 if xx > r else -1 for xx in x]
            g2 = [-1 if xx > r else 1 for xx in x]
            err1 = np.sum((g1 != y) * w)
            err2 = np.sum((g2 != y) * w)
            G_temp.update({(r,-1,1):err1})
            G_temp.update({(r,1,-1):err2})
            print((r,-1,1), '错误率：{}'.format(err1))
            print((r,1,-1), '错误率：{}'.format(err2))

        tupleK = min(G_temp,key=G_temp.get)
        # 获取分类器的分类值
        left,right=tupleK[1],tupleK[2]
        # 当前最小错误率
        minError = G_temp.get(tupleK)

        # 更新alpha
        alpha = np.log((1 - minError) / minError)/2
        alpha_list.append(alpha)
        G.update({tupleK:alpha})
        print('最小错误率:{}；分类阈值：{}；g系数：{}'.format(minError,tupleK[0], alpha))

        # 更新权值系数w,下一w只与当前g有关
        cur_result=[right if i > tupleK[0] else left for i in x]
        # 规范化因子Zm
        Zm = np.sum(w * np.exp(-alpha * y * cur_result))
        #更新权值系数w 只有权值系数进入下一次迭代
        w = (w * np.exp(-alpha * y * cur_result)) / Zm
        print('w:',w)

        # {(threshold, flagA, flagB): alpha}
        for i in G.keys():
            print('---------',k,'---------')
            result = [i[2] if xx > i[0] else i[1] for xx in x]
            print('分类树分类结果：',)
            # 更新分类树g,需要迭代每一次分类结果，更新结束，就是最终分类器
            print('g : ', g)
            g += np.array(G[i]) * np.array(result)
            print('g : ',g)
            print('分类器叠加结果：{}'.format(np.sign(g)))
            print('分类正确：{}'.format(np.sum(np.sign(g)==y)))

            if  (np.sign(g) == y).all():
                print('第{}次迭代结束，预测结果{}'.format(k, (np.sign(g) == y).all()))
                flag = False
                break
        print('第{}次迭代结束，'
              '分类错误的点还有{}个,'
              '预测结果{},进入下次迭代，'
              '更新权值系数为{}'.format(k,len(x) - sum(np.sign(g) == y),(np.sign(g) == y).all(),w))


        # 本次迭代完毕，进入下次迭代
        k += 1


    return G


def ababoost_pred(xx):
    G =build_adaboost(x,y,threshold)
    alpha = G.values()
    GList = G.keys()
    print('==============use======================')
    print(G)
    print(G.values())
    print(G.keys())
    #使用阈值进行分离
    print('使用阈值进行分离：得到三个分类器的分类结果：')
    print([np.where(np.array(xx)>i[0],i[1],i[2]) for i in GList])
    #整合
    print('将三个分类器的分类结果进行整合（每一列是一个分类器结果）：')

    result = np.array([np.where(np.array(xx)>i[0],i[1],i[2]) for i in GList]).T
    print(result)
    #乘以分类器系数
    print('乘以分类器系数')
    print(np.array(list(alpha)))
    print(np.array(list(alpha)) * result)

    #叠加
    print('叠加(每一列是一个分类器，每一行相加，得到每个值的最终分类结果):')
    print(np.sum(np.array(list(alpha)) * result,axis=1))
    #添加sign
    print('sign,输出预测结果：')
    print(np.sign(np.sum(np.array(list(alpha)) * result,axis=1)))


xx=[3,6,9]
ababoost_pred(xx)




