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

print(oridata.target)
df['species']=oridata.target

# print(df)

for i in columns:
    print('\n\n\n{}n\n\n\n\n'.format(i))
    x = df[i]
    y = df.species
    fit = ols('x~C(y)',df).fit()
    print('summmary')
    print(fit.summary())
    print('F检验')
    print(anova_lm(fit))

    dfn=fit.df_model
    dfd=fit.df_resid
    fv=fit.fvalue
    print('fvalue:',fv)
    print('检查f检验临界值：（fv大于该临界值）')
    # ppf: q
    criticalFValue= scipy.stats.f.ppf(q=1-0.05,dfn = dfn,dfd = dfd)
    print('{}对{}的影响显著性：{}'.format(i,'species',fv>criticalFValue))
    print('当前fv的置信度：（必须大于0.95才行）')
    # cdf(x, dfn, dfd, loc=0, scale=1)     Cumulative distribution function
    # ppf(q, dfn, dfd, loc=0, scale=1)   Percent point function(inverse of  cdf — percentiles). 分位点函数
    confidence = scipy.stats.f.cdf(fv,dfn=dfn,dfd=dfd)
    print('{}对{}的影响显著性：{}, 当前的置信度是{}'.format(i,'species',confidence>0.95,confidence))

print(df.corr())