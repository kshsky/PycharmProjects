from scipy.stats import chi2                 # 卡方分布
from scipy.stats import norm                 # 正态分布
from scipy.stats import t                    # t分布
from scipy.stats import f                    # F分布
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import chi2_contingency     # 列联表分析


# rvs: Random Variates
# pdf: Probability Density Function                         概率密度函数
# cdf: Cumulative Distribution Function                     概率密度函数的积分函数
# sf: Survival Function (1-CDF)
# ppf: Percent Point Function (Inverse of CDF)              百分点函数，概率密度函数的积分值
# isf: Inverse Survival Function (Inverse of SF)
# stats: Return mean, variance, (Fisher’s) skew, or (Fisher’s) kurtosis
# moment: non-central moments of the distribution

# ppf以概率的形式，查询函数值-----------类似分布临界表

plt.figure(figsize=(12,16))
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号, 注意['SimHei']对应这句不行.

ax1 = plt.subplot(2,4,1)
# example ------------------------------------------- 卡方分布(右侧单边)
df = 20                                                   # 自由度
# print(chi2.ppf(0.01, df))                               # 计算函q=0.01概率时数值。其中 q = 1-a
# print(chi2.cdf(8.260, df))                              # 知道x值求a
x = np.linspace(chi2.ppf(0.01, df),                       # 绘制概率密度图
                 chi2.ppf(0.99, df), 100)
plt.plot(x, chi2.pdf(x, df), alpha=0.6, label='chi2 pdf')
plt.title(u'自由度为20时的卡方概率密度函数图', size=10)
# 计算平均数、方差、标准差
# print(chi2.mean(df))
# print(chi2.var(df))
# print(chi2.std(df))

ax2 = plt.subplot(2,4,2)
# # example ---------------------------------------------------- 标准正态分布(左侧单边)
# print(norm.ppf(0.6179))                                         # 知道q时求x, q=a
# print(norm.cdf(0.3))                                            # 知道x时求q
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
plt.plot(x, norm.pdf(x), alpha=0.6, label='norm pdf')
plt.title(u'标准正态分布概率密度函数图', size=10)

ax3 = plt.subplot(243)
# # example ----------------------------------------------------- t分布(双边分布)
df = 15
x = np.linspace(t.ppf(0.01, df), t.ppf(0.99, df), 100)
# print(t.ppf(0.95, df))                                           # q=0.95,a=(1-q)*2
# print(t.cdf(1.753, df))
plt.plot(x, t.pdf(x, df), alpha=0.6, label='t pdf')
plt.title(u'自由度为15时的t分布概率密度函数图', size=10)

ax4 = plt.subplot(244)
# # example ------------------------------------------------------ F分布(右侧单边分布)
df = 5
dn = 8
x = np.linspace(f.ppf(0.01, df, dn), f.ppf(0.99, df, dn), 100)
# print(f.ppf(0.95, df, dn))
plt.plot(x, f.pdf(x, df, dn), alpha=0.6, label='f pdf')
plt.title(u'自由度为5和8时的f分布概率密度函数图', size=10)

ax5 = plt.subplot(245)
# # example ------------------------------------------------------- 非标准正态分布

std = 1
mean = 2
normalDistribution = stats.norm(mean, std)                        # 构建统计分布
x = np.linspace(normalDistribution.ppf(0.01), normalDistribution.ppf(0.99), 100)
plt.plot(x, normalDistribution.pdf(x))
plt.title(u'非标准正态分布', size=10)

# example -------------------------------------------------------- 对连续数据进行正态拟合
# plt.figure()
# train = pd.read_csv("csv/Titanic/train.csv")
# train_Age = train.dropna(subset=['Age'])
# M_S = stats.norm.fit(train_Age['Age'])                            # 正态拟合的平均值与标准差
# train_Age['Age'].plot(kind='kde')                                 # 原本的概率密度分布图
#
# normalDistribution = stats.norm(M_S[0], M_S[1])                   # 绘制拟合的正态分布图
# x = np.linspace(normalDistribution.ppf(0.01), normalDistribution.ppf(0.99), 100)
# plt.plot(x, normalDistribution.pdf(x), c='orange')
# plt.xlabel('Age about Titanic')
# plt.title('Titanic[Age] on NormalDistribution', size=20)
# plt.legend(['Origin', 'NormDistribution'])
#
#
# # ----------------------------------------------------------------- R x C列联表，独立性检验
# # 建立关于性别与存活
# train_pclass_0 = train['Pclass'][train['Survived'] == 0].value_counts()
# train_pclass_1 = train['Pclass'][train['Survived'] == 1].value_counts()
# train_pclass_01 = pd.concat([train_pclass_0, train_pclass_1], axis=1, sort=True)
# train_pclass_01.columns = ['Not_Survived', 'Survived']
# g, p, dof, expctd = chi2_contingency(train_pclass_01.values)             # g为chi2值，服从自由度为dof的卡方分布
#
# print(g)
# # 拟合优度检验，判断两个分类型变量是否独立
# # 首先绘制卡方自由度为dof的曲线
# plt.figure()
# x = np.linspace(chi2.ppf(0.01, dof), chi2.ppf(0.99, dof), 100)
# plt.plot(x, chi2.pdf(x, dof))

# 以95%置信区间，查看小概率事件区间
# plt.axvline(chi2.ppf(0.975, dof), color='r')
# plt.axvline(chi2.ppf(0.025, dof), color='r')
# plt.title('chi2 distribution'+'whose dof is '+str(dof))
# plt.text(chi2.ppf(0.975, dof), 0.02, 'q=0.95,z='+str(round(chi2.ppf(0.975, dof), 2)), ha='right', va='top', color='g', alpha=0.8, size=15)
# plt.text(chi2.ppf(0.025, dof), 0.02, 'q=0.05,z='+str(round(chi2.ppf(0.025, dof), 2)), ha='left', va='top', color='g', alpha=0.8, size=15)

plt.show()