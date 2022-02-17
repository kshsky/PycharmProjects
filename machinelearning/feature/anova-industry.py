import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import levene
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

num = np.array([57,66,49,40,34,53,44,68,39,29,45,56,51,31,49,21,34,40,44,51,65,77,58])
industry=['零售业','零售业','零售业','零售业','零售业','零售业','零售业',
          '旅游业','旅游业','旅游业','旅游业','旅游业','旅游业',
          '航空公司','航空公司','航空公司','航空公司','航空公司',
          '家电制造业','家电制造业','家电制造业','家电制造业','家电制造业']
df=pd.DataFrame(data ={'num':num,'industry':industry})
print(len([57,66,49,40,34,53,44,68,39,29,45,56,51,31,49,21,34,40,44,51,65,77,58]))
# print(df)
#先查看方差是否一致
lingshou =df['num'][df.industry=='零售业']
lvyou =df['num'][df.industry=='旅游业']
hangkong =df['num'][df.industry=='航空公司']
jiadian =df['num'][df.industry=='家电制造业']
print('------------levene:检验方差是否相等------------------')
#levene方差齐性假设，
# 检验结果为p>0.05所以，可以认为方差是相等的
leveneResult = stats.levene(lingshou,lvyou,hangkong,jiadian)
stat,p = stats.levene(lingshou,lvyou,hangkong,jiadian)
print(leveneResult)
print(leveneResult.statistic)
print(leveneResult.pvalue)
#单因素方差分析 f_oneway
f,p  = stats.f_oneway(lingshou,lvyou,hangkong,jiadian)
f_onewayResult  = stats.f_oneway(lingshou,lvyou,hangkong,jiadian)
# pvalue=0.03876452440122184 < 0.05 说明四组数据之间有差异。
print(stats.f_oneway(lingshou,lvyou,hangkong,jiadian))
print('f-critical:{},p-value:{}'.format(f_onewayResult.statistic,f_onewayResult.pvalue))
print('f-critical:{}'.format(stats.f.ppf(0.95,3,19)))
print('confidence:{}'.format(stats.f.cdf(f,3,19)))