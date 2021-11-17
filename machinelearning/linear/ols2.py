import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# x是施肥量，y是小麦产量
x=np.array([15,20,25,30,35,40,45])
y=np.array([330,345,365,405,445,450,455])

df=pd.DataFrame({'x':x,'y':y})
formula='y~x'
fit=ols(formula,df).fit()
print(fit.summary())

print(anova_lm(ols('y~x',df).fit()))

#假设检验 - F检验
import scipy.stats
f = fit.fvalue
print(f)
print(scipy.stats.f.ppf(q=1-0.05, dfn=1, dfd=5))
print(scipy.stats.f.cdf(f,dfn=1,dfd=5))

