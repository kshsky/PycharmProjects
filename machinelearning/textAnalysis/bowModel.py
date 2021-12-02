from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
corpus=["I come to  to  to China travel travel travel",
    "This is a car to polupar in China",
    "I love tea and to Apple ",
    "The work is to write some papers in science"]


print(vectorizer.fit_transform(corpus).toarray())
print(vectorizer.get_feature_names())
#"I"在英文中是停用词，不参加词频的统计，由于大部分的文本都只会使用词汇表中的很少一部分的词，
#因此我们的词向量中会有大量的0。也就是说词向量是稀疏的。在实际应用中一般使用稀疏矩阵来存储。

import pandas as pd
df = pd.DataFrame(vectorizer.fit_transform(corpus).toarray(),columns=vectorizer.get_feature_names())
print(df)


import urllib.parse
print(urllib.parse.quote('姓名'))
print(urllib.parse.unquote('%E5%A7%93%E5%90%8D'))

quoteStr=urllib.parse.quote("数据挖掘")
print(quoteStr)
rawurl = "%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98"
originStr=urllib.parse.unquote(rawurl)
print(originStr)
