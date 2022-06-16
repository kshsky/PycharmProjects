import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy import stats

num = np.array([57,66,49,40,34,53,44,68,39,29,45,56,51,31,49,21,34,40,44,51,65,77,58])
industry=['零售业','零售业','零售业','零售业','零售业','零售业','零售业',
          '旅游业','旅游业','旅游业','旅游业','旅游业','旅游业',
          '航空公司','航空公司','航空公司','航空公司','航空公司',
          '家电制造业','家电制造业','家电制造业','家电制造业','家电制造业']
df=pd.DataFrame(data ={'num':num,'industry':industry})

#先查看方差是否一致
lingshou =df['num'][df.industry=='零售业']
lvyou =df['num'][df.industry=='旅游业']
hangkong =df['num'][df.industry=='航空公司']
jiadian =df['num'][df.industry=='家电制造业']

print(stats.levene(lingshou,lvyou,hangkong,jiadian))
print(stats.f_oneway(lingshou,lvyou,hangkong,jiadian))
