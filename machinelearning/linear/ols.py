#部分较常用的结果数值提取具体操作示例如下
from statsmodels.formula.api import ols
import numpy as np
import pandas as pd
#from statsmodels.stats.anova import anova_lm
x=np.array([15,20,25,30,35,40,45])
y=np.array([330,345,365,405,445,450,455])
df=pd.DataFrame({'x':x,'y':y})
formula='y~x'
fit=ols(formula,df).fit()
fit.summary()# 查看模型结果
print(fit.summary())
print('提取回归系数 fit.params\n {}'.format(fit.params))
print('提取回归系数标准差 fit.bse\n {}'.format(fit.bse))
print('提取回归系数p值 fit.pvalues\n {}'.format(fit.pvalues))

print('提取回归系数t值 fit.tvalues\n {}'.format(fit.tvalues))
print('提取回归系数置信区间 fit.conf_int()\n {}'.format(fit.conf_int()))
print('提取回归系数置信区间 fit.conf_int(0.05)\n {}'.format(fit.conf_int(0.05)))
print('提取回归系数置信区间 fit.conf_int(0.1)\n {}'.format(fit.conf_int(0.1)))
print('=================')
print('提取模型预测值 fit.fittedvalues\ntvalues----\n{}'.format(fit.fittedvalues))
print('提取残差 fit.resid\n{}'.format(fit.resid))
print('模型自由度（系数自由度） fit.df_model\n{}'.format(fit.df_model))
print('残差自由度（样本自由度） fit.df_resid\n{}'.format(fit.df_resid))
print('模型样本数量 fit.nobs\n{}'.format(fit.nobs))
print('=================')
print('提取R方 fit.rsquared:{}'.format(fit.rsquared))
print('提取调整R方 fit.rsquared_adj:{}'.format(fit.rsquared_adj))
print('提取F-statistic fit.fvalue:{}'.format(fit.fvalue))
print('提取F-statistic 的pvalue fit.f_pvalue:{}'.format(fit.f_pvalue))
print('模型mse fit.mse_model:{}'.format(fit.mse_model))
print('残差mse fit.mse_resid:{}'.format(fit.mse_resid))
print('总体mse fit.mse_total:{}'.format(fit.mse_total))
print('提取AIC fit.aic:{}'.format(fit.aic))
print('提取BIC fit.bic:{}'.format(fit.bic))
print('=================')
print('协方差矩阵比例因子 fit.scale\n{}'.format(fit.scale))
print('White异方差稳健标准误 fit.HC0_se\n{}'.format(fit.HC0_se))
print('MacKinnon和White（1985）的异方差稳健标准误 fit.HC1_se\n{}'.format(fit.HC1_se))
print('White异方差矩阵 fit.cov_HC0\n{}'.format(fit.cov_HC0))
print('MacKinnon和White（1985）的异方差矩阵 fit.cov_HC1\n{}'.format(fit.cov_HC1))
