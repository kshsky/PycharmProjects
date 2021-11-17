import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

from sklearn.datasets import load_iris
import scipy.stats

oridata = load_iris()
data = oridata.data
columns = oridata.feature_names
df = pd.DataFrame(data = data, columns = columns)

# print(df)
# print(oridata.target)
df['species']=oridata.target

# print(df)

for i in columns:
    print('\n\n\n{}n\n\n\n\n'.format(i))
    x = df[i]
    y = df.species
    # y~x 表示x是自变量，y是因变量，计算自变量对因变量的影响程度
    formula = 'y~x'
    fit = ols(formula,df).fit()
    print('summmary ================== ',i)
    print(fit.summary())
    print('F检验')
    print(anova_lm(fit))

    #df_model 参数个数
    dfn=fit.df_model
    dfd=fit.df_resid
    fv=fit.fvalue
    print('fvalue:',fv)
    print('dfn = dfn,dfd = dfd',dfn,dfd)
    print('检查f检验临界值：（fv大于该临界值）')
    criticalFValue= scipy.stats.f.ppf(q=1-0.05,dfn = dfn,dfd = dfd)
    print('{}对{}的影响显著性：{}'.format(i,'species',fv>criticalFValue))
    print('当前fv的置信度：（必须大于0.95才行）')
    confidence = scipy.stats.f.cdf(fv,dfn=dfn,dfd=dfd)
    print('{}对{}的影响显著性：{}, 当前的置信度是{}'.format(i,'species',confidence>0.95,confidence))

print(df.corr())