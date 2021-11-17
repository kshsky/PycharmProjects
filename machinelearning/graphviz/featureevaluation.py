from graphviz import Digraph

# 黑体：SimHei 宋体：SimSun 新宋体：NSimSun 仿宋：FangSong 楷体：KaiTi

# 仿宋_GB2312：FangSong_GB2312 楷体_GB2312：KaiTi_GB2312
# plaintext
dot =  Digraph  (name='featureEvaluation',format = 'pdf',node_attr={'fontname':'SimSun','shape':'ellipse','style':'filled'})
dot.node(name='a',label='特征评价')
dot.node(name='b',label='特征初选')
dot.node(name='c',label='影响评价')
dot.node(name='d',label='模型法')

dot.edge('a','b')
dot.edge('a','c')
dot.edge('a','d')

dot.render('dataFile/feature',view=True)