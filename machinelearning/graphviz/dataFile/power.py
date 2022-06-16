import graphviz
from graphviz import Digraph

#五星殇
dot = Digraph(name='a',format='png',node_attr={'fontname':'SimSun'})

dot.node(name='effort',label='综合实力',style='filled',color='#1e90ff')
dot.node(name='meta',label='元能力',style='filled',color='tomato')
#============================原能力
dot.node(name='memory',label='记忆力',style='filled',color='tomato')
dot.node(name='calc',label='计算力',style='filled',color='tomato')

dot.node(name='physical',label='体力',style='filled',color='tomato')

dot.node(name='renew',label='恢复力',style='filled',color='tomato')
dot.node(name='utmost',label='极限力',style='filled',color='tomato')



dot.edge('meta','physical',color='tomato')
dot.edge('meta','memory',color='tomato')
dot.edge('meta','calc',color='tomato')
dot.edge('meta','renew',color='tomato')
dot.edge('meta','utmost',color='tomato')



#============================体力
dot.node(name='ridge',label='脊柱',style='filled',color='gold')
dot.node(name='arms',label='臂',style='filled',color='gold')
dot.node(name='leg',label='腿',style='filled',color='gold')

dot.node(name='pushup',label='俯卧撑',style='filled',color='gold')
dot.node(name='chinup',label='引体向上',style='filled',color='gold')
dot.node(name='handstandpushup',label='倒立撑',style='filled',color='gold')

dot.node(name='squat',label='蹲起',style='filled',color='gold')
dot.node(name='legraise',label='举腿',style='filled',color='gold')

dot.node(name='bridge',label='桥',style='filled',color='gold')

dot.edge('physical','arms',color='gold')
dot.edge('physical','leg',color='gold')
dot.edge('physical','ridge',color='gold')

dot.edge('arms','pushup',color='gold')
dot.edge('arms','chinup',color='gold')
dot.edge('arms','handstandpushup',color='gold')

dot.edge('leg','squat',color='gold')
dot.edge('leg','legraise',color='gold')

dot.edge('ridge','bridge',color='gold')

#===============================努力
dot.node(name='confidence',label='自信',style='filled',color='#1e90ff')
dot.node(name='respect',label='自尊',style='filled',color='#1e90ff')
# self-discipline 自律，自我修养，自我训练
dot.node(name='discipline',label='自律',style='filled',color='#1e90ff')
# self-reflective
dot.node(name='reflective',label='自省',style='filled',color='#1e90ff')

dot.node(name='improvement',label='自强',style='filled',color='#1e90ff')

dot.node(name='independent',label='自立',style='filled',color='#1e90ff')


dot.edge('effort','confidence',color='#1e90ff')
dot.edge('effort','respect',color='#1e90ff')
dot.edge('effort','discipline',color='#1e90ff')
dot.edge('effort','reflective',color='#1e90ff')
dot.edge('effort','improvement',color='#1e90ff')
dot.edge('effort','independent',color='#1e90ff')

#============================================
dot.edge('discipline','meta',color='#1e90ff')

dot.node(name='unitedFront',label='统战力',style='filled',color='limegreen')

dot.node(name='think',label='思考力',style='filled',color='limegreen')

dot.node(name='creative',label='创造力',style='filled',color='limegreen')
dot.node(name='express',label='表达力',style='filled',color='limegreen')


dot.edge('improvement','creative',color='limegreen')
dot.edge('reflective','unitedFront',color='limegreen')
dot.edge('confidence','think',color='limegreen')
dot.edge('respect','express',color='limegreen')

#======================== 统战力
dot.node(name='property',label='财力',style='filled',color='limegreen')
dot.edge('independent','property',color='limegreen')


graphviz.Source(dot.source)


# dot.render('dotfile/power.dot'.replace('helvetica', 'FangSong').replace('helvetica', 'FangSong'))
# with open(file,'r',encoding='utf-8') as f:
#     dot_graph = f.read()

with open('dotFile/power.dot',encoding='utf-8') as f:
    dot_txt = f.read()
fromDot = graphviz.Source(dot_txt.replace('helvetica', 'FangSong'),directory='dataFile',filename='allpower',format='pdf')
fromDot.view()

